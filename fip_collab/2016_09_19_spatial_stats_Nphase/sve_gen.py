import time
import h5py
import numpy as np
import functions as rr
from scipy.spatial.distance import cdist
from scipy.ndimage.filters import convolve
from scipy.ndimage.filters import gaussian_filter


def sample_H(H):
    Hvec = range(H)
    h1 = np.random.choice(Hvec)
    Hvec.remove(h1)
    h2 = np.random.choice(Hvec)

    return h1, h2


def bicrystal(el, ns, H, set_id, wrt_file):

    start = time.time()

    sshape = (ns, el, el, el)

    f = h5py.File("spatial_stats.hdf5", 'a')
    sves = f.create_dataset("sves_%s" % set_id, sshape, dtype='int64')

    gridvec = np.arange(el)
    gridx, gridy, gridz = np.meshgrid(gridvec, gridvec, gridvec)
    gridx = gridx.reshape(gridx.size)
    gridy = gridy.reshape(gridy.size)
    gridz = gridz.reshape(gridz.size)
    grid = np.vstack([gridx, gridy, gridz]).T

    for sn in xrange(ns):

        loc1 = np.zeros((1, 3))

        randi2 = np.int8(2*np.random.rand())
        randi6 = np.int8(6*np.random.rand())

        if randi6 == 0:
            loc1[0, 0] = 0
            loc1[0, 1] = np.int8(el*np.random.rand())
            loc1[0, 2] = np.int8(el*np.random.rand())
        elif randi6 == 1:
            loc1[0, 0] = el-1
            loc1[0, 1] = np.int8(el*np.random.rand())
            loc1[0, 2] = np.int8(el*np.random.rand())
        elif randi6 == 2:
            loc1[0, 0] = np.int8(el*np.random.rand())
            loc1[0, 1] = 0
            loc1[0, 2] = np.int8(el*np.random.rand())
        elif randi6 == 3:
            loc1[0, 0] = np.int8(el*np.random.rand())
            loc1[0, 1] = el-1
            loc1[0, 2] = np.int8(el*np.random.rand())
        elif randi6 == 4:
            loc1[0, 0] = np.int8(el*np.random.rand())
            loc1[0, 1] = np.int8(el*np.random.rand())
            loc1[0, 2] = 0
        elif randi6 == 5:
            loc1[0, 0] = np.int8(el*np.random.rand())
            loc1[0, 1] = np.int8(el*np.random.rand())
            loc1[0, 2] = el-1

        loc2 = np.int8(el*np.random.random((1, 3)))

        dist_loc1 = np.squeeze(cdist(grid, loc1))
        dist_loc2 = np.squeeze(cdist(grid, loc2))

        if randi2 == 0:
            dist_xgy = dist_loc1 >= dist_loc2
        if randi2 == 1:
            dist_xgy = dist_loc1 < dist_loc2

        dist_xgy = np.int8(dist_xgy)

        h1, h2 = sample_H(H)

        # print h1, h2
        # print np.sum(dist_xgy == 0)
        # print np.sum(dist_xgy == 1)

        sve = np.zeros(el**3, dtype='int8')

        sve[dist_xgy == 0] = h1
        sve[dist_xgy == 1] = h2

        # print np.unique(sve)

        sves[sn, ...] = sve.reshape(el, el, el)

    f.close()

    end = time.time()
    timeE = np.round((end - start), 3)

    msg = "%s bicrystal SVEs generated: %ss" % (ns, timeE)
    rr.WP(msg, wrt_file)


def bicrystal_orthog(el, ns, H, set_id, wrt_file):

    start = time.time()

    sshape = (ns, el, el, el)

    f = h5py.File("spatial_stats.hdf5", 'a')
    sves = f.create_dataset("sves_%s" % set_id, sshape, dtype='int64')

    for sn in xrange(ns):

        h1, h2 = sample_H(H)

        sves[sn, ...] = h1

        direc = np.int8(3*np.random.rand())  # define a random direction
        vf = np.int8(20*np.random.rand())+1  # define a random volume fraction

        if direc == 0:
            sves[sn, :vf, :, :] = h2
        elif direc == 1:
            sves[sn, :, :vf, :] = h2
        elif direc == 2:
            sves[sn, :, :, :vf] = h2

    f.close()

    end = time.time()
    timeE = np.round((end - start), 3)

    msg = "%s bicrystal SVEs generated: %ss" % (ns, timeE)
    rr.WP(msg, wrt_file)


