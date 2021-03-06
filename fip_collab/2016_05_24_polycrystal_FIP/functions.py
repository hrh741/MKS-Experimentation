# -*- coding: utf-8 -*-

import numpy as np
import itertools as it
from constants import const
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model
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

    Scalar = data.GetCellData().GetArray(reader.GetScalarsNameInFile(0))

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


def regress(x_cal, x_val, y_cal, y_val, n_pc, n_poly):

    C = const()

    """compute the data matrices with dimensions
    n_samp x n_feat where the features contain all polynomial terms
    up to the specified degree"""
    poly = PolynomialFeatures(degree=(n_poly-1))
    X_cal = poly.fit_transform(x_cal[:, :n_pc])
    X_val = poly.fit_transform(x_val[:, :n_pc])

    """set up the regression model"""
    clf = linear_model.LinearRegression(normalize=False)
    """fit the regression model"""
    clf.fit(X_cal, y_cal)
    coef = clf.coef_

    # if n_pc == 20 and n_poly == 4:
    #     np.savetxt("coef.txt", coef, delimiter=',')
    #     np.savetxt("xmat.txt", xmat, delimiter=',')

    """validate with the calibration data"""
    y_cal_predict = clf.predict(X_cal)

    err = np.abs(y_cal-y_cal_predict)
    meanerr_cal = err.mean()
    maxerr_cal = err.max()

    tmp = str([meanerr_cal, maxerr_cal])
    msg = "y_cal mean and max error: %s" % tmp
    WP(msg, C['wrt_file'])
    tmp = str([y_cal.min(), y_cal.mean(), y_cal.max()])
    msg = "y_cal min mean and max: %s" % tmp
    WP(msg, C['wrt_file'])
    tmp = str([y_cal_predict.min(), y_cal_predict.mean(), y_cal_predict.max()])
    msg = "y_cal_predict min mean and max: %s" % tmp
    WP(msg, C['wrt_file'])

    """cross-validate with the validation data"""
    y_val_predict = clf.predict(X_val)

    err = np.abs(y_val-y_val_predict)
    meanerr_val = err.mean()
    maxerr_val = err.max()

    tmp = str([meanerr_val, maxerr_val])
    msg = "y_val mean and max error: %s" % tmp
    WP(msg, C['wrt_file'])
    tmp = str([y_cal.min(), y_val.mean(), y_val.max()])
    msg = "y_val min mean and max: %s" % tmp
    WP(msg, C['wrt_file'])
    tmp = str([y_val_predict.min(), y_val_predict.mean(), y_val_predict.max()])
    msg = "y_val_predict min mean and max: %s" % tmp
    WP(msg, C['wrt_file'])

    return [y_cal_predict, y_val_predict,
            meanerr_cal, meanerr_val,
            maxerr_cal, maxerr_val,
            coef]


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
