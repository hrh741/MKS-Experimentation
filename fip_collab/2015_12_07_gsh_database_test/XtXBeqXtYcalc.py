import numpy as np
import h5py


def independent_columns(A, tol=1e-05):
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


def WP(msg, filename):
    """
    Summary:
        This function takes an input message and a filename, and appends that
        message to the file. This function also prints the message
    Inputs:
        msg (string): the message to write and print.
        filename (string): the full name of the file to append to.
    Outputs:
        both prints the message and writes the message to the specified file
    """
    fil = open(filename, 'a')
    print msg
    fil.write(msg)
    fil.write('\n')
    fil.close()

filename = 'log_XtXBeqXtYcalc.txt'

f = h5py.File('XtXtotal.hdf5', 'r')
XtX = f.get('XtX')[...]
f.close()

msg = "rank(XtX): %s" % np.linalg.matrix_rank(XtX)
WP(msg, filename)

ind_vec = independent_columns(XtX)
msg = "independent columns of X: %s" % str(ind_vec)
WP(msg, filename)

f = h5py.File('XtYtotal.hdf5', 'r')
XtY = f.get('XtY')[...]
f.close()

# XtX_plus: the psudeo-inverse of XtX
XtX_plus = np.linalg.pinv(XtX)
# coeff: vector of least squares coefficients for the selected basis functions.
# This is calculated with the pseudo-inverse above
coeff = np.dot(XtX_plus, XtY)

f = h5py.File('reg_coeff.hdf5', 'w')
f.create_dataset('coeff', data=coeff)
f.close()
