import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import h5py


f = h5py.File('slice.hdf5', 'r')
slice = f.get('slice')[...]
f.close()

fig = plt.figure(num=1, figsize=[10, 6])
ax = fig.add_subplot(111, projection='3d')

ax.scatter(slice[:, 1], slice[:, 2], slice[:, 5].real, c='b')
ax.scatter(slice[:, 1], slice[:, 2], slice[:, 6].real, c='r')

plt.show()
