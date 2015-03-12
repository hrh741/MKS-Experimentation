# -*- coding: utf-8 -*-
"""
This script reads a set of microstructures designated by the set-ID and saves
the microstructure function in real and frequency space.

Written by Noah Paulson Fri March 5 2015
"""

import time
import os
import numpy as np
import functions as rr
import scipy.io as sio
import itertools as it


# @profile
def msf(el, ns, Hi, order, set_id, wrt_file):

    st = time.time()

    # import microstructures
    microstructure = sio.loadmat('M_%s%s.mat' % (ns, set_id))['M']
    microstructure = microstructure.swapaxes(0, 1)

    tmp = np.zeros([Hi, ns, el**3])

    for h in xrange(Hi):
        tmp[h, ...] = (microstructure == h).astype(int)

    del microstructure

    tmp = tmp.swapaxes(0, 1)
    pre_micr = tmp.reshape([ns, Hi, el, el, el])

    del tmp

    np.save('pre_msf_%s%s' % (ns, set_id), pre_micr)

    direc = 'M_%s%s' % (ns, set_id)
    os.mkdir(direc)
    nwd = os.getcwd() + '/' + direc  # for unix
    # nwd = os.getcwd() + '\\' + direc
    os.chdir(nwd)

    for sn in xrange(ns):

        # real space microstructure coefficients
        [micr, H] = mf(pre_micr[sn, ...], el, Hi, order)

        # take FFT of microstructure coefficients
        M = np.fft.fftn(micr, axes=[1, 2, 3]).reshape([H, el**3])

        del micr

        np.save('M_%s%s_%s' % (ns, set_id, sn), M)

        del M

        msg = 'sn: %s' % sn
        rr.WP(msg, wrt_file)

    os.chdir('..')

    msg = "generate real space microstructure and perform FFT:"\
          " %s seconds" % np.round((time.time() - st), 3)
    rr.WP(msg, wrt_file)

    return H


def mf(micr, el, Hi, order):

    if order == 1:
        H = Hi
        m = micr

    if order == 2:

        hs = np.array([[1, 1], [0, 0], [1, 0], [0, 1]])
        vec = np.array([[1, 0], [1, 1], [1, 2]])

        H = hs.shape[0] * vec.shape[0]

        k = 0
        m = np.zeros([H, el, el, el])
        for hh in xrange(hs.shape[0]):
            for t in xrange(vec.shape[0]):
                a1 = micr[hs[hh, 0], ...]
                a2 = np.roll(micr[hs[hh, 1], ...], vec[t, 0], vec[t, 1])
                m[k, ...] = a1 * a2
                k = k + 1

    if order == 7:

        hs = np.array(list(it.product([0, 1], repeat=7)))
        vec = np.array([[1, 0], [1, 1], [1, 2], [-1, 0], [-1, 1], [-1, 2]])

        vlen = vec.shape[0]
        H = hs.shape[0]

        m = np.zeros([H, el, el, el])

        for hh in xrange(H):
            pre_m = micr[hs[hh, 0], ...]
            for t in xrange(vlen):
                a_n = np.roll(micr[hs[hh, t+1], ...], vec[t, 0], vec[t, 1])
                pre_m = pre_m * a_n
            m[hh, ...] = pre_m

    m = m.astype(int)

    return m, H

if __name__ == "__main__":
    st = time.time()
    msf(21, 200, 2, 7, 'calRpc', 'M', 'test.txt')
    print "elapsed time: %s" % (time.time() - st)
