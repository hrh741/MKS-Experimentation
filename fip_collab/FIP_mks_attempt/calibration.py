# -*- coding: utf-8 -*-
"""
Created on Fri May 23 14:25:50 2014

This script performs the MKS calibration given the microstructure function 
and the FIP response, both in frequency space.

@author: nhpnp3
"""

import time
import numpy as np
import functions_ti_alpha_fip_v1 as rr
from functools import partial


## el is the # of elements per side of the cube 
el = 21 
## select which order terms with nearest neighbors you would like to analyze
order = 1
## the number of sample microstructures for calibration.
ns = 200
## specify the number of local states you are using
H = 15
## specify the set designation (string format)
set_id = 'cal'
## specify the file to write messages to 
wrt_file = 'calib_%s%s_%s.txt' %(ns,set_id,time.strftime("%Y-%m-%d_h%Hm%M")) 


M = np.load('M_%s%s.npy' %(ns,set_id))
fip_fft = np.load('fip_fft_%s%s.npy' %(ns,set_id))

start = time.time()

specinfc = np.zeros((el**3,H),dtype = 'complex64')

## here we perform the calibration for the scalar FIP

specinfc[0,:] = rr.calib(0,M,fip_fft,0,H,el,ns)
[specinfc[1,:],p] = rr.calib(1,M,fip_fft,0,H,el,ns)

## calib_red is simply calib with some default arguments
calib_red = partial(rr.calib,M=M,fip_fft=fip_fft,
                    p=p,H=H,el=el,ns=ns)
specinfc[2:(el**3),:] = np.asarray(map(calib_red,range(2,el**3)))
 

np.save('specinfc_%s%s' %(ns,set_id),specinfc)

end = time.time()
timeE = np.round((end - start),3)
msg = 'Calibration: %s seconds' %timeE
rr.WP(msg,wrt_file)