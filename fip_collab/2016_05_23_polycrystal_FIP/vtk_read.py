# -*- coding: utf-8 -*-
"""
Created on Mon Jun 16 11:32:08 2014

@author: nhpnp3
"""

import functions as rr
import numpy as np
from constants import const
import time
import os
import h5py


def read_euler(strt, ns, set_id, newdir, funit):

    start = time.time()

    C = const()

    euler = np.zeros([ns, 3, C['el']**3], dtype='float64')

    # nwd = os.getcwd() + '\\' + newdir
    nwd = os.getcwd() + '/' + newdir  # for unix
    os.chdir(nwd)

    for ii in xrange(ns):
        sn = strt + ii + 1
        filename = "Results_Ti64_Dream3D_XdirLoad_210microns_9261el_AbqInp_PowerLaw_%s_data_v2_06.vtk" % sn
        euler[ii, :, :] = rr.read_vtk_vector(filename=filename)

    if funit == 1:
        euler = euler * (np.pi/180.)

    print euler.min()

    # return to the original directory
    os.chdir('..')

    f = h5py.File("spatial.hdf5", 'a')
    dset_name = 'euler_%s' % set_id
    f.create_dataset(dset_name, data=euler)
    f.close()

    end = time.time()
    timeE = np.round((end - start), 3)

    msg = 'euler angles read from .vtk file for %s: %s seconds' \
          % (set_id, timeE)
    rr.WP(msg, C['wrt_file'])


def read_fip(strt, ns, set_id, newdir):

    start = time.time()

    C = const()

    fip = np.zeros([ns, C['el']**3])

    # nwd = os.getcwd() + '\\' + newdir
    nwd = os.getcwd() + '/' + newdir  # for unix
    os.chdir(nwd)

    for ii in xrange(ns):
        sn = strt + ii + 1
        filename = "Results_Ti64_Dream3D_XdirLoad_210microns_9261el_AbqInp_PowerLaw_%s_data_v2_06.vtk" % sn
        fip[ii, :] = rr.read_vtk_scalar(filename=filename)

    """return to the original directory"""
    os.chdir('..')

    f = h5py.File("raw_responses.hdf5", 'a')
    f.create_dataset('fip_%s' % set_id, data=fip)
    f.close()

    end = time.time()
    timeE = np.round((end - start), 3)

    msg = 'fip values read from .vtk file for %s: %s seconds' % (set_id,
                                                                 timeE)
    rr.WP(msg, C['wrt_file'])
