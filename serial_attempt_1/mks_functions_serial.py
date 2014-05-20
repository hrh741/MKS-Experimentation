# -*- coding: utf-8 -*-
"""
Functions for 3D, isotropic MKS analyses

Noah Paulson, 5/8/2014
"""

import numpy as np
import matplotlib.pyplot as plt
import time
import itertools as it
import scipy.io as sio

def eval_meas(mks_R, resp_val, el=21):
    """
    Summary:
        This function returns the mean absolute strain error (MASE) and the
        average strain (avgE)
    Inputs:
        mks_R: (el,el,el) The response predicted by the MKS for the validation
        microstructure
        resp_val: (el,el,el) the FEM response for the validation microstructure
        el (int): the number of elements per side of the microstructure cube
    Outputs:
        avgE: (scalar) The average strain of the predicted response
        MASE: (scalar) The mean absolute strain error between the MKS
        prediction and FEM response for the validation microstructure
    """
    avgE = np.average(mks_R[:,:,:])
    MASE = 0
    for k in xrange(el**3):
        [u,v,w] = np.unravel_index(k,[el,el,el])
        MASE = MASE + ((np.abs(resp_val[u,v,w] - mks_R[u,v,w]))/(avgE * el**3))
        
    return avgE, MASE

def gen_micr(file_name, read_dat, ns, el):
    """
    Summary:
        This function reads the microstructures for all samples (calibration
        and validation) from a matlab data file, rearanges them into ns # of
        el x el x el cubes, and saves them in the .npy file format
    Inputs:
        file_name (string): the filename for the matlab '.mat' file
        read_dat (int): if read_dat = 1 the '.mat' file is read and rearanged,
        if read_dat = 0 micr is simply loaded from the '.npy' file
        ns (int): the total number of microstructures (for calibration and 
        validation)
        el (int): the number of elements per side of the microstructure cube
    Output:
        micr ([el,el,el,ns],int8): The binary microstructures for calibration
        and validation
    """
    if read_dat == 1:        
        ## convert the matlab file to an array in python        
        pre_micr = sio.loadmat(file_name)    
        pre_micr = pre_micr['M'].astype(int)   
        
        ## here we perform flips and reshapes to enact the proper arrangement 
        ## of spatial locations in the 3D cub
        micr = np.zeros((el,el,el,ns),dtype = 'int8') 
        for jj in range(ns):    
            micr[:,:,:,jj] = np.swapaxes(np.reshape(np.flipud(pre_micr[:,jj]), [el,el,el]),1,2)
    
        ## save the microstructure array
        np.save('micr_%s' %ns,micr)
    else:        
        micr = np.load('micr_%s.npy' %ns)
    
    return micr


def independent_columns(A, tol = 1e-05):
    """
    Summary:    
        This function returns an vector of the independent columns of a matrix        
        Note: the answer may not be unique; this function returns one of many
        possible answers.
        Source: http://stackoverflow.com/q/1331249
    Inputs:
        A (generic array {numerical})
        tol (float): This number specifies how numerically close two columns
        must be to be dependent.
    Outputs:
        independent (vector of int): vector containing the indices of the 
        independent columns of A
    """
    Q, R = np.linalg.qr(A)
    independent = np.where(np.abs(R.diagonal()) > tol)[0]
    return independent


def load_fe(read_dat=0,ns=151,el=21):
    """    
    Summary:        
        responses of the black and white delta microstructures and random
        microstructures.
    Inputs:
        read_dat (int): if read_dat = 1 the '.dat' files are read and compiled,
        if read_dat = 0 resp is simply loaded from the '.npy' file
        ns (int): the total number of microstructures (for calibration and 
        validation)
        el (int): the number of elements per side of the microstructure cube        
    Outputs:
        resp ([el,el,el,ns],float): The FEM responses of all calibration and 
        validation microstructures
        msg (string): A message detailing how resp was loaded
    """    

    if read_dat == 1:
        start = time.time()    
        
        resp = np.zeros((el,el,el,ns),dtype = 'float64')
        for n in xrange(ns):
            filename = "sq21_5cont_%s.dat" %(n+1) 
            resp[:,:,:,n] = res_red(filename)
        
        np.save('FE_results_%' %ns,resp)    
        
        end = time.time()
        timeE = np.round((end - start),1)
        msg = "Import FE results: %s seconds" %timeE
    
    ## if read_dat == 0 the script will simply reload the results from a 
    ## previously saved FE_results.npy
    else:
        resp = np.load('FE_results_%s.npy' %ns)
        msg = "FE results loaded"  
    
    return [resp,msg]


