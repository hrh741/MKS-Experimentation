# -*- coding: utf-8 -*-
"""
Created on Mon Dec 15 09:32:40 2014

@author: nhpnp3
"""

import numpy as np


def gsh_hcp_tri_L_7(e_angles):
    
    
    phi1 = e_angles[0,:]
    phi = e_angles[1,:]    
    phi2 = e_angles[2,:] 
        
    zvec = np.abs(phi) < 10e-17
    zvec = zvec.astype(int)   
    randvec = np.round(np.random.rand(zvec.shape[0]))    
    randvecopp = np.ones(zvec.shape[0]) - randvec
    phi += (1e-7)*zvec*(randvec - randvecopp)
 
    t2 = np.exp((-2j) * phi1)
    t3 = np.sqrt(0.6e1)
    t5 = np.cos(phi)
    t6 = 0.1e1 - t5
    t7 = 0.1e1 + t5
    t8 = t6 * t7
    t12 = np.exp((-1j) * phi1)
    t15 = np.sqrt(t6)
    t16 = 0.1e1 / t15
    t17 = np.sqrt(t7)
    t18 = t16 * t17
    t19 = t6 ** 2
    t23 = t7 ** 2
    t27 = np.exp((1j) * phi1)
    t30 = 0.1e1 / t17
    t31 = t15 * t30
    t36 = np.exp((2j) * phi1)
    t41 = np.exp((-4j) * phi1)
    t42 = np.sqrt(0.70e2)
    t44 = t19 * t23
    t48 = np.exp((-3j) * phi1)
    t50 = np.sqrt(0.35e2)
    t52 = t15 * t6
    t53 = 0.1e1 / t52
    t54 = t17 * t7
    t55 = t53 * t54
    t56 = t19 * t6
    t57 = t56 * t7
    t58 = t19 ** 2
    t62 = np.sqrt(0.10e2)
    t64 = 0.1e1 / t6
    t65 = t64 * t7
    t66 = 0.360e3 * t44
    t74 = np.sqrt(0.5e1)
    t76 = t23 * t7
    t77 = t6 * t76
    t79 = 0.720e3 * t44
    t85 = t23 ** 2
    t99 = 0.1e1 / t7
    t100 = t6 * t99
    t108 = np.exp((3j) * phi1)
    t111 = 0.1e1 / t54
    t112 = t52 * t111
    t117 = np.exp((4j) * phi1)
    t122 = np.exp((-6j) * phi1)
    t123 = np.sqrt(0.231e3)
    t125 = t56 * t76
    t129 = np.exp((-6j) * phi2)
    t130 = t129 * t122
    t131 = t85 * t23
    t132 = np.sqrt(0.2e1)
    t133 = t131 * t132
    t136 = np.exp((6j) * phi2)
    t137 = t136 * t122
    t138 = t58 * t19
    t139 = t138 * t132
    t143 = np.exp((-5j) * phi1)
    t145 = np.sqrt(0.77e2)
    t147 = t15 * t19
    t148 = 0.1e1 / t147
    t149 = t17 * t23
    t151 = t58 * t6
    t152 = t151 * t7
    t156 = ((-0.1e1 / 0.64e2)*1j) * t129
    t158 = np.sqrt(0.3e1)
    t160 = t85 * t7
    t161 = t17 * t160
    t163 = t158 * t15 * t161 * t132
    t165 = ((0.1e1 / 0.64e2)*1j) * t136
    t167 = t15 * t151
    t169 = t17 * t132
    t170 = t158 * t167 * t169
    t173 = np.sqrt(0.14e2)
    t175 = 0.1e1 / t19
    t177 = t58 * t23
    t185 = t129 * t41
    t186 = np.sqrt(0.66e2)
    t188 = t6 * t160
    t189 = t188 * t132
    t191 = t136 * t41
    t193 = t152 * t132
    t197 = np.sqrt(0.105e3)
    t199 = 0.60480e5 * t125
    t206 = ((0.1e1 / 0.64e2)*1j) * t129
    t208 = np.sqrt(0.55e2)
    t210 = t17 * t85
    t212 = t208 * t52 * t210 * t132
    t214 = ((-0.1e1 / 0.64e2)*1j) * t136
    t216 = t15 * t58
    t219 = t208 * t216 * t54 * t132
    t223 = t19 * t85
    t225 = 0.161280e6 * t125
    t233 = t129 * t2
    t235 = t223 * t132
    t237 = t136 * t2
    t239 = t177 * t132
    t243 = np.sqrt(0.42e2)
    t247 = 0.252000e6 * t125
    t256 = np.sqrt(0.22e2)
    t258 = t17 * t76
    t260 = t256 * t147 * t258 * t132
    t264 = t15 * t56
    t267 = t256 * t264 * t149 * t132
    t279 = t125 * t132
    t310 = t129 * t36
    t313 = t136 * t36
    t331 = 0.1e1 / t23
    t340 = t129 * t117
    t343 = t136 * t117
    t348 = np.exp((5j) * phi1)
    t351 = 0.1e1 / t149
    t362 = np.exp((6j) * phi1)
    t366 = t129 * t362
    t368 = t136 * t362
    t373 = np.exp((-7j) * phi1)
    t376 = t17 * t131
    t381 = ((-0.1e1 / 0.256e3)*1j) * t136
    t383 = t15 * t138
    t388 = 0.87178291200e11 * t5
    t395 = t58 ** 2
    t397 = t7 * t395 * t58
    t406 = ((0.1e1 / 0.3188234649600e13)*1j) * t129
    t407 = np.sqrt(0.26e2)
    t408 = t143 * t407
    t415 = ((-0.1e1 / 0.512e3)*1j) * t136
    t420 = t23 * t395 * t56
    t438 = t76 * t395 * t19
    t447 = ((-0.1e1 / 0.3188234649600e13)*1j) * t129
    t448 = np.sqrt(0.286e3)
    t449 = t48 * t448
    t456 = ((0.1e1 / 0.512e3)*1j) * t136
    t461 = t85 * t395 * t6
    t469 = np.sqrt(0.143e3)
    t479 = t160 * t395
    t488 = np.sqrt(0.858e3)
    t489 = t12 * t488
    t500 = t131 * t58 * t56
    t508 = np.sqrt(0.3003e4)
    t520 = t85 * t76 * t138
    t527 = t27 * t488
    t537 = t85 ** 2
    t538 = t537 * t151
    t556 = t537 * t7 * t58
    t565 = t108 * t448
    t576 = t537 * t23 * t56
    t594 = t537 * t76 * t19
    t603 = t348 * t407
    t614 = t537 * t85 * t6
    t638 = np.exp((7j) * phi1)
   
    out_tvalues = np.zeros([56,e_angles.shape[1]], dtype = 'complex128')    
 
    out_tvalues[0,:] = 1
    out_tvalues[1,:] = -(t2 * t3 * t8 / 4)
    out_tvalues[2,:] = (((-0.1e1 / 0.4e1)*1j) * t12 * t3 * t18 * (t8 - t19))
    out_tvalues[3,:] = (t23 / 0.4e1 - t8 + t19 / 0.4e1)
    out_tvalues[4,:] = (((0.1e1 / 0.4e1)*1j) * t27 * t3 * t31 * (-t23 + t8))
    out_tvalues[5,:] = -(t36 * t3 * t8 / 4)
    out_tvalues[6,:] = (t41 * t42 * t44 / 16)
    out_tvalues[7,:] = (((0.1e1 / 0.8e1)*1j) * t48 * t50 * t55 * (t57 - t58))
    out_tvalues[8,:] = -(t2 * t62 * t65 * (t66 - 0.960e3 * t57 + 0.360e3 * t58) / 1920)
    out_tvalues[9,:] = (((-0.1e1 / 0.960e3)*1j) * t12 * t74 * t18 * (0.120e3 * t77 - t79 + 0.720e3 * t57 - 0.120e3 * t58))
    out_tvalues[10,:] = (t85 / 0.16e2 - t77 + 0.9e1 / 0.4e1 * t44 - t57 + t58 / 0.16e2)
    out_tvalues[11,:] = (((0.1e1 / 0.960e3)*1j) * t27 * t74 * t31 * (-0.120e3 * t85 + 0.720e3 * t77 - t79 + 0.120e3 * t57))
    out_tvalues[12,:] = -(t36 * t62 * t100 * (0.360e3 * t85 - 0.960e3 * t77 + t66) / 1920)
    out_tvalues[13,:] = (((-0.1e1 / 0.8e1)*1j) * t108 * t50 * t112 * (-t85 + t77))
    out_tvalues[14,:] = (t117 * t42 * t44 / 16)
    out_tvalues[15,:] = -(t122 * t123 * t125 / 32)
    out_tvalues[16,:] = (t130 * t133 / 128 + t137 * t139 / 128)
    out_tvalues[17,:] = (((-0.3e1 / 0.32e2)*1j) * t143 * t145 * t148 * t149 * (t152 - t138))
    out_tvalues[18,:] = (t156 * t143 * t163 + t165 * t143 * t170)
    out_tvalues[19,:] = (t41 * t173 * t175 * t23 * (0.151200e6 * t177 - 0.362880e6 * t152 + 0.151200e6 * t138) / 645120)
    out_tvalues[20,:] = (-t185 * t186 * t189 / 128 - t191 * t186 * t193 / 128)
    out_tvalues[21,:] = (((0.1e1 / 0.967680e6)*1j) * t48 * t197 * t55 * (t199 - 0.272160e6 * t177 + 0.272160e6 * t152 - 0.60480e5 * t138))
    out_tvalues[22,:] = (t206 * t48 * t212 + t214 * t48 * t219)
    out_tvalues[23,:] = -(t2 * t197 * t65 * (0.20160e5 * t223 - t225 + 0.302400e6 * t177 - 0.161280e6 * t152 + 0.20160e5 * t138) / 645120)
    out_tvalues[24,:] = ((0.3e1 / 0.128e3) * t233 * t208 * t235 + (0.3e1 / 0.128e3) * t237 * t208 * t239)
    out_tvalues[25,:] = (((-0.1e1 / 0.322560e6)*1j) * t12 * t243 * t18 * (0.5040e4 * t188 - 0.75600e5 * t223 + t247 - 0.252000e6 * t177 + 0.75600e5 * t152 - 0.5040e4 * t138))
    out_tvalues[26,:] = (((-0.3e1 / 0.64e2)*1j) * t129 * t12 * t260 + ((0.3e1 / 0.64e2)*1j) * t136 * t12 * t267)
    out_tvalues[27,:] = (t131 / 0.64e2 - 0.9e1 / 0.16e2 * t188 + 0.225e3 / 0.64e2 * t223 - 0.25e2 / 0.4e1 * t125 + 0.225e3 / 0.64e2 * t177 - 0.9e1 / 0.16e2 * t152 + t138 / 0.64e2)
    out_tvalues[28,:] = (-t129 * t123 * t279 / 64 - t136 * t123 * t279 / 64)
    out_tvalues[29,:] = (((0.1e1 / 0.322560e6)*1j) * t27 * t243 * t31 * (-0.5040e4 * t131 + 0.75600e5 * t188 - 0.252000e6 * t223 + t247 - 0.75600e5 * t177 + 0.5040e4 * t152))
    out_tvalues[30,:] = (((0.3e1 / 0.64e2)*1j) * t129 * t27 * t267 + ((-0.3e1 / 0.64e2)*1j) * t136 * t27 * t260)
    out_tvalues[31,:] = -(t36 * t197 * t100 * (0.20160e5 * t131 - 0.161280e6 * t188 + 0.302400e6 * t223 - t225 + 0.20160e5 * t177) / 645120)
    out_tvalues[32,:] = ((0.3e1 / 0.128e3) * t310 * t208 * t239 + (0.3e1 / 0.128e3) * t313 * t208 * t235)
    out_tvalues[33,:] = (((-0.1e1 / 0.967680e6)*1j) * t108 * t197 * t112 * (-0.60480e5 * t131 + 0.272160e6 * t188 - 0.272160e6 * t223 + t199))
    out_tvalues[34,:] = (t156 * t108 * t219 + t165 * t108 * t212)
    out_tvalues[35,:] = (t117 * t173 * t19 * t331 * (0.151200e6 * t131 - 0.362880e6 * t188 + 0.151200e6 * t223) / 645120)
    out_tvalues[36,:] = (-t340 * t186 * t193 / 128 - t343 * t186 * t189 / 128)
    out_tvalues[37,:] = (((0.3e1 / 0.32e2)*1j) * t348 * t145 * t147 * t351 * (-t131 + t188))
    out_tvalues[38,:] = (t206 * t348 * t170 + t214 * t348 * t163)
    out_tvalues[39,:] = -(t362 * t123 * t125 / 32)
    out_tvalues[40,:] = (t366 * t139 / 128 + t368 * t133 / 128)
    out_tvalues[41,:] = (((0.1e1 / 0.256e3)*1j) * t129 * t373 * t173 * t16 * t376 * t6 * t132 + t381 * t373 * t173 * t383 * t169)
    out_tvalues[42,:] = (t130 * t131 * (-t388 + 0.74724249600e11) * t132 / 1594117324800 - t137 / t138 * (-0.13e2 * t397 + t395 * t151) * t132 / 256)
    out_tvalues[43,:] = (t406 * t408 * t15 * t161 * (-0.62270208000e11 + t388) * t132 + t415 * t408 / t167 * t30 * (-0.12e2 * t420 + 0.2e1 * t397) * t132)
    out_tvalues[44,:] = (-t185 * t407 * t188 * (0.49816166400e11 - t388) * t132 / 1594117324800 + t191 * t407 / t151 * t99 * (-0.11e2 * t438 + 0.3e1 * t420) * t132 / 256)
    out_tvalues[45,:] = (t447 * t449 * t52 * t210 * (-0.37362124800e11 + t388) * t132 + t456 * t449 / t216 * t111 * (-0.10e2 * t461 + 0.4e1 * t438) * t132)
    out_tvalues[46,:] = (t233 * t469 * t223 * (0.24908083200e11 - t388) * t132 / 1594117324800 - t237 * t469 / t58 * t331 * (-0.9e1 * t479 + 0.5e1 * t461) * t132 / 256)
    out_tvalues[47,:] = (t406 * t489 * t147 * t258 * (-0.12454041600e11 + t388) * t132 + t415 * t489 / t264 * t351 * (-0.8e1 * t500 + 0.6e1 * t479) * t132)
    out_tvalues[48,:] = (t129 * t508 * t76 * t56 * t5 * t132 / 64 + t136 * t508 / t56 / t76 * (-t520 + t500) * t132 / 128)
    out_tvalues[49,:] = (t447 * t527 * t264 * t149 * (0.12454041600e11 + t388) * t132 + t456 * t527 * t148 / t258 * (-0.6e1 * t538 + 0.8e1 * t520) * t132)
    out_tvalues[50,:] = (t310 * t469 * t177 * (-0.24908083200e11 - t388) * t132 / 1594117324800 - t313 * t469 * t175 / t85 * (-0.5e1 * t556 + 0.9e1 * t538) * t132 / 256)
    out_tvalues[51,:] = (t406 * t565 * t216 * t54 * (0.37362124800e11 + t388) * t132 + t415 * t565 * t53 / t210 * (-0.4e1 * t576 + 0.10e2 * t556) * t132)
    out_tvalues[52,:] = (-t340 * t407 * t152 * (-0.49816166400e11 - t388) * t132 / 1594117324800 + t343 * t407 * t64 / t160 * (-0.3e1 * t594 + 0.11e2 * t576) * t132 / 256)
    out_tvalues[53,:] = (t447 * t603 * t167 * t17 * (0.62270208000e11 + t388) * t132 + t456 * t603 * t16 / t161 * (-0.2e1 * t614 + 0.12e2 * t594) * t132)
    out_tvalues[54,:] = (t366 * t138 * (-0.74724249600e11 - t388) * t132 / 1594117324800 - t368 / t131 * (-t537 * t160 + 0.13e2 * t614) * t132 / 256)
    out_tvalues[55,:] = (((0.1e1 / 0.256e3)*1j) * t129 * t638 * t173 * t383 * t30 * t7 * t132 + t381 * t638 * t173 * t376 * t15 * t132)

    return out_tvalues


