import time


def const():

    C = {}

    """general constants"""
    C['path'] = '/gpfs/scratch1/3/nhpnp3/4_28_neig'
    C['wrt_file'] = 'log_%s.txt' % (time.strftime("%Y-%m-%d_h%H"))

    C['names_cal'] = ['actual', 'basaltrans', 'dice',
                      'innerdonut', 'outerdonut', 'random',
                      'trans']
    C['set_id_cal'] = [s + '_cal' for s in C['names_cal']]
    C['strt_cal'] = [0, 0, 0, 0, 0, 0, 0]
    C['ns_cal'] = [30, 30, 30, 30, 30, 30, 30]
    C['dir_cal'] = C['names_cal']

    C['names_val'] = ['actual', 'basaltrans', 'dice', 'doubledonut',
                      'innerdonut', 'outerdonut', 'random',
                      'trans']
    C['set_id_val'] = [s + '_val' for s in C['names_val']]
    C['strt_val'] = [30, 30, 30, 30, 30, 30, 30, 30]
    C['ns_val'] = [30, 30, 30, 30, 30, 30, 30, 30]
    C['dir_val'] = C['names_val']

    C['dir_resp'] = "response"

    C['H'] = 9
    C['el'] = 21
    C['n_pc_tot'] = 20

    return C
