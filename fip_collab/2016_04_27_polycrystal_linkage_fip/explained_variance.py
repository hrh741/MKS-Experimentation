import numpy as np
import matplotlib.pyplot as plt
import h5py


def variance():

    f = h5py.File("pca_data.hdf5", 'r')
    ratios = f.get('ratios')[...]
    f.close()

    plt.figure(2)
    plt.plot(np.arange(ratios.size)+1, np.cumsum(ratios), 'ko-')
    plt.xlabel('pc number')
    plt.xticks(np.arange(ratios.size)+1)
    plt.ylabel('pca cumulative explained variance (%)')
    plt.title('pca cumulative explained variance plot')
    plt.show()

    plt.show()


if __name__ == '__main__':
    variance()
