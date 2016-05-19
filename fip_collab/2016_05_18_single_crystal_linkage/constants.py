import time


def const():

    C = {}

    """general constants"""
    C['wrt_file'] = 'log_%s.txt' % (time.strftime("%Y-%m-%d_h%H"))

    C['names_cal'] = ['single']
    C['set_id_cal'] = [s + '_cal' for s in C['names_cal']]
    # C['strt_cal'] = [0]
    C['ns_cal'] = [576]
    C['dir_cal'] = C['names_cal']

    C['names_val'] = ['single']
    C['set_id_val'] = [s + '_val' for s in C['names_val']]
    # C['strt_val'] = [30]
    C['ns_val'] = [250]
    C['dir_val'] = C['names_val']

    C['dir_resp'] = "response"

    C['H'] = 23
    C['el'] = 3
    C['n_pc_tot'] = 30

    return C
