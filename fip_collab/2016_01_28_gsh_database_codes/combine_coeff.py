import numpy as np
import db_functions as fn
import h5py


filename = 'log_combine_coeff.txt'

""" Initialize important variables """
# pick range of indxmat to calculate
n_jobs = 50  # number of jobs submitted to PACE

N_p = 215  # number of GSH bases to evaluate
N_q = 20  # number of cosine bases to evaluate for theta
N_r = 14  # number of cosine bases to evaluate for en
cmax = N_p*N_q*N_r  # total number of permutations of basis functions
print cmax

""" Combine the results of the parallelized orthogonal regression """
# coeff is the combined vector of coefficients as calculated by the
# orthogonal regression
coeff = np.zeros(cmax, dtype='complex128')

c = 0
for tnum in xrange(n_jobs):

    fn.WP(str(tnum), filename)

    # load partially filled XtX arrays from each file
    f = h5py.File('coeff_prt_%s.hdf5' % tnum, 'r')
    coeff_prt = f.get('coeff_prt')

    for ii in xrange(coeff_prt.shape[0]):

        coeff[c] = coeff_prt[ii]
        c += 1

f = h5py.File('coeff_total.hdf5', 'w')
f.create_dataset('coeff', data=coeff)
f.close()
