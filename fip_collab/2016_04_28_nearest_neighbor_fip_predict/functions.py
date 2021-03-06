# -*- coding: utf-8 -*-
"""
Functions connected to 3D, isotropic MKS analyses

In general these functions are not for parallel processing or chunking of data

Noah Paulson, 5/28/2014
"""

import numpy as np
import itertools as it
import vtk
import time


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


def read_vtk_tensor(filename, tensor_id, comp):
    """
    Summary:
        Much of this code was taken from Matthew Priddy's example
        file.
    Inputs:
    Outputs:
    """

    # Initialize the reading of the VTK microstructure created by Dream3D
    reader = vtk.vtkDataSetReader()
    reader.SetFileName(filename)
    reader.ReadAllTensorsOn()
    reader.ReadAllVectorsOn()
    reader.ReadAllScalarsOn()
    reader.Update()
    data = reader.GetOutput()
    dim = data.GetDimensions()
    vec = list(dim)
    vec = [i-1 for i in dim]

    el = vec[0]

    # if tensor_id == 0:
    #     # if meas == 0, we read the stress tensor
    #     meas = data.GetCellData().GetArray(reader.GetTensorsNameInFile(0))
    # elif tensor_id == 1:
    #     # if meas == 1, we read the strain tensor
    #     meas = data.GetCellData().GetArray(reader.GetTensorsNameInFile(1))
    # elif tensor_id == 2:
    #     # if meas == 2, we read the plastic strain tensor
    #     meas = data.GetCellData().GetArray(reader.GetTensorsNameInFile(2))

    # if meas == 0, we read the stress tensor
    # if meas == 1, we read the strain tensor
    # if meas == 2, we read the plastic strain tensor
    meas = data.GetCellData().GetArray(reader.GetTensorsNameInFile(tensor_id))

    meas_py = np.zeros([el**3])

    for ii in xrange(el**3):
        meas_py[ii] = meas.GetValue(ii*9 + comp)

    return meas_py


def read_vtk_scalar(filename):
    """
    Summary:
        Much of this code was taken from Matthew Priddy's example
        file.
    Inputs:
    Outputs:
    """

    # Initialize the reading of the VTK microstructure created by Dream3D
    reader = vtk.vtkDataSetReader()
    reader.SetFileName(filename)
    reader.ReadAllTensorsOn()
    reader.ReadAllVectorsOn()
    reader.ReadAllScalarsOn()
    reader.Update()
    data = reader.GetOutput()
    dim = data.GetDimensions()
    vec = list(dim)
    vec = [i-1 for i in dim]

    el = vec[0]

    # Calculate the total number of elements
    el_total = el**3

    # print reader.GetScalarsNameInFile

    Scalar = data.GetCellData().GetArray(reader.GetScalarsNameInFile(1))

    scalar_py = np.zeros([el_total])

    for ii in xrange(el_total):
        scalar_py[ii] = Scalar.GetValue(ii)

    return scalar_py


def read_vtk_vector(filename):
    """
    Summary:
        Much of this code was taken from Matthew Priddy's example
        file.
    Inputs:
    Outputs:
    """

    # Initialize the reading of the VTK microstructure created by Dream3D
    reader = vtk.vtkDataSetReader()
    reader.SetFileName(filename)
    reader.ReadAllTensorsOn()
    reader.ReadAllVectorsOn()
    reader.ReadAllScalarsOn()
    reader.Update()
    data = reader.GetOutput()
    dim = data.GetDimensions()
    vec = list(dim)
    vec = [i-1 for i in dim]

    el = vec[0]

    Euler = data.GetCellData().GetArray(reader.GetVectorsNameInFile(0))

    euler_py = np.zeros([3, el**3])

    for ii in xrange(el**3):
        euler_py[0, ii] = Euler.GetValue(ii*3 + 0)
        euler_py[1, ii] = Euler.GetValue(ii*3 + 1)
        euler_py[2, ii] = Euler.GetValue(ii*3 + 2)

    return euler_py


