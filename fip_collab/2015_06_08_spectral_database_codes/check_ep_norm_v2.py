import numpy as np
import h5py

n_phi1 = 120
n_Phi = 31
n_phi2 = 20
n_tot = n_phi1 * n_Phi * n_phi2

cmat = np.zeros([21, 41])

for mm in xrange(1, 22):

    # Read Simulation info from "sim" file
    filename = 'sim_Ti64_tensor_%s.txt' % str(mm).zfill(2)

    f = open(filename, "r")

    linelist = f.readlines()

    euler = np.zeros([n_tot, 3])

    for k in xrange(n_tot):
        temp_line = linelist[k+1]
        euler[k, :] = temp_line.split()[1:4]

    f.close()

    etvec = np.linspace(.006, .01, 41)

    # Get data for all simulations

    # open file containing Matthew's data
    filename = 'Results_tensor_%s.hdf5' % str(mm).zfill(2)
    f_mwp = h5py.File(filename, 'r')

    ii = 1
    test_id = 'sim%s' % str(ii+1).zfill(7)

    dset = f_mwp.get(test_id)

    """
    Column order in each dataset:
    time,...
    sig11,sig22,sig33,sig12,sig13,sig23...
    e11,e22,e33,e12,e13,e23
    ep11,ep22,ep33,ep12,ep13,ep23
    """

    et = dset[:, 7:13]
    ep = dset[:, 13:19]

    # check that et is traceless
    et_tr = et[:, 0] + et[:, 1] + et[:, 2]

    et_tr_max = np.max(np.abs(et_tr))

    if et_tr_max > 1E-4:
        print ii
        print et_tr_max

    # calculate the norm of et
    et_norm = np.sqrt(et[:, 0]**2 + et[:, 1]**2 + et[:, 2]**2 +
                      et[:, 3]**2 + et[:, 4]**2 + et[:, 5]**2)

    # calculate the norm of ep
    ep_norm = np.sqrt(ep[:, 0]**2 + ep[:, 1]**2 + ep[:, 2]**2 +
                      ep[:, 3]**2 + ep[:, 4]**2 + ep[:, 5]**2)

    # check that et_norm is close enough to our approximation

    # find the maximum percent deviation between etvec and et_norm
    et_err = 100*np.max(np.abs((etvec-et_norm[59:])/etvec))
    et_err = et_err

    if et_err > 1:
        print ii
        msg = "maximum %% devation in et_norm scales: %s%%" % et_err
        print msg

    cmat[mm-1, :] = ep_norm[59:]

    f_mwp.close()

# mean_curve = np.mean(cmat, 0)
# std_curve = np.std(cmat, 0)

np.save("cmat.npy", cmat)
