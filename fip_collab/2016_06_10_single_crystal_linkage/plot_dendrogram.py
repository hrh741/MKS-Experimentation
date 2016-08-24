import numpy as np
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as hie
from constants import const
import h5py


def pltdend(ns_set, set_id_set, names_set):

    C = const()

    plt.figure(num=4, figsize=[7, 5])

    y = np.zeros([ns_set[0], C['n_pc_tot']])

    f_red = h5py.File("spatial_reduced.hdf5", 'r')

    for ii in xrange(len(set_id_set)):

        reduced = f_red.get('reduced_%s' % set_id_set[ii])[...]

        y = reduced

    print "y.shape: %s" % str(y.shape)

    f_red.close()

    Z = hie.linkage(y, method='average')

    # hie.dendrogram(Z, orientation='top', distance_sort='ascending')
    # plt.xticks(10*np.arange(8)+5, names_set, rotation=45.0)

    hie.dendrogram(Z, orientation='right', p=2, truncate_mode='level')

    plt.xlabel('Euclidean distance')

    plt.tight_layout()


if __name__ == '__main__':

    C = const()
    ns_set = C['ns_val']
    set_id_set = C['set_id_val']
    names_set = C['names_val']

    pltdend(ns_set, set_id_set, names_set)

    plt.show()