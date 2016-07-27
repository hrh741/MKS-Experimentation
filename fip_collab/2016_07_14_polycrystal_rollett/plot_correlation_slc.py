import numpy as np
import matplotlib.pyplot as plt
from constants import const
import h5py


def pltcorr():

    C = const()

    f = h5py.File("slice.hdf5", 'r')
    euler = f.get('euler')[...]
    corr = f.get('corr')[...]
    set_id = f.get('set_id')[...]
    iA = np.int64(f.get('iA')[...])
    f.close()

    """Plot slices of the response"""
    fig = plt.figure(figsize=[15, 5])

    lt0 = euler < 0
    euler += 2*np.pi*lt0

    plt.subplot(121)
    ax = plt.imshow(euler,
                    interpolation='none', cmap='magma')
    plt.colorbar(ax)
    plt.title('phi1 field')

    plt.subplot(122)
    ax = plt.imshow(corr,
                    interpolation='none', cmap='viridis')
    plt.colorbar(ax)
    plt.title('ff: %s, %s' % (C['cmat'][iA, 0], C['cmat'][iA, 1]))

    fig_name = 'correlation_%s_L%s_L%s.png' % (set_id, C['cmat'][iA, 0], C['cmat'][iA, 1])
    fig.canvas.set_window_title(fig_name)
    plt.savefig(fig_name)


if __name__ == '__main__':

    pltcorr()
    plt.show()
