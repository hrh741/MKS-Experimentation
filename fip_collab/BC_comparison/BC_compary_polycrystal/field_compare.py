# -*- coding: utf-8 -*-
"""
Created on Fri Aug 22 15:59:54 2014

@author: nhpnp3
"""
import numpy as np
import functions_ori_compare as fs
import matplotlib.pyplot as plt

el = 21




column_num = 1

filename = 'yuksel_ori_test.dat'
dat1 = fs.res_red(filename)

filename = 'Results_Ti64_RandomMicroFZreducedNewBCs_21x21x21_AbqInp_PowerLaw_00001_data_strain_max_C1.txt'
dat2 = fs.file_read(filename,column_num, el = el)


slc = 1
    
dmin = np.amin([dat1[slc,:,:],dat2[slc,:,:]])
dmax = np.amax([dat1[slc,:,:],dat2[slc,:,:]])

plt.subplot(121)
ax = plt.imshow(dat1[slc,:,:], origin='lower', interpolation='none',
    cmap='jet', vmin=dmin, vmax=dmax)
plt.title('MINED LE')
plt.colorbar(ax)  

plt.subplot(122)
ax = plt.imshow(dat2[slc,:,:], origin='lower', interpolation='none',
    cmap='jet', vmin=dmin, vmax=dmax)
plt.title('GOALI-Ti CPFEM')
plt.colorbar(ax)    