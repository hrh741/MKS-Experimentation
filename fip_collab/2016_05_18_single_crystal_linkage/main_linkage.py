import get_linkage as gl
import get_response as gr
from constants import const
import h5py

C = const()

names_cal = C['names_cal']
set_id_cal = C['set_id_cal']
# strt_cal = C['strt_cal']
ns_cal = C['ns_cal']
dir_cal = C['dir_cal']

names_val = C['names_val']
set_id_val = C['set_id_val']
# strt_val = C['strt_val']
ns_val = C['ns_val']
dir_val = C['dir_val']

"""get the data for the linkage"""
f = h5py.File("responses.hdf5", 'w')
f.close()

"""get the responses for the linkage"""
for ii in xrange(len(set_id_cal)):
    gr.read(ns_cal[ii], set_id_cal[ii])
for ii in xrange(len(set_id_val)):
    gr.read(ns_val[ii], set_id_val[ii])

"""create the specified array of linkages and cross validate"""

f = h5py.File("regression_results.hdf5", 'w')
f.close()

par = 'modulus'
gl.linkage(par)

par = 'strength'
gl.linkage(par)

"""
NOTES:
* sklearn.decomposition.PCA and scipy.linalg.interpolative.svd
give similar results if you subtract the means of the feature
values from the data matrix prior to SVD
* sklearn.decomposition.PCA does not work for complex values,
scipy.linalg.interpolative.svd does
"""
