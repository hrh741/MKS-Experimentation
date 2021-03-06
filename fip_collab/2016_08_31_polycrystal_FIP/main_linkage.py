import vtk_read as vtk
import get_linkage as gl
import get_response as gr
from constants import const
import h5py

C = const()

sid_cal = C['sid_cal']
names_cal_alt = C['names_cal_alt']
sid_cal = C['sid_cal']
sid_cal_split = C['sid_cal_split']
strt_cal = C['strt_cal']
ns_cal = C['ns_cal']
ns_cal_split = C['ns_cal_split']

sid_val = C['sid_val']
names_val_alt = C['names_val_alt']
sid_val = C['sid_val']
sid_val_split = C['sid_val_split']
strt_val = C['strt_val']
ns_val = C['ns_val']
ns_val_split = C['ns_val_split']

# """get the data for the linkage"""

# f = h5py.File("raw_responses.hdf5", 'w')
# f.close()

# """Gather data from vtk files"""
# dir_fip = 'fip'

# for ii in xrange(len(sid_cal)):
#     vtk.read_fip(strt_cal[ii], ns_cal[ii], names_cal_alt[ii], sid_cal[ii],
#                  dir_fip)
# for ii in xrange(len(sid_val)):
#     vtk.read_fip(strt_val[ii], ns_val[ii], names_val_alt[ii], sid_val[ii],
#                  dir_fip)

f = h5py.File("responses.hdf5", 'w')
f.close()

"""get the fitting coefficients for the linkage"""
for ii in xrange(len(sid_cal_split)):
    gr.resp(ns_cal_split[ii], sid_cal_split[ii])
for ii in xrange(len(sid_val_split)):
    gr.resp(ns_val_split[ii], sid_val_split[ii])

"""create the specified array of linkages and cross validate"""

f = h5py.File("regression_results_L%s.hdf5" % C['H'], 'w')
f.close()

par = 'mu'
gl.linkage(par)

par = 'sigma'
gl.linkage(par)

"""
NOTES:
* sklearn.decomposition.PCA and scipy.linalg.interpolative.svd
give similar results if you subtract the means of the feature
values from the data matrix prior to SVD
* sklearn.decomposition.PCA does not work for complex values,
scipy.linalg.interpolative.svd does
"""