def gsh_hcp_tri_L_4(e_angles):   
    
    phi1 = e_angles[0,:]
    phi = e_angles[1,:]    
        
    zvec = np.abs(phi) < 10e-17
    zvec = zvec.astype(int)   
    randvec = np.round(np.random.rand(zvec.shape[0]))    
    randvecopp = np.ones(zvec.shape[0]) - randvec
    phi += (1e-7)*zvec*(randvec - randvecopp)
     
    t2 = np.exp((-2j) * phi1)
    t3 = np.sqrt(0.6e1)
    t5 = np.cos(phi)
    t6 = 0.1e1 - t5
    t7 = 0.1e1 + t5
    t8 = t6 * t7
    t12 = np.exp((-1j) * phi1)
    t15 = np.sqrt(t6)
    t16 = 0.1e1 / t15
    t17 = np.sqrt(t7)
    t18 = t16 * t17
    t19 = t6 ** 2
    t23 = t7 ** 2
    t27 = np.exp((1j) * phi1)
    t30 = 0.1e1 / t17
    t31 = t15 * t30
    t36 = np.exp((2j) * phi1)
    t41 = np.exp((-4j) * phi1)
    t42 = np.sqrt(0.70e2)
    t44 = t19 * t23
    t48 = np.exp((-3j) * phi1)
    t50 = np.sqrt(0.35e2)
    t52 = t15 * t6
    t53 = 0.1e1 / t52
    t54 = t17 * t7
    t55 = t53 * t54
    t56 = t19 * t6
    t57 = t56 * t7
    t58 = t19 ** 2
    t62 = np.sqrt(0.10e2)
    t64 = 0.1e1 / t6
    t65 = t64 * t7
    t66 = 0.360e3 * t44
    t74 = np.sqrt(0.5e1)
    t76 = t23 * t7
    t77 = t6 * t76
    t79 = 0.720e3 * t44
    t85 = t23 ** 2
    t99 = 0.1e1 / t7
    t100 = t6 * t99
    t108 = np.exp((3j) * phi1)
    t111 = 0.1e1 / t54
    t112 = t52 * t111
    t117 = np.exp((4j) * phi1)
        
    out_tvalues = np.zeros([15,e_angles.shape[1]], dtype = 'complex128')    
        
    out_tvalues[0,:] = 1
    out_tvalues[1,:] = -(t2 * t3 * t8 / 4)
    out_tvalues[2,:] = (((-0.1e1 / 0.4e1)*1j) * t12 * t3 * t18 * (t8 - t19))
    out_tvalues[3,:] = (t23 / 0.4e1 - t8 + t19 / 0.4e1)
    out_tvalues[4,:] = (((0.1e1 / 0.4e1)*1j) * t27 * t3 * t31 * (-t23 + t8))
    out_tvalues[5,:] = -(t36 * t3 * t8 / 4)
    out_tvalues[6,:] = (t41 * t42 * t44 / 16)
    out_tvalues[7,:] = (((0.1e1 / 0.8e1)*1j) * t48 * t50 * t55 * (t57 - t58))
    out_tvalues[8,:] = -(t2 * t62 * t65 * (t66 - 0.960e3 * t57 + 0.360e3 * t58) / 1920)
    out_tvalues[9,:] = (((-0.1e1 / 0.960e3)*1j) * t12 * t74 * t18 * (0.120e3 * t77 - t79 + 0.720e3 * t57 - 0.120e3 * t58))
    out_tvalues[10,:] = (t85 / 0.16e2 - t77 + 0.9e1 / 0.4e1 * t44 - t57 + t58 / 0.16e2)
    out_tvalues[11,:] = (((0.1e1 / 0.960e3)*1j) * t27 * t74 * t31 * (-0.120e3 * t85 + 0.720e3 * t77 - t79 + 0.120e3 * t57))
    out_tvalues[12,:] = -(t36 * t62 * t100 * (0.360e3 * t85 - 0.960e3 * t77 + t66) / 1920)
    out_tvalues[13,:] = (((-0.1e1 / 0.8e1)*1j) * t108 * t50 * t112 * (-t85 + t77))
    out_tvalues[14,:] = (t117 * t42 * t44 / 16)
    
    return out_tvalues


