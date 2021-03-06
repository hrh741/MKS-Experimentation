# -*- coding: utf-8 -*-
"""
Created on Fri May 23 14:25:50 2014

This script evaluates the success of a given MKS calibration and validation
through metrics like MASE and maximum error as well as plotting strain
fields and histograms.

@author: nhpnp3
"""

import time
import numpy as np
import functions as rr
#import matplotlib.pyplot as plt


def results_all(el, ns, set_id, step, typ, compl, comp_app):

    # specify the file to write messages to
    wrt_file = 'results_all_step%s_%s%s_%s.txt' % (step, ns, set_id, time.strftime("%Y-%m-%d_h%Hm%M"))

    r_mks = np.zeros([ns, 6, el, el, el])
    r_fem = np.zeros([ns, 6, el, el, el])

    for comp in xrange(6):
        ccur = compl[comp]
        r_mks[:, comp, ...] = np.load('%s%s_mks_%s%s_s%s.npy' % (typ, ccur, ns, set_id, step))
        r_fem[:, comp, ...] = np.load('%s%s_fem_%s%s_s%s.npy' % (typ, ccur, ns, set_id, step))

    app_r_fem = np.mean(r_fem[:, comp_app, ...])

    for comp in xrange(6):

        ccur = compl[comp]

        # WRITE HEADER TO FILE
        msg = ''
        rr.WP(msg, wrt_file)
        rr.WP(msg, wrt_file)
        msg = 'Results report for %s%s' % (typ, ccur)
        rr.WP(msg, wrt_file)
        msg = ''
        rr.WP(msg, wrt_file)

        # MEAN ABSOLUTE STRAIN ERROR (MASE)
        avgr_fe_tot = 0
        avgr_mks_tot = 0
        max_diff_all = np.zeros(ns)

        for sn in xrange(ns):
            avgr_fe_indv = np.average(r_fem[sn, comp, ...])
            avgr_mks_indv = np.average(r_fem[sn, comp, ...])

            avgr_fe_tot += avgr_fe_indv
            avgr_mks_tot += avgr_mks_indv
            max_diff_all[sn] = np.amax(abs(r_fem[sn, comp, ...]-r_mks[sn, comp, ...]))

        avgr_fe = avgr_fe_tot/ns
        avgr_mks = avgr_mks_tot/ns

        # DIFFERENCE MEASURES
        mean_diff_meas = np.mean(abs(r_fem[:, comp, ...]-r_mks[:, comp, ...]))/app_r_fem
        mean_max_diff_meas = np.mean(max_diff_all)/app_r_fem
        max_diff_meas_all = np.amax(abs(r_fem[:, comp, ...]-r_mks[:, comp, ...]))/app_r_fem

        msg = 'Mean voxel difference over all microstructures: %s%%' % (mean_diff_meas*100)
        rr.WP(msg, wrt_file)
        msg = 'Average Maximum voxel difference per microstructure: %s%%' % (mean_max_diff_meas*100)
        rr.WP(msg, wrt_file)
        msg = 'Maximum voxel difference in all microstructures: %s%%' % (max_diff_meas_all*100)
        rr.WP(msg, wrt_file)

        # STANDARD STATISTICS
        msg = 'Average, %s%s, FEM: %s' % (typ, ccur, avgr_fe)
        rr.WP(msg, wrt_file)
        msg = 'Average, %s%s, MKS: %s' % (typ, ccur, avgr_mks)
        rr.WP(msg, wrt_file)
        msg = 'Standard deviation, %s%s, FEM: %s' % (typ, ccur, np.std(r_fem[:, comp, ...]))
        rr.WP(msg, wrt_file)
        msg = 'Standard deviation, %s%s, MKS: %s' % (typ, ccur, np.std(r_mks[:, comp, ...]))
        rr.WP(msg, wrt_file)

        r_fem_min = np.mean(np.amin(np.reshape(r_fem[:, comp, ...], [ns, el**3]), axis=1))
        r_mks_min = np.mean(np.amin(np.reshape(r_mks[:, comp, ...], [ns, el**3]), axis=1))

        r_fem_max = np.mean(np.amax(np.reshape(r_fem[:, comp, ...], [ns, el**3]), axis=1))
        r_mks_max = np.mean(np.amax(np.reshape(r_mks[:, comp, ...], [ns, el**3]), axis=1))

        msg = 'Mean minimum, %s%s, FEM: %s' % (typ, ccur, r_fem_min)
        rr.WP(msg, wrt_file)
        msg = 'Mean minimum, %s%s, MKS: %s' % (typ, ccur, r_mks_min)
        rr.WP(msg, wrt_file)
        msg = 'Mean maximum, %s%s, FEM: %s' % (typ, ccur, r_fem_max)
        rr.WP(msg, wrt_file)
        msg = 'Mean maximum, %s%s, MKS: %s' % (typ, ccur, r_mks_max)
        rr.WP(msg, wrt_file)

