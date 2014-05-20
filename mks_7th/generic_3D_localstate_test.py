# -*- coding: utf-8 -*-
"""
Created on Mon Apr 07 15:19:39 2014

Generate microstructure function for generic order terms

@author: nhpnp3
"""

import numpy as np
import itertools as it

## MICROSTRUCTURE GENERATION ##
el = 3
ns = 2
order = 7

micr = np.round(np.random.rand(el, el, el, ns))

## BASELINE MICROSTRUCTURE FUNCTION GENERATION ##

pm = np.zeros([el,el,el,ns,2])
pm[:,:,:,:,0] = (micr == 0)
pm[:,:,:,:,1] = (micr == 1)
pm = pm.astype(int)

hs = np.array(list(it.product([0,1], repeat=order)))
print hs

vec = np.array([[1,0],[1,1],[1,2],[-1,0],[-1,1],[-1,2]])
veclen = len(vec[:,0])
print veclen

comb = np.array(list(it.combinations(xrange(veclen), order-1)))
print comb

LS = len(hs[:,0]) * len(comb[:,0])
H = len(hs[:,0])

#print vec[comb[co_i,:],:]

c = 0;
m = np.zeros([el,el,el,ns,H])

for hh in xrange(H):
    
    a1 = pm[:,:,:,:,hs[hh,0]]    
    pre_m = a1
    
    for t in xrange(len(comb[:,0])):
        
        a_n = np.roll(pm[:,:,:,:,hs[hh,t+1]],vec[comb[t,:],0],vec[comb[t,:],1])
        pre_m = pre_m * a_n
    
    m[:,:,:,:,c] = pre_m
    c = c + 1

m = m.astype(int)


## VALIDATION ##

# for each index in the microstructure function we output the arrangement
# of local states we are looking for and the locations of those local states
# in the slice
for k in xrange(H):
    print k
    print '\nlocal state and confirmation on middle slice'
    print hs[k,:]
    print m[:,:,:,0,k]
    print '\nmicrostructure'    
    print pm[:,:,:,0,1]
    print '\n\n'

print '\ncheck that every location is associated with a specific local state\n' 
print np.sum(m[:,:,:,0,:],axis = 3)