import numpy as np
# import itertools as it
import db_functions as fn
import gsh_hex_tri_L0_16 as gsh
import h5py
import time
import sys


tnum = np.int64(sys.argv[1])

filename = 'log_integrate_parallel_%s.txt' % str(tnum)

""" Load Y vec """
f = h5py.File('var_extract_total.hdf5', 'r')
var_set = f.get('var_set')
sinphi = np.sin(var_set[:, 1])
Y = var_set[:, 3]
f.close

""" Initialize important variables """
N_p = 215  # number of GSH bases to evaluate

inc = 6
sub2rad = inc*np.pi/180.

n_jobs = 5.  # number of jobs submitted to cluster

""" Calculate basis function indices """
cmax = N_p  # total number of permutations of basis functions
fn.WP(str(cmax), filename)

# cmat is the matrix containing all permutations of basis function indices
cmat = np.arange(cmax)

""" Deal with the parallelization of this operation specifically pick range
of indxmat to calculate """
n_ii = np.int64(np.ceil(np.float(cmax)/n_jobs))  # number dot products per job
fn.WP(str(n_ii), filename)

ii_stt = tnum*n_ii  # start index
if (tnum+1)*n_ii > cmax:
    ii_end = cmax
else:
    ii_end = (tnum+1)*n_ii  # end index

msg = "ii_stt = %s" % ii_stt
fn.WP(msg, filename)
msg = "ii_end = %s" % ii_end
fn.WP(msg, filename)

""" perform the orthogonal regressions """

coeff_prt = np.zeros(ii_end-ii_stt, dtype='complex128')

f = h5py.File('X_parts.hdf5', 'r')
c = 0

indxvec = gsh.gsh_basis_info()

bsz_gsh = sub2rad**3

for ii in xrange(ii_stt, ii_end):

    msg = str(ii)
    fn.WP(msg, filename)

    st = time.time()

    p = cmat[ii]
    basis_p = f.get('p_%s' % p)[...]

    ep_set = np.squeeze(basis_p)

    msg = "load time: %ss" % np.round(time.time()-st, 3)
    fn.WP(msg, filename)

    st = time.time()

    l = indxvec[p, 0]
    c_gsh = (1./(2.*l+1.))*(3./(2.*np.pi**2))

    c_tot = c_gsh*bsz_gsh

    tmp = c_tot*np.sum(Y*ep_set.conj()*sinphi)

    del ep_set

    coeff_prt[c] = tmp

    msg = "regression time: %ss" % np.round(time.time()-st, 3)
    fn.WP(msg, filename)

    c += 1

f.close()

f = h5py.File('coeff_prt_%s.hdf5' % tnum, 'w')
f.create_dataset('coeff_prt', data=coeff_prt)
f.close()