def GSH_Hexagonal_Triclinic(e_angles):
    
    phi1 = e_angles[0,:]
    phi = e_angles[1,:]
    
    zvec = np.abs(phi) < 10e-17
    zvec = zvec.astype(int)   
    randvec = np.round(np.random.rand(zvec.shape[0]))    
    randvecopp = np.ones(zvec.shape[0]) - randvec
    phi += (1e-7)*zvec*(randvec - randvecopp)
    
    t1 = np.sqrt(0.6e1)
    t3 = np.exp((-2j) * phi1)
    t5 = np.sin(phi)
    t6 = t5 ** 2
    t9 = ((-0.5e1 / 0.2e1)*1j) * t1
    t10 = np.cos(phi)
    t11 = 0.1e1 - t10
    t12 = np.sqrt(t11)
    t14 = 0.1e1 + t10
    t15 = np.sqrt(t14)
    t16 = t15 * t10
    t18 = np.exp((-1j) * phi1)
    t21 = t10 ** 2
    t24 = np.exp((1j) * phi1)
    t29 = np.exp((2j) * phi1)
    t33 = np.sqrt(0.70e2)
    t35 = np.exp((-4j) * phi1)
    t37 = t6 ** 2
    t40 = np.sqrt(0.35e2)
    t44 = t15 * t14
    t47 = np.exp((-3j) * phi1)
    t50 = np.sqrt(0.10e2)
    t52 = 0.7e1 * t21
    t54 = t6 * (-0.1e1 + t52)
    t57 = np.sqrt(0.5e1)
    t66 = t21 ** 2
    t75 = 0.1e1 / t12
    t87 = np.exp((3j) * phi1)
    t93 = np.exp((4j) * phi1)

    Tsym = np.zeros([15,e_angles.shape[1]], dtype = 'complex128')    
    
    Tsym[0,:] = 1
    Tsym[1,:] = -((0.5e1 / 0.4e1) * t1 * t3 * t6)
    Tsym[2,:] = (t9 * t12 * t16 * t18)
    Tsym[3,:] = (-0.5e1 / 0.2e1 + 0.15e2 / 0.2e1 * t21)
    Tsym[4,:] = (t9 * t24 * t16 * t12)
    Tsym[5,:] = -((0.5e1 / 0.4e1) * t1 * t29 * t6)
    Tsym[6,:] = ((0.9e1 / 0.16e2) * t33 * t35 * t37)
    Tsym[7,:] = ((0.9e1 / 0.4e1)*1j) * t40 * t12 * t11 * t44 * t10 * t47
    Tsym[8,:] = -((0.9e1 / 0.8e1) * t50 * t3 * t54)
    Tsym[9,:] = ((-0.9e1 / 0.4e1)*1j) * t57 * t18 * t12 * t15 * t10 * (-0.3e1 + t52)
    Tsym[10,:] = (0.27e2 / 0.8e1 - 0.135e3 / 0.4e1 * t21 + 0.315e3 / 0.8e1 * t66)
    Tsym[11,:] = ((0.9e1 / 0.4e1)*1j) * t57 * t24 * t16 * (0.3e1 - t52 - 0.3e1 * t10 + 0.7e1 * t21 * t10) * t75
    Tsym[12,:] = -((0.9e1 / 0.8e1) * t50 * t29 * t54)
    Tsym[13,:] = ((0.9e1 / 0.4e1)*1j) * t10 * t44 * (0.1e1 + t21 - 0.2e1 * t10) * t87 * t40 * t75
    Tsym[14,:] = ((0.9e1 / 0.16e2) * t33 * t93 * t37)
    
    Tsym=np.conjugate(Tsym)    

    return Tsym


if __name__ == '__main__':
    tvals = GSH_Hexagonal_Triclinic(np.array([[123],[0.0],[3]]))
    print tvals
#    tvals = gsh_hcp_tri_L_7(np.array([[1,100],[2,200],[3,300]]))
#    print tvals
#    import scipy.io as sio
#    sio.savemat('tvals', {'tvals':tvals})
  

    
    