def mf(micr_sn, el, H, order):
    """
    Summary:
        This function takes in a single microstructure, and generates all of
        the local states based on the desired order of terms. It does this by
        shifting the microstructure in pre-defined directions, and then
        performing an element-wise multiplication. This reveals the
        conformation for a higher order local state.
    Inputs:
        micr_sn ([el,el,el],int8): the arangement of black and white cells in
        the cube for a single microstructure (from the micr variable)
        el (int): the number of elements per side of the microstructure cube
        H (int): the total number of local states in the microstructure
        function (including higher order comformations)
        order (int): the order of the terms used for 
    Output:
        m_sn ([el,el,el,H],int): The microstructure function for a single
        microstructure, including higher order local state conformations
    """
    ## 1st order microstructure function generation
    pm = np.zeros([el,el,el,2])
    pm[:,:,:,0] = (micr_sn == 0)
    pm[:,:,:,1] = (micr_sn == 1)
    pm = pm.astype(int)

    if order == 1:
        ## pm already represents the microstructure function for first order
        ## terms        
        m_sn = pm          
        
    if order == 2:
        ## in hs, the first element of each row represents the desired local
        ## state of the original cell (black or white), and the second is
        ## the desired local state after the microstructure is shifted.
        hs = np.array([[1,1],[0,0],[1,0],[0,1]])
        ## in vec, the first element of each row represents the number of 
        ## elements to shift the microstructure, and the second is the
        ## dimension along which the microstructure should be shifted
        vec = np.array([[1,0],[1,1],[1,2]])
        
        ## in the generation of the microstructure for second order
        ## localization terms the microstructure is rolled in a single
        ## direction for each term.
        k = 0
        m_sn = np.zeros([el,el,el,H])
        for hh in xrange(len(hs[:,0])):
            for t in xrange(len(vec[:,0])):
                a1 = pm[:,:,:,hs[hh,0]]
                a2 = np.roll(pm[:,:,:,hs[hh,1]],vec[t,0],vec[t,1])
                m_sn[:,:,:,k] = a1 * a2
                k = k + 1
        
    if order == 7:            
        ## Here hs is automatically generated
        hs = np.array(list(it.product([0,1],repeat=7)))
        vec = np.array([[1,0],[1,1],[1,2],[-1,0],[-1,1],[-1,2]])
        
        vlen = len(vec[:,0])
        m_sn = np.zeros([el,el,el,H])
        
        ## in the generation of the microstructure for seventh order terms
        ## the microstructure is rolled in all 6 directions. These 7 
        ## microstructures are all multiplied together.
        for hh in xrange(H):  
            a1 = pm[:,:,:,hs[hh,0]]    
            pre_m = a1  
            for t in xrange(vlen):      
                a_n = np.roll(pm[:,:,:,hs[hh,t+1]],vec[t,0],vec[t,1])
                pre_m = pre_m * a_n  
            m_sn[:,:,:,hh] = pre_m
            
    m_sn = m_sn.astype(int)
   
    return m_sn


def pha_loc(filename="msf.txt",read_dat=0,el=21):   
    """
    Summary:    
        Opens file with microstructure info where is column represents a single
        microstructure. Converts each microstructure column vector into a 
        cube data structure with indexing which matches that of the 
        Finite Element structure
    Inputs:
        filename (string): the name of the '.txt' file containing the 
        microstructures
        read_dat (int): if read_dat = 1 the '.txt' file is read and compiled,
        if read_dat = 0 micr is simply loaded from the '.npy' file        
    Output: 
        micr ([el,el,el,ns],int8): The binary microstructures for calibration
        and validation
    """    
    
    if read_dat == 1:
       
        f = open(filename, "r")
    
        linelist = f.readlines()
        
        ns = len(linelist[0].split())    
        pre_micr1 = np.zeros((21**3,ns), dtype = 'int8')    
        
        for ii in xrange(21**3):
            for jj in xrange(ns):
                pre_micr1[ii,jj] = linelist[ii].split()[jj]
    
        f.close()
                
        ## element 4630 is at the centroid of a 21x21x21 dataset
