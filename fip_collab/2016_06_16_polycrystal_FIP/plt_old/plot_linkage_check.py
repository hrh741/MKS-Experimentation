import numpy as np
import matplotlib.pyplot as plt
from constants import const
import h5py


def plot_check(ns_set, names_set, par, n_poly, plt_num):

    C = const()

    # colormat = np.random.rand(len(set_id_set), 3)
    colormat = np.array([[.3, .3, 1.],
                         [.3, 1., .3],
                         [1., .2, .2],
                         [0., .7, .7],
                         [.7, .0, .7],
                         [.7, .7, .0],
                         [.5, .3, .1],
                         [.3, .5, .1],
                         [.1, .3, .5]])

    f_reg = h5py.File("regression_results.hdf5", 'r')
    order = f_reg.get('order_%s' % par)[...]

    # """calculate # PCs required to reach desired explained variance"""

    # f_pc = h5py.File("pca_data.hdf5", 'r')
    # ratios = f_pc.get('ratios')[...]
    # f_pc.close()

    # tmp = np.cumsum(ratios)
    # tmp = np.arange(tmp.size)[tmp >= C["ev_lvl"]]
    # # max_ev = tmp.max()
    # # print "max explained variance: %s" % max_ev
    # # tmp = np.arange(tmp.size)[tmp >= max_ev]
    # n_pc = tmp[0] + 1

    # tmp = (order[:, 0] == n_pc)*(order[:, 1] == n_poly)

    # indx = np.arange(order.shape[0])[tmp]

    """calculate # PCs to minimize LOOCV mean error"""

    tmp = f_reg.get('loocv_err_%s' % par)[4:]
    # tmp = f_reg.get('meanerr_val_%s' % par)[4:]

    indx = np.argmin(tmp)+4

    print par
    print "n_pc, n_poly: %s" % str(order[indx, :])

    """find the results associated with the desired n_pc, n_poly"""

    """load the simulated and predicted responses"""
    Rsim = f_reg.get('Rsim_val_%s' % par)[...]
    Rpred = f_reg.get('Rpred_val_%s' % par)[indx, :]

    """write out the associated error"""
    err = np.abs(Rpred-Rsim)
    print "mean error: %s" % err.mean()
    print "max error: %s" % err.max()

    """plot the prediction equal to simulation line"""
    plt.figure(num=plt_num, figsize=[6, 5.75])

    minval = np.min([Rsim, Rpred])
    maxval = np.max([Rsim, Rpred])

    valrange = maxval-minval
    minval += -0.5*valrange
    maxval += 0.5*valrange
    line = np.array([minval, maxval])

    plt.plot(line, line, 'k-')

    for ii in xrange(len(ns_set)):

        name = names_set[ii]
        Rsim_tmp = Rsim[ii]
        Rpred_tmp = Rpred[ii]

        plt.plot(Rsim_tmp, Rpred_tmp,
                 marker='o', markersize=7, color=colormat[ii, :],
                 linestyle='', label=name)

    plt.title("predicted versus simulated %s" % par)
    plt.xlabel("simulation")
    plt.ylabel("prediction")
    plt.legend(loc='upper left', shadow=True, fontsize='medium')

    plt.xticks(rotation=20)
    plt.yticks(rotation=20)

    minval = np.min([Rsim, Rpred])
    maxval = np.max([Rsim, Rpred])
    valrange = maxval-minval
    minval += -0.1*valrange
    maxval += 0.1*valrange

    plt.axis([minval, maxval, minval, maxval])

    plt.tight_layout()

    f_reg.close()

    return indx


if __name__ == '__main__':
    C = const()
    ns_set = C['ns_val']
    names_set = C['names_val']
    par = "c0"

    plot_check(ns_set, names_set, par)
    plt.show()