def VTK_Header(fileName, file_input, nx_pt, ny_pt, nz_pt, X, Y, Z, no_el):

    fileName.write("# vtk DataFile Version 2.0" "\n")

    fileName.write("data file: " + file_input +
                   " generated by Noah H. Paulson on " +
                   str(time.strftime("%c")) + "\n")

    fileName.write("ASCII" + "\n")
    fileName.write("DATASET RECTILINEAR_GRID" + "\n")
    fileName.write("DIMENSIONS " + str(nx_pt) + " " + str(ny_pt) + " " +
                   str(nz_pt) + "\n")
    fileName.write("X_COORDINATES " + str(nx_pt) + " float" "\n")
    for i in range(len(X)):
        fileName.write("% 2.4f " % (X[i]))
        if i == len(X):
            fileName.write("\n")
    fileName.write("\n")
    fileName.write("Y_COORDINATES " + str(ny_pt) + " float" "\n")
    for i in range(len(Y)):
        fileName.write("% 2.4f " % (Y[i]))
        if i == len(Y):
            fileName.write("\n")
    fileName.write("\n")
    fileName.write("Z_COORDINATES " + str(nz_pt) + " float" "\n")
    for i in range(len(Z)):
        fileName.write("% 2.4f " % (Z[i]))
        if i == len(Z):
            fileName.write("\n")
    fileName.write("\n")

    fileName.write("CELL_DATA " + str(no_el) + "\n")


def VTK_Vector(fileName, dataName, data, no_per_line):
    fileName.write("VECTORS " + dataName + " float " + "\n")

    for ii in range(np.size(data, 0)):
        fileName.write(" % +2.6E % +2.6E % +2.6E    " % (data[ii, 0],
                                                         data[ii, 1],
                                                         data[ii, 2]))
        ii += 1
        if ii % no_per_line == 0:
            fileName.write("\n")
        elif ii == np.size(data, 1):
            fileName.write("\n")


def regress(x_cal, x_val, y_cal, y_val, n_pc, n_poly):

    """calculate the indices for the regression bases"""

    xmax = n_pc*n_poly
    xmat = np.unravel_index(np.arange(xmax), (n_pc, n_poly))
    xmat = np.array(xmat).T
    remove = (xmat[:, 0] != 0)*(xmat[:, 1] == 0)
    keep = np.ones(remove.shape, dtype='bool') - remove
    xmat = xmat[keep, :]
    xmax = xmat.shape[0]

    """calculate the X matrix for calibration"""

    n_samp = x_cal.shape[0]

    X_cal = np.zeros((n_samp, xmax), dtype='float64')

    for xx in xrange(xmax):
        pc, deg = xmat[xx, :]

        # print pc, deg

        X_cal[:, xx] = x_cal[:, pc]**deg

    """calculate the X matrix for validation"""

    n_samp = x_val.shape[0]

    X_val = np.zeros((n_samp, xmax), dtype='float64')

    for xx in xrange(xmax):
        pc, deg = xmat[xx, :]

        X_val[:, xx] = x_val[:, pc]**deg

    """calculate the XhX matrix"""

    XhX = np.zeros((xmax, xmax), dtype='float64')

    tmp = it.combinations_with_replacement(np.arange(xmax), 2)
    Imat = np.array(list(tmp))
    ImatL = Imat.shape[0]

    # print Imat

    for I in xrange(ImatL):

        ii, jj = Imat[I, :]

        dotvec = np.dot(X_cal[:, ii], X_cal[:, jj])

        if ii == jj:
            XhX[ii, ii] = dotvec
        else:
            XhX[ii, jj] = dotvec
            XhX[jj, ii] = dotvec

    # if (n_pc == 1)*(n_poly == 5):

    #     print XhX.min()
    #     print XhX.mean()
    #     print XhX.max()

    #     import matplotlib.pyplot as plt

    #     ax = plt.imshow(XhX, origin='lower',
    #                     interpolation='none', cmap='viridis')
    #     plt.colorbar(ax)
    #     plt.show()

    print "shape(XhX): %s" % str(XhX.shape)

    if np.linalg.matrix_rank(XhX) != xmax:
        print "WARNING: XhX is rank deficient"

    """calculate XhY"""

    XhY = np.zeros(xmax, dtype='float64')

    for ii in xrange(xmax):
        XhY[ii] = np.dot(X_cal[:, ii], y_cal)

    """perform the regression"""

    # coef = np.linalg.solve(XhX, XhY)
    coef = np.linalg.lstsq(XhX, XhY)[0]

    """cross-validate with the validation data"""

    y_val_predict = np.dot(coef, X_val.T)

    err = np.abs(y_val-y_val_predict)
    err_mean = err.mean()
    err_max = err.max()

    print "mean error: %s" % err_mean
    print "max error: %s" % err_max

    print "y min: %s" % y_val.min()
    print "y_predict min: %s" % y_val_predict.min()
    print "y mean: %s" % y_val.mean()
    print "y_predict mean: %s" % y_val_predict.mean()
    print "y max: %s" % y_val.max()
    print "y_predict max: %s" % y_val_predict.max()

    return err_mean, err_max, coef, y_val_predict


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