#        print e11cond[4630]
                
        ## here we reshape the data from a 9261 length vector to a 21x21x21
        ## 3D matrix
        pre_micr2 = np.zeros((21,21,21,ns), dtype = 'int8')
        micr = np.zeros((21,21,21,ns), dtype = 'int8')
        
        for jj in range(ns):    
            pre_micr2 = np.reshape(np.flipud(pre_micr1[:,jj]), [21,21,21])
            micr[:,:,:,jj] = np.swapaxes(pre_micr2,1,2)
            
        np.save('micr_%s' %ns,(micr,ns))

    else:    
        micr = np.load('micr_%s.npy' %ns)        
        
    return micr
    

def res_red(filename = "21_1_noah.dat", el = 21, slc = 10):
    """
    Summary:    
        This function reads the E11 values from a .dat file and reorganizes
        the data into a el x el x el array with the correct organization
        It will also plot a certain x-slice in the dataset if called within
        this script.
    Inputs:
        filename (string): the name of the '.dat' file containing the 
        FEM response        
        el (int): the number of elements per side of the microstructure cube
        slc (int): which slice to plot (if this function is called in this
        very script)
    Outputs:
        e11mat ([el,el,el],float): the FEM response of the '.dat' file of
        interest
    """
    f = open(filename, "r")

    linelist = f.readlines()

    # finds a location several lines above the start of the data
    # linelist[n] reads the entire line at location n
    for n in range(1000):
        if 'THE FOLLOWING TABLE' in linelist[n]:
            break

    # line0 is the index of first line of the data
    line0 = n + 5;      

    e11 = np.zeros((21**3,8))
    c = 0

    # this series of loops generates a 9261x8 dataset of E11s (element x integration point) 
    for ii in range(21**3):
        for jj in range(8):
            e11pre = linelist[line0 + c].split()[2]
            c = c + 1
            e11[ii,jj] = float(e11pre)
    
    f.close()    
    
    # here we average all 8 integration points in each element cell
    e11cond = np.flipud(np.mean(e11, axis=1))
    # element 4630 is at the centroid of a 21x21x21 dataset
    #print e11cond[4630]

    # here we reshape the data from a 9261 length vector to a 21x21x21 3D matrix
    pre_e11mat = np.reshape(e11cond, [21,21,21])
    e11mat = np.swapaxes(pre_e11mat,1,2)

    # here we generate an image and scalebar for a particular slice of the 3D matrix
    if __name__ == '__main__':
        plt.clf()        
        plt.imshow(e11mat[slc,:,:], origin='lower', interpolation='none',
                   cmap='jet')
        plt.colorbar()
    else:
        return e11mat


def WP(msg,filename):
    """
    Summary:
        This function takes an input message and a filename, and appends that
        message to the file. This function also prints the message
    Inputs:
        msg (string): the message to write and print.
        filename (string): the full name of the file to append to.
    """
    fil = open(filename, 'a')
    print msg
    fil.write(msg)
    fil.write('\n')
    fil.close()

def validate(M_val,specinfc,H,el=21):
    """
    Summary:
        This function takes in a validation microstructure and the results of
        the MKS calibration and predicts the response of that microstructure
        under identical loading conditions to those used in the generation
        of calibration microstructures.
    Input:
        M_val ([el,el,el],complex): the microstructure function in frequency 
        space for the validation microstructure
        specinfc ([el**3,H],complex): the core of the materials knowledge
        generated from the calibration process
        H (int): the total number of local states in the microstructure
        function (including higher order comformations)
        el (int): the number of elements per side of the microstructure cube
    Output:
        mks_R ([el,el,el],float): The MKS prediction of the FEM response for
        a given validation microstructure (M_val)
    
    """        
    ## vectorize the frequency-space microstructure function for the validation
    ## dataset
    lin_M = np.zeros((el**3,H),dtype = 'complex64')
    for h in xrange(H):
        lin_M[:,h] = np.reshape(M_val[:,:,:,h],el**3)
    
    ## find the frequency-space response of the validation microstructure
    ## and convert to the real space
    lin_sum = np.sum(np.conjugate(specinfc) * lin_M, 1)
    mks_F = np.reshape(lin_sum,[21,21,21])
    mks_R = np.fft.ifftn(mks_F).real
    
    return mks_R