#        ### VISUALIZATION OF MKS VS. FEM ###
#
#        plt.close('all')
#
#        ## pick a slice perpendicular to the x-direction
#        slc = 11
#        sn = 20
#
#
#        ## find the min and max of both datasets for the slice of interest
#        #(needed to scale both images the same)
#        dmin = np.amin([r_fem[:,:,slc,comp,sn],r_mks[:,:,slc,comp,sn]])
#        dmax = np.amax([r_fem[:,:,slc,comp,sn],r_mks[:,:,slc,comp,sn]])
#
#
#        ## Plot slices of the response
#        plt.figure(num=1,figsize=[12,4])
#
#        plt.subplot(121)
#        ax = plt.imshow(r_mks[:,:,slc,comp,sn], origin='lower', interpolation='none',
#            cmap='jet', vmin=dmin, vmax=dmax)
#        plt.colorbar(ax)
#        plt.title('MKS $\%s_{%s}$ response, slice %s' %(typ,real_comp,slc))
#
#        plt.subplot(122)
#        ax = plt.imshow(r_fem[:,:,slc,comp,sn], origin='lower', interpolation='none',
#            cmap='jet', vmin=dmin, vmax=dmax)
#        plt.colorbar(ax)
#        plt.title('FEM $\%s_{%s}$ response, slice %s' %(typ,real_comp,slc))
#
#        plt.savefig('field_step%s_comp%s_%s%s.png' %(step,comp,ns,set_id))
#
#
#        # Plot a histogram representing the frequency of strain levels with separate
#        # channels for each phase of each type of response.
#        plt.figure(num=2,figsize=[12,5])
#
#        ## find the min and max of both datasets (in full)
#        dmin = np.amin([r_fem[:,:,:,comp,:],r_mks[:,:,:,comp,:]])
#        dmax = np.amax([r_fem[:,:,:,comp,:],r_mks[:,:,:,comp,:]])
#
#        fe = np.reshape(r_fem[:,:,:,comp,:],ns*(el**3))
#        mks = np.reshape(r_mks[:,:,:,comp,:],ns*(el**3))
#
#
#        # select the desired number of bins in the histogram
#        bn = 40
#        weight = np.ones_like(fe)/(el**3)
#
#        # FEM histogram
#        n, bins, patches = plt.hist(fe, bins = bn, histtype = 'step', hold = True,
#                                    range = (dmin, dmax), weights=weight, color = 'white')
#        bincenters = 0.5*(bins[1:]+bins[:-1])
#        fe, = plt.plot(bincenters,n,'k', linestyle = '-', lw = 0.5)
#
#        # 1st order terms MKS histogram
#        n, bins, patches = plt.hist(mks, bins = bn, histtype = 'step', hold = True,
#                                    range = (dmin, dmax), weights=weight, color = 'white')
#        mks, = plt.plot(bincenters,n,'b', linestyle = '-', lw = 0.5)
#
#        plt.grid(True)
#
#        plt.legend([fe, mks], ["FEM response", "MKS predicted response"])
#
#        plt.xlabel("$\%s_{%s}$" %(typ,real_comp))
#        plt.ylabel("Number Fraction")
#        plt.title("Frequency comparison of MKS and FEM $\%s_{%s}$ strain responses" %(typ,real_comp))
#
#        plt.savefig('hist_step%s_comp%s_%s%s.png' %(step,comp,ns,set_id))

if __name__ == '__main__':
    results_all(50, 'val', 'sigma')