def improcess(el, ns, H, set_id, wrt_file):

    start = time.time()

    sshape = (ns, el, el, el)

    f = h5py.File("spatial_stats.hdf5", 'a')
    sves = f.create_dataset("sves_%s" % set_id, sshape, dtype='int64')

    sigset = [0., .2, .4, .6, .8, 2, 5]

    for sn in xrange(ns):

        base = np.random.random((el, el, el))

        r2a = np.random.randint(1, 5)
        r2b = np.random.randint(1, 5)
        r2c = np.random.randint(1, 5)
        weights = np.random.random(size=(r2a, r2b, r2c))

        raw = convolve(base, weights, mode='wrap')

        blur = gaussian_filter(raw, sigma=np.random.choice(sigset))
        scaled = scale_array(blur)

        scaled_lin = scaled.reshape(el**3)
        sve = np.zeros((el**3))

        vf_bounds = np.zeros(H+1)
        vf_bounds[-1] = 1
        tmp = np.sort(np.random.rand(H-1))
        vf_bounds[1:H] = tmp

        for ii in xrange(H):
            indx = (scaled_lin > vf_bounds[ii])*(scaled_lin <= vf_bounds[ii+1])
            sve[indx] = ii

        sves[sn, ...] = sve.reshape(el, el, el)

    f.close()

    end = time.time()
    timeE = np.round((end - start), 3)

    msg = "%s bicrystal SVEs generated: %ss" % (ns, timeE)
    rr.WP(msg, wrt_file)


def delta(el, ns, H, set_id, wrt_file):

    start = time.time()

    sshape = (ns, el, el, el)

    f = h5py.File("spatial_stats.hdf5", 'a')
    sves = f.create_dataset("sves_%s" % set_id, sshape, dtype='int64')

    h1, h2 = sample_H(H)

    for sn in xrange(ns):
        sves[sn, ...] = h1
        sves[sn, 10, 10, 10] = h2

    f.close()

    end = time.time()
    timeE = np.round((end - start), 3)

    msg = "%s delta SVEs generated: %ss" % (ns, timeE)
    rr.WP(msg, wrt_file)


def inclusion(el, ns, H, set_id, wrt_file, vfrac):

    start = time.time()

    sshape = (ns, el, el, el)
    n_phase = len(vfrac)

    f = h5py.File("spatial_stats.hdf5", 'a')
    sves = f.create_dataset("sves_%s" % set_id, sshape, dtype='int64')

    for sn in xrange(ns):

        h1, h2 = sample_H(H)

        svetmp = np.int64(h1*np.ones(el**3))

        tmp = np.random.rand(el**3)

        for ii in xrange(n_phase):

            indx = (tmp > np.sum(vfrac[:ii]))*(tmp < np.sum(vfrac[:(ii+1)]))
            svetmp[indx] = h2

        sves[sn, ...] = svetmp.reshape(el, el, el)

    f.close()

    end = time.time()
    timeE = np.round((end - start), 3)

    msg = "%s SVEs with inclusions generated: %ss" % (ns, timeE)
    rr.WP(msg, wrt_file)


def inclusion_red(el, ns, H, set_id, wrt_file, vfrac):
    """this code generates inclusions in a matrix of the H=0 material
    based on a user supplied vector of inclusion volume fractions.
    These volume fractions are perturbed such as to blur the distinction
    between the SVE distributions"""

    start = time.time()

    sshape = (ns, el, el, el)

    vfrac = np.array(vfrac)
    n_phase = len(vfrac)

    f = h5py.File("spatial_stats.hdf5", 'a')
    sves = f.create_dataset("sves_%s" % set_id, sshape, dtype='int64')

    for sn in xrange(ns):

        # perturb vfrac to make things less defined
        delta = 0.0125*(2*(np.random.random(n_phase))-1)
        vfrac_ = vfrac + delta

        if np.any(vfrac_ < 0):
            print "negative volume fraction detected!!!"

        svetmp = np.zeros(el**3)

        tmp = np.random.rand(el**3)

        for ii in xrange(n_phase):

            indx = (tmp > np.sum(vfrac_[:ii]))*(tmp < np.sum(vfrac_[:(ii+1)]))
            svetmp[indx] = ii+1

        sves[sn, ...] = svetmp.reshape(el, el, el)

    f.close()

    end = time.time()
    timeE = np.round((end - start), 3)

    msg = "%s SVEs with inclusions generated: %ss" % (ns, timeE)
    rr.WP(msg, wrt_file)


def rod(el, ns, H, set_id, wrt_file, raxis):

    start = time.time()

    sshape = (ns, el, el, el)

    f = h5py.File("spatial_stats.hdf5", 'a')
    sves = f.create_dataset("sves_%s" % set_id, sshape, dtype='int64')

    cmat = np.unravel_index(np.arange(el**2), [el, el])
    cmat = np.array(cmat).T

    for c in xrange(el**2):
        ii, jj = cmat[c, :]

        if raxis == 0:
            sves[:, :, ii, jj] = np.int64(H*np.random.rand())
        elif raxis == 1:
            sves[:, ii, :, jj] = np.int64(H*np.random.rand())
        elif raxis == 2:
            sves[:, ii, jj, :] = np.int64(H*np.random.rand())

    f.close()

    end = time.time()
    timeE = np.round((end - start), 3)

    msg = "%s SVEs with rods generated: %ss" % (ns, timeE)
    rr.WP(msg, wrt_file)


def scale_array(raw):
    amin = raw.min()
    amax = raw.max()
    return (raw-amin)/(amax-amin)


if __name__ == '__main__':
    el = 21
    ns = 1
    H = 5
    set_id = 'test'
    wrt_file = 'test.txt'

    bicrystal(el, ns, H, set_id, wrt_file)
