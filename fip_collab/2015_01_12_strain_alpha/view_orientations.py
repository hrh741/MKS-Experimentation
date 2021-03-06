# -*- coding: utf-8 -*-
"""
Created on Fri May 23 14:25:50 2014

This script evaluates the success of a given MKS calibration and validation
through metrics like MASE and maximum error as well as plotting strain
fields and histograms.

@author: nhpnp3
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


euler_val = np.load('euler_97val_basal_s1.npy')
#euler_cal = np.load('euler_200cal.npy')

sn=5
min = 0
max = 50

fig = plt.figure(3)
ax3D = fig.add_subplot(111, projection='3d')
p3d = ax3D.scatter(euler_val[:,0,min:max],euler_val[:,1,min:max],euler_val[:,2,min:max])
plt.title('Discrete Orientation for Basal Texture')
ax3D.set_xlabel("$\phi1$")
ax3D.set_ylabel("$\Phi$")
ax3D.set_zlabel("$\phi2$")
#ax3D.set_xlim3d(0, 2*np.pi)
#ax3D.set_ylim3d(0, np.pi/2)
#ax3D.set_zlim3d(0, np.pi/3)

plt.figure(1)
plt.scatter(euler_val[:,0,min:max],euler_val[:,1,min:max])
plt.title('Selected Orientations for Hexagonal MKS Calibration')
plt.xlabel("$\phi1$")
plt.ylabel("$\Phi$")
#
#plt.figure(2)
#plt.scatter(euler_val[:max,sn,0],euler_val[:max,sn,2])
#plt.title('Selected Orientations for Hexagonal MKS Calibration')
#plt.xlabel("$\phi1$")
#plt.ylabel("$\phi2$")

#plt.figure(2)
#plt.scatter(euler_cal[:max,sn,0],euler_cal[:max,sn,1])
#plt.title('Selected Orientations for Hexagonal MKS Calibration')
#plt.xlabel("$\phi1$")
#plt.ylabel("$\Phi$")


