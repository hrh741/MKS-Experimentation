# -*- coding: utf-8 -*-
"""
Created on Thursday, August 14th, 2014


@author: nhpnp3
"""

import numpy as np
import matplotlib.pyplot as plt
import functions_ti_alpha_fip_v1 as rr
import time

set_id = 'C3_E23_comparison'
st_comp = "E23"
comp_latex = "$\epsilon_{23}$"
cyc = 3
column_num = 6

## specify the file to write messages to 
wrt_file = '%s_%s.txt' %(set_id,time.strftime("%Y-%m-%d_h%Hm%M"))


## el is the # of elements per side of the cube 
el = 21 

### READ DATA FROM TEXT FILE ###

def file_read(filename, column_num):
    
    f = open(filename, "r")
    
    linelist = f.readlines()
    
    # line0 is the index of first line of the data
    line0 = 2;      
    
    E_pre = np.zeros((21**3))
    c = -1
    
    ## This reads through all the lines in the file.
     
    for k in xrange(21**3):
        c += 1                        
        E_pre[k] = linelist[line0 + c].split()[column_num]
    
    f.close()    
         
    E = np.swapaxes(np.reshape(np.flipud(E_pre), [el,el,el]),1,2)

    return E

filename = 'Results_Ti64_RandomMicroFZreducedNewBCs_21x21x21_AbqInp_PowerLaw_00001_data_strain_max_C3.txt'
C_CPFEM = file_read(filename,column_num)

filename = 'Results_Ti64_RandomMicroFZreducedNewBCs_21x21x21_AbqInp_AnisoLE_00001_data_strain_max_C3.txt'
C_LE = file_read(filename,column_num)


### VISUAL COMPARISON OF CPFEM AND LE+PY SIMULATIONS ###

plt.close()

## pick a slice perpendicular to the z-direction
slc = 10

## Plot slices of the response
plt.figure(1)

## find the min and max of both datasets for the slice of interest
#(needed to scale both images the same) 
dmin = np.amin([C_CPFEM[:,:,slc],C_LE[:,:,slc]])
dmax = np.amax([C_CPFEM[:,:,slc],C_LE[:,:,slc]])

plt.subplot(121)
ax = plt.imshow(C_CPFEM[:,:,slc], origin='lower', interpolation='none',
    cmap='jet', vmin=dmin, vmax=dmax)
plt.title('Cycle 3 maximum, CPFEM, %s' %comp_latex)
plt.colorbar(ax)  

plt.subplot(122)
ax = plt.imshow(C_LE[:,:,slc], origin='lower', interpolation='none',
    cmap='jet', vmin=dmin, vmax=dmax)
plt.title('Cycle 3 maximum, LE, %s' %comp_latex)
plt.colorbar(ax)    


# Plot a histogram representing the frequency of strain levels with separate
# channels for each phase of each type of response.
plt.figure(2)


C_CPFEM_lin = np.reshape(C_CPFEM,el**3)
C_LE_lin = np.reshape(C_LE,el**3)

## find the min and max of both datasets
dmin = np.amin([C_CPFEM,C_LE])
dmax = np.amax([C_CPFEM,C_LE])

# select the desired number of bins in the histogram
bn = 40

weight = np.ones_like(C_CPFEM_lin)/(el**3)

## response histograms

n, bins, patches = plt.hist(C_CPFEM_lin, bins = bn, histtype = 'step', hold = True,
                            range = (dmin, dmax), weights=weight, color = 'white')
bincenters = 0.5*(bins[1:]+bins[:-1])

C_CPFEM_lin, = plt.plot(bincenters,n,'k', marker = 's', linestyle = '-', lw = 2.5)

n, bins, patches = plt.hist(C_LE_lin, bins = bn, histtype = 'step', hold = True,
                            range = (dmin, dmax), weights=weight, color = 'white')

C_LE_lin, = plt.plot(bincenters,n,'r', marker = 'o', linestyle = '-', lw = 1.0)
   

plt.grid(True)

plt.legend([C_CPFEM_lin, C_LE_lin], ["CPFEM", "LE"])

plt.xlabel('%s' %comp_latex)
plt.ylabel("Number Fraction")

plt.title("Frequency comparison of %s in CPFEM and LE for cycle %s" %(comp_latex,cyc))



## Generate data file for statistical summary

def mase_meas(C_cp,C_py,C_cp_avg):    
    MASE = 0
    for k in xrange(el**3):
        [u,v,w] = np.unravel_index(k,[el,el,el])
        MASE += ((np.abs(C_cp[u,v,w] - C_py[u,v,w]))/(C_cp_avg * el**3))
        
    return MASE
    
def max_err_meas(C_cp,C_py,C_cp_avg):
    max_err = np.amax(C_cp-C_py)/C_cp_avg  
    
    return max_err


cyc = 3

msg = 'Average %s, CPFEM, Cycle %s: %s' %(st_comp,cyc,np.average(C_CPFEM))
rr.WP(msg,wrt_file)
msg = 'Average %s, LE, Cycle %s: %s' %(st_comp,cyc,np.average(C_LE))
rr.WP(msg,wrt_file)

msg = 'Standard deviation %s, CPFEM, Cycle %s: %s' %(st_comp,cyc,np.std(C_CPFEM))
rr.WP(msg,wrt_file)
msg = 'Standard deviation %s, LE, Cycle %s: %s' %(st_comp,cyc,np.std(C_LE))
rr.WP(msg,wrt_file)    

msg = 'Minimum %s, CPFEM, Cycle %s: %s' %(st_comp,cyc,np.min(C_CPFEM))
rr.WP(msg,wrt_file)
msg = 'Minimum %s, LE, Cycle %s: %s' %(st_comp,cyc,np.min(C_LE))
rr.WP(msg,wrt_file)

msg = 'Maximum %s, CPFEM, Cycle %s: %s' %(st_comp,cyc,np.max(C_CPFEM))
rr.WP(msg,wrt_file)
msg = 'Maximum %s, LE, Cycle %s: %s' %(st_comp,cyc,np.max(C_LE))
rr.WP(msg,wrt_file)

msg = 'Mean absolute strain error (MASE), Cycle %s: %s%%' %(cyc,mase_meas(C_CPFEM,C_LE,np.average(C_CPFEM))*100)
rr.WP(msg,wrt_file)

msg = 'Maximum error, Cycle %s: %s%%' %(cyc,max_err_meas(C_CPFEM,C_LE,np.average(C_CPFEM))*100)
rr.WP(msg,wrt_file)








    







