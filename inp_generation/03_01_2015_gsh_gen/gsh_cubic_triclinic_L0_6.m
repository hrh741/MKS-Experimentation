function [out_tvalues]=gsh_cubic_triclinic_L0_6(e_angles)

phi1 = e_angles(1, :);
phi = e_angles(2, :);
phi2 = e_angles(3, :);

zvec = abs(phi) < 10e-17;
randvec = round(rand(size(zvec)));
randvecopp = ones(size(zvec)) - randvec;
phi = phi + (1e-7)*zvec.*(randvec - randvecopp);

out_tvalues = zeros(23, length(phi1));

out_tvalues(1, :) = 1;
out_tvalues(2, :) = exp((-4*i) * phi2) * exp((-4*i) * phi1) * ((0.1e1 + cos(phi)) ^ 4) * sqrt(0.21e2) * sqrt(0.7e1) * sqrt(0.5e1) * sqrt(0.2e1) / 1344 + exp((-4*i) * phi2) * sqrt(0.70e2) * ((0.1e1 + cos(phi)) ^ 2) * ((0.1e1 - cos(phi)) ^ 2) * sqrt(0.21e2) / 96 + exp((-4*i) * phi2) * exp((4*i) * phi1) * ((0.1e1 - cos(phi)) ^ 4) * sqrt(0.21e2) * sqrt(0.7e1) * sqrt(0.5e1) * sqrt(0.2e1) / 1344;
out_tvalues(3, :) = (-0.1e1 / 0.336e3*i) * exp((-3*i) * phi2) * exp((-4*i) * phi1) * sqrt(0.1e1 - cos(phi)) * ((0.1e1 + cos(phi)) ^ (0.7e1 / 0.2e1)) * sqrt(0.21e2) * sqrt(0.7e1) * sqrt(0.5e1) + (0.1e1 / 0.40320e5*i) * exp((-3*i) * phi2) * sqrt(0.35e2) * ((0.1e1 - cos(phi)) ^ (-0.3e1 / 0.2e1)) * ((0.1e1 + cos(phi)) ^ (0.3e1 / 0.2e1)) * (-0.840e3 * (0.1e1 - cos(phi)) ^ 4 + 0.840e3 * (0.1e1 + cos(phi)) * (0.1e1 - cos(phi)) ^ 3) * sqrt(0.21e2) + (0.1e1 / 0.336e3*i) * exp((-3*i) * phi2) * exp((4*i) * phi1) * ((0.1e1 - cos(phi)) ^ (0.7e1 / 0.2e1)) * sqrt(0.1e1 + cos(phi)) * sqrt(0.21e2) * sqrt(0.7e1) * sqrt(0.5e1);
out_tvalues(4, :) = -exp((-2*i) * phi2) * exp((-4*i) * phi1) * ((0.1e1 + cos(phi)) ^ 3) * (0.1e1 - cos(phi)) * sqrt(0.21e2) * sqrt(0.5e1) * sqrt(0.2e1) / 96 - exp((-2*i) * phi2) * sqrt(0.10e2) * (0.1e1 + cos(phi)) / (0.1e1 - cos(phi)) * (0.360e3 * (0.1e1 - cos(phi)) ^ 4 - 0.960e3 * (0.1e1 + cos(phi)) * (0.1e1 - cos(phi)) ^ 3 + 0.360e3 * (0.1e1 + cos(phi)) ^ 2 * (0.1e1 - cos(phi)) ^ 2) * sqrt(0.21e2) / 11520 - exp((-2*i) * phi2) * exp((4*i) * phi1) * (0.1e1 + cos(phi)) * ((0.1e1 - cos(phi)) ^ 3) * sqrt(0.21e2) * sqrt(0.5e1) * sqrt(0.2e1) / 96;
out_tvalues(5, :) = (0.1e1 / 0.672e3*i) * exp((-1*i) * phi2) * exp((-4*i) * phi1) * sqrt(0.14e2) * ((0.1e1 - cos(phi)) ^ (0.3e1 / 0.2e1)) * ((0.1e1 + cos(phi)) ^ (0.5e1 / 0.2e1)) * sqrt(0.21e2) * sqrt(0.7e1) * sqrt(0.5e1) * sqrt(0.2e1) + (-0.1e1 / 0.5760e4*i) * exp((-1*i) * phi2) * sqrt(0.5e1) * ((0.1e1 - cos(phi)) ^ (-0.1e1 / 0.2e1)) * sqrt(0.1e1 + cos(phi)) * (-0.120e3 * (0.1e1 - cos(phi)) ^ 4 + 0.720e3 * (0.1e1 + cos(phi)) * (0.1e1 - cos(phi)) ^ 3 - 0.720e3 * (0.1e1 + cos(phi)) ^ 2 * (0.1e1 - cos(phi)) ^ 2 + 0.120e3 * (0.1e1 + cos(phi)) ^ 3 * (0.1e1 - cos(phi))) * sqrt(0.21e2) + (-0.1e1 / 0.672e3*i) * exp((-1*i) * phi2) * exp((4*i) * phi1) * sqrt(0.14e2) * ((0.1e1 - cos(phi)) ^ (0.5e1 / 0.2e1)) * ((0.1e1 + cos(phi)) ^ (0.3e1 / 0.2e1)) * sqrt(0.21e2) * sqrt(0.7e1) * sqrt(0.5e1) * sqrt(0.2e1);
out_tvalues(6, :) = exp((-4*i) * phi1) * sqrt(0.70e2) * ((0.1e1 + cos(phi)) ^ 2) * ((0.1e1 - cos(phi)) ^ 2) * sqrt(0.21e2) * sqrt(0.7e1) * sqrt(0.5e1) * sqrt(0.2e1) / 1344 + (((0.1e1 - cos(phi)) ^ 4 / 0.16e2 - (0.1e1 + cos(phi)) * (0.1e1 - cos(phi)) ^ 3 + 0.9e1 / 0.4e1 * (0.1e1 + cos(phi)) ^ 2 * (0.1e1 - cos(phi)) ^ 2 - (0.1e1 + cos(phi)) ^ 3 * (0.1e1 - cos(phi)) + (0.1e1 + cos(phi)) ^ 4 / 0.16e2) * sqrt(0.21e2) / 0.6e1) + exp((4*i) * phi1) * sqrt(0.70e2) * ((0.1e1 + cos(phi)) ^ 2) * ((0.1e1 - cos(phi)) ^ 2) * sqrt(0.21e2) * sqrt(0.7e1) * sqrt(0.5e1) * sqrt(0.2e1) / 1344;
out_tvalues(7, :) = (-0.1e1 / 0.672e3*i) * exp((i) * phi2) * exp((-4*i) * phi1) * sqrt(0.14e2) * ((0.1e1 - cos(phi)) ^ (0.5e1 / 0.2e1)) * ((0.1e1 + cos(phi)) ^ (0.3e1 / 0.2e1)) * sqrt(0.21e2) * sqrt(0.7e1) * sqrt(0.5e1) * sqrt(0.2e1) + (0.1e1 / 0.5760e4*i) * exp((i) * phi2) * sqrt(0.5e1) * sqrt(0.1e1 - cos(phi)) * ((0.1e1 + cos(phi)) ^ (-0.1e1 / 0.2e1)) * (0.120e3 * (0.1e1 + cos(phi)) * (0.1e1 - cos(phi)) ^ 3 - 0.720e3 * (0.1e1 + cos(phi)) ^ 2 * (0.1e1 - cos(phi)) ^ 2 + 0.720e3 * (0.1e1 + cos(phi)) ^ 3 * (0.1e1 - cos(phi)) - 0.120e3 * (0.1e1 + cos(phi)) ^ 4) * sqrt(0.21e2) + (0.1e1 / 0.672e3*i) * exp((i) * phi2) * exp((4*i) * phi1) * sqrt(0.14e2) * ((0.1e1 - cos(phi)) ^ (0.3e1 / 0.2e1)) * ((0.1e1 + cos(phi)) ^ (0.5e1 / 0.2e1)) * sqrt(0.21e2) * sqrt(0.7e1) * sqrt(0.5e1) * sqrt(0.2e1);
out_tvalues(8, :) = -exp((2*i) * phi2) * exp((-4*i) * phi1) * (0.1e1 + cos(phi)) * ((0.1e1 - cos(phi)) ^ 3) * sqrt(0.21e2) * sqrt(0.5e1) * sqrt(0.2e1) / 96 - exp((2*i) * phi2) * sqrt(0.10e2) / (0.1e1 + cos(phi)) * (0.1e1 - cos(phi)) * (0.360e3 * (0.1e1 + cos(phi)) ^ 2 * (0.1e1 - cos(phi)) ^ 2 - 0.960e3 * (0.1e1 + cos(phi)) ^ 3 * (0.1e1 - cos(phi)) + 0.360e3 * (0.1e1 + cos(phi)) ^ 4) * sqrt(0.21e2) / 11520 - exp((2*i) * phi2) * exp((4*i) * phi1) * ((0.1e1 + cos(phi)) ^ 3) * (0.1e1 - cos(phi)) * sqrt(0.21e2) * sqrt(0.5e1) * sqrt(0.2e1) / 96;
out_tvalues(9, :) = (0.1e1 / 0.336e3*i) * exp((3*i) * phi2) * exp((-4*i) * phi1) * ((0.1e1 - cos(phi)) ^ (0.7e1 / 0.2e1)) * sqrt(0.1e1 + cos(phi)) * sqrt(0.21e2) * sqrt(0.7e1) * sqrt(0.5e1) + (-0.1e1 / 0.40320e5*i) * exp((3*i) * phi2) * sqrt(0.35e2) * ((0.1e1 - cos(phi)) ^ (0.3e1 / 0.2e1)) * ((0.1e1 + cos(phi)) ^ (-0.3e1 / 0.2e1)) * (0.840e3 * (0.1e1 + cos(phi)) ^ 3 * (0.1e1 - cos(phi)) - 0.840e3 * (0.1e1 + cos(phi)) ^ 4) * sqrt(0.21e2) + (-0.1e1 / 0.336e3*i) * exp((3*i) * phi2) * exp((4*i) * phi1) * sqrt(0.1e1 - cos(phi)) * ((0.1e1 + cos(phi)) ^ (0.7e1 / 0.2e1)) * sqrt(0.21e2) * sqrt(0.7e1) * sqrt(0.5e1);
out_tvalues(10, :) = exp((4*i) * phi2) * exp((-4*i) * phi1) * ((0.1e1 - cos(phi)) ^ 4) * sqrt(0.21e2) * sqrt(0.7e1) * sqrt(0.5e1) * sqrt(0.2e1) / 1344 + exp((4*i) * phi2) * sqrt(0.70e2) * ((0.1e1 + cos(phi)) ^ 2) * ((0.1e1 - cos(phi)) ^ 2) * sqrt(0.21e2) / 96 + exp((4*i) * phi2) * exp((4*i) * phi1) * ((0.1e1 + cos(phi)) ^ 4) * sqrt(0.21e2) * sqrt(0.7e1) * sqrt(0.5e1) * sqrt(0.2e1) / 1344;
out_tvalues(11, :) = exp((-6*i) * phi2) * exp((-4*i) * phi1) * sqrt(0.66e2) * (0.1e1 - cos(phi)) * ((0.1e1 + cos(phi)) ^ 5) * sqrt(0.2e1) * sqrt(0.14e2) / 512 - exp((-6*i) * phi2) * sqrt(0.231e3) * ((0.1e1 - cos(phi)) ^ 3) * ((0.1e1 + cos(phi)) ^ 3) * sqrt(0.2e1) / 128 + exp((-6*i) * phi2) * exp((4*i) * phi1) * sqrt(0.66e2) * ((0.1e1 - cos(phi)) ^ 5) * (0.1e1 + cos(phi)) * sqrt(0.2e1) * sqrt(0.14e2) / 512;
out_tvalues(12, :) = (0.1e1 / 0.20437401600e11*i) * exp((-5*i) * phi2) * exp((-4*i) * phi1) * sqrt(0.22e2) * ((0.1e1 - cos(phi)) ^ (-0.1e1 / 0.2e1)) * ((0.1e1 + cos(phi)) ^ (0.9e1 / 0.2e1)) * (0.39916800e8 * (0.1e1 - cos(phi)) * (0.1e1 + cos(phi)) - 0.199584000e9 * (0.1e1 - cos(phi)) ^ 2) * sqrt(0.2e1) * sqrt(0.14e2) + (-0.1e1 / 0.14192640e8*i) * exp((-5*i) * phi2) * sqrt(0.77e2) * ((0.1e1 - cos(phi)) ^ (-0.5e1 / 0.2e1)) * ((0.1e1 + cos(phi)) ^ (0.5e1 / 0.2e1)) * (0.332640e6 * (0.1e1 - cos(phi)) ^ 5 * (0.1e1 + cos(phi)) - 0.332640e6 * (0.1e1 - cos(phi)) ^ 6) * sqrt(0.2e1) + (0.1e1 / 0.11264e5*i) * exp((-5*i) * phi2) * exp((4*i) * phi1) * sqrt(0.22e2) * ((0.1e1 - cos(phi)) ^ (-0.9e1 / 0.2e1)) * sqrt(0.1e1 + cos(phi)) * (0.110e3 * (0.1e1 - cos(phi)) ^ 9 * (0.1e1 + cos(phi)) - 0.22e2 * (0.1e1 - cos(phi)) ^ 10) * sqrt(0.2e1) * sqrt(0.14e2);
out_tvalues(13, :) = -exp((-4*i) * phi2) * exp((-4*i) * phi1) * ((0.1e1 + cos(phi)) ^ 4) * (0.3628800e7 * (0.1e1 + cos(phi)) ^ 2 - 0.72576000e8 * (0.1e1 - cos(phi)) * (0.1e1 + cos(phi)) + 0.163296000e9 * (0.1e1 - cos(phi)) ^ 2) * sqrt(0.2e1) * sqrt(0.14e2) / 1857945600 + exp((-4*i) * phi2) * sqrt(0.14e2) / ((0.1e1 - cos(phi)) ^ 2) * ((0.1e1 + cos(phi)) ^ 2) * (0.151200e6 * (0.1e1 - cos(phi)) ^ 4 * (0.1e1 + cos(phi)) ^ 2 - 0.362880e6 * (0.1e1 - cos(phi)) ^ 5 * (0.1e1 + cos(phi)) + 0.151200e6 * (0.1e1 - cos(phi)) ^ 6) * sqrt(0.2e1) / 2580480 - exp((-4*i) * phi2) * exp((4*i) * phi1) / ((0.1e1 - cos(phi)) ^ 4) * (0.90e2 * (0.1e1 - cos(phi)) ^ 8 * (0.1e1 + cos(phi)) ^ 2 - 0.40e2 * (0.1e1 - cos(phi)) ^ 9 * (0.1e1 + cos(phi)) + 0.2e1 * (0.1e1 - cos(phi)) ^ 10) * sqrt(0.2e1) * sqrt(0.14e2) / 1024;
out_tvalues(14, :) = (-0.1e1 / 0.5573836800e10*i) * exp((-3*i) * phi2) * exp((-4*i) * phi1) * sqrt(0.30e2) * sqrt(0.1e1 - cos(phi)) * ((0.1e1 + cos(phi)) ^ (0.7e1 / 0.2e1)) * (-0.10886400e8 * (0.1e1 + cos(phi)) ^ 2 + 0.97977600e8 * (0.1e1 - cos(phi)) * (0.1e1 + cos(phi)) - 0.130636800e9 * (0.1e1 - cos(phi)) ^ 2) * sqrt(0.2e1) * sqrt(0.14e2) + (0.1e1 / 0.3870720e7*i) * exp((-3*i) * phi2) * sqrt(0.105e3) * ((0.1e1 - cos(phi)) ^ (-0.3e1 / 0.2e1)) * ((0.1e1 + cos(phi)) ^ (0.3e1 / 0.2e1)) * (0.60480e5 * (0.1e1 - cos(phi)) ^ 3 * (0.1e1 + cos(phi)) ^ 3 - 0.272160e6 * (0.1e1 - cos(phi)) ^ 4 * (0.1e1 + cos(phi)) ^ 2 + 0.272160e6 * (0.1e1 - cos(phi)) ^ 5 * (0.1e1 + cos(phi)) - 0.60480e5 * (0.1e1 - cos(phi)) ^ 6) * sqrt(0.2e1) + (-0.1e1 / 0.3072e4*i) * exp((-3*i) * phi2) * exp((4*i) * phi1) * sqrt(0.30e2) * ((0.1e1 - cos(phi)) ^ (-0.7e1 / 0.2e1)) * ((0.1e1 + cos(phi)) ^ (-0.1e1 / 0.2e1)) * (0.72e2 * (0.1e1 - cos(phi)) ^ 7 * (0.1e1 + cos(phi)) ^ 3 - 0.54e2 * (0.1e1 - cos(phi)) ^ 8 * (0.1e1 + cos(phi)) ^ 2 + 0.6e1 * (0.1e1 - cos(phi)) ^ 9 * (0.1e1 + cos(phi))) * sqrt(0.2e1) * sqrt(0.14e2);
out_tvalues(15, :) = exp((-2*i) * phi2) * exp((-4*i) * phi1) * sqrt(0.30e2) * (0.1e1 - cos(phi)) * ((0.1e1 + cos(phi)) ^ 3) * (0.21772800e8 * (0.1e1 + cos(phi)) ^ 2 - 0.116121600e9 * (0.1e1 - cos(phi)) * (0.1e1 + cos(phi)) + 0.101606400e9 * (0.1e1 - cos(phi)) ^ 2) * sqrt(0.2e1) * sqrt(0.14e2) / 3715891200 - exp((-2*i) * phi2) * sqrt(0.105e3) / (0.1e1 - cos(phi)) * (0.1e1 + cos(phi)) * (0.20160e5 * (0.1e1 - cos(phi)) ^ 2 * (0.1e1 + cos(phi)) ^ 4 - 0.161280e6 * (0.1e1 - cos(phi)) ^ 3 * (0.1e1 + cos(phi)) ^ 3 + 0.302400e6 * (0.1e1 - cos(phi)) ^ 4 * (0.1e1 + cos(phi)) ^ 2 - 0.161280e6 * (0.1e1 - cos(phi)) ^ 5 * (0.1e1 + cos(phi)) + 0.20160e5 * (0.1e1 - cos(phi)) ^ 6) * sqrt(0.2e1) / 2580480 + exp((-2*i) * phi2) * exp((4*i) * phi1) * sqrt(0.30e2) / ((0.1e1 - cos(phi)) ^ 3) / (0.1e1 + cos(phi)) * (0.56e2 * (0.1e1 - cos(phi)) ^ 6 * (0.1e1 + cos(phi)) ^ 4 - 0.64e2 * (0.1e1 - cos(phi)) ^ 7 * (0.1e1 + cos(phi)) ^ 3 + 0.12e2 * (0.1e1 - cos(phi)) ^ 8 * (0.1e1 + cos(phi)) ^ 2) * sqrt(0.2e1) * sqrt(0.14e2) / 2048;
out_tvalues(16, :) = (0.1e1 / 0.928972800e9*i) * exp((-1*i) * phi2) * exp((-4*i) * phi1) * sqrt(0.3e1) * ((0.1e1 - cos(phi)) ^ (0.3e1 / 0.2e1)) * ((0.1e1 + cos(phi)) ^ (0.5e1 / 0.2e1)) * (-0.36288000e8 * (0.1e1 + cos(phi)) ^ 2 + 0.127008000e9 * (0.1e1 - cos(phi)) * (0.1e1 + cos(phi)) - 0.76204800e8 * (0.1e1 - cos(phi)) ^ 2) * sqrt(0.2e1) * sqrt(0.14e2) + (-0.1e1 / 0.1290240e7*i) * exp((-1*i) * phi2) * sqrt(0.42e2) * ((0.1e1 - cos(phi)) ^ (-0.1e1 / 0.2e1)) * sqrt(0.1e1 + cos(phi)) * (0.5040e4 * (0.1e1 - cos(phi)) * (0.1e1 + cos(phi)) ^ 5 - 0.75600e5 * (0.1e1 - cos(phi)) ^ 2 * (0.1e1 + cos(phi)) ^ 4 + 0.252000e6 * (0.1e1 - cos(phi)) ^ 3 * (0.1e1 + cos(phi)) ^ 3 - 0.252000e6 * (0.1e1 - cos(phi)) ^ 4 * (0.1e1 + cos(phi)) ^ 2 + 0.75600e5 * (0.1e1 - cos(phi)) ^ 5 * (0.1e1 + cos(phi)) - 0.5040e4 * (0.1e1 - cos(phi)) ^ 6) * sqrt(0.2e1) + (0.1e1 / 0.512e3*i) * exp((-1*i) * phi2) * exp((4*i) * phi1) * sqrt(0.3e1) * ((0.1e1 - cos(phi)) ^ (-0.5e1 / 0.2e1)) * ((0.1e1 + cos(phi)) ^ (-0.3e1 / 0.2e1)) * (0.42e2 * (0.1e1 - cos(phi)) ^ 5 * (0.1e1 + cos(phi)) ^ 5 - 0.70e2 * (0.1e1 - cos(phi)) ^ 6 * (0.1e1 + cos(phi)) ^ 4 + 0.20e2 * (0.1e1 - cos(phi)) ^ 7 * (0.1e1 + cos(phi)) ^ 3) * sqrt(0.2e1) * sqrt(0.14e2);
out_tvalues(17, :) = -exp((-4*i) * phi1) * ((0.1e1 - cos(phi)) ^ 2) * ((0.1e1 + cos(phi)) ^ 2) * (0.54432000e8 * (0.1e1 + cos(phi)) ^ 2 - 0.130636800e9 * (0.1e1 - cos(phi)) * (0.1e1 + cos(phi)) + 0.54432000e8 * (0.1e1 - cos(phi)) ^ 2) * sqrt(0.2e1) / 132710400 + (((0.1e1 + cos(phi)) ^ 6 / 0.64e2 - 0.9e1 / 0.16e2 * (0.1e1 - cos(phi)) * (0.1e1 + cos(phi)) ^ 5 + 0.225e3 / 0.64e2 * (0.1e1 - cos(phi)) ^ 2 * (0.1e1 + cos(phi)) ^ 4 - 0.25e2 / 0.4e1 * (0.1e1 - cos(phi)) ^ 3 * (0.1e1 + cos(phi)) ^ 3 + 0.225e3 / 0.64e2 * (0.1e1 - cos(phi)) ^ 4 * (0.1e1 + cos(phi)) ^ 2 - 0.9e1 / 0.16e2 * (0.1e1 - cos(phi)) ^ 5 * (0.1e1 + cos(phi)) + (0.1e1 - cos(phi)) ^ 6 / 0.64e2) * sqrt(0.2e1) / 0.4e1) - (0.7e1 / 0.512e3) * exp((4*i) * phi1) / ((0.1e1 - cos(phi)) ^ 2) / ((0.1e1 + cos(phi)) ^ 2) * (0.30e2 * (0.1e1 - cos(phi)) ^ 4 * (0.1e1 + cos(phi)) ^ 6 - 0.72e2 * (0.1e1 - cos(phi)) ^ 5 * (0.1e1 + cos(phi)) ^ 5 + 0.30e2 * (0.1e1 - cos(phi)) ^ 6 * (0.1e1 + cos(phi)) ^ 4) * sqrt(0.2e1);
out_tvalues(18, :) = (-0.1e1 / 0.928972800e9*i) * exp((i) * phi2) * exp((-4*i) * phi1) * sqrt(0.3e1) * ((0.1e1 - cos(phi)) ^ (0.5e1 / 0.2e1)) * ((0.1e1 + cos(phi)) ^ (0.3e1 / 0.2e1)) * (-0.76204800e8 * (0.1e1 + cos(phi)) ^ 2 + 0.127008000e9 * (0.1e1 - cos(phi)) * (0.1e1 + cos(phi)) - 0.36288000e8 * (0.1e1 - cos(phi)) ^ 2) * sqrt(0.2e1) * sqrt(0.14e2) + (0.1e1 / 0.1290240e7*i) * exp((i) * phi2) * sqrt(0.42e2) * sqrt(0.1e1 - cos(phi)) * ((0.1e1 + cos(phi)) ^ (-0.1e1 / 0.2e1)) * (-0.5040e4 * (0.1e1 + cos(phi)) ^ 6 + 0.75600e5 * (0.1e1 - cos(phi)) * (0.1e1 + cos(phi)) ^ 5 - 0.252000e6 * (0.1e1 - cos(phi)) ^ 2 * (0.1e1 + cos(phi)) ^ 4 + 0.252000e6 * (0.1e1 - cos(phi)) ^ 3 * (0.1e1 + cos(phi)) ^ 3 - 0.75600e5 * (0.1e1 - cos(phi)) ^ 4 * (0.1e1 + cos(phi)) ^ 2 + 0.5040e4 * (0.1e1 - cos(phi)) ^ 5 * (0.1e1 + cos(phi))) * sqrt(0.2e1) + (-0.1e1 / 0.512e3*i) * exp((i) * phi2) * exp((4*i) * phi1) * sqrt(0.3e1) * ((0.1e1 - cos(phi)) ^ (-0.3e1 / 0.2e1)) * ((0.1e1 + cos(phi)) ^ (-0.5e1 / 0.2e1)) * (0.20e2 * (0.1e1 - cos(phi)) ^ 3 * (0.1e1 + cos(phi)) ^ 7 - 0.70e2 * (0.1e1 - cos(phi)) ^ 4 * (0.1e1 + cos(phi)) ^ 6 + 0.42e2 * (0.1e1 - cos(phi)) ^ 5 * (0.1e1 + cos(phi)) ^ 5) * sqrt(0.2e1) * sqrt(0.14e2);
out_tvalues(19, :) = exp((2*i) * phi2) * exp((-4*i) * phi1) * sqrt(0.30e2) * ((0.1e1 - cos(phi)) ^ 3) * (0.1e1 + cos(phi)) * (0.101606400e9 * (0.1e1 + cos(phi)) ^ 2 - 0.116121600e9 * (0.1e1 - cos(phi)) * (0.1e1 + cos(phi)) + 0.21772800e8 * (0.1e1 - cos(phi)) ^ 2) * sqrt(0.2e1) * sqrt(0.14e2) / 3715891200 - exp((2*i) * phi2) * sqrt(0.105e3) * (0.1e1 - cos(phi)) / (0.1e1 + cos(phi)) * (0.20160e5 * (0.1e1 + cos(phi)) ^ 6 - 0.161280e6 * (0.1e1 - cos(phi)) * (0.1e1 + cos(phi)) ^ 5 + 0.302400e6 * (0.1e1 - cos(phi)) ^ 2 * (0.1e1 + cos(phi)) ^ 4 - 0.161280e6 * (0.1e1 - cos(phi)) ^ 3 * (0.1e1 + cos(phi)) ^ 3 + 0.20160e5 * (0.1e1 - cos(phi)) ^ 4 * (0.1e1 + cos(phi)) ^ 2) * sqrt(0.2e1) / 2580480 + exp((2*i) * phi2) * exp((4*i) * phi1) * sqrt(0.30e2) / (0.1e1 - cos(phi)) / ((0.1e1 + cos(phi)) ^ 3) * (0.12e2 * (0.1e1 - cos(phi)) ^ 2 * (0.1e1 + cos(phi)) ^ 8 - 0.64e2 * (0.1e1 - cos(phi)) ^ 3 * (0.1e1 + cos(phi)) ^ 7 + 0.56e2 * (0.1e1 - cos(phi)) ^ 4 * (0.1e1 + cos(phi)) ^ 6) * sqrt(0.2e1) * sqrt(0.14e2) / 2048;
out_tvalues(20, :) = (0.1e1 / 0.5573836800e10*i) * exp((3*i) * phi2) * exp((-4*i) * phi1) * sqrt(0.30e2) * ((0.1e1 - cos(phi)) ^ (0.7e1 / 0.2e1)) * sqrt(0.1e1 + cos(phi)) * (-0.130636800e9 * (0.1e1 + cos(phi)) ^ 2 + 0.97977600e8 * (0.1e1 - cos(phi)) * (0.1e1 + cos(phi)) - 0.10886400e8 * (0.1e1 - cos(phi)) ^ 2) * sqrt(0.2e1) * sqrt(0.14e2) + (-0.1e1 / 0.3870720e7*i) * exp((3*i) * phi2) * sqrt(0.105e3) * ((0.1e1 - cos(phi)) ^ (0.3e1 / 0.2e1)) * ((0.1e1 + cos(phi)) ^ (-0.3e1 / 0.2e1)) * (-0.60480e5 * (0.1e1 + cos(phi)) ^ 6 + 0.272160e6 * (0.1e1 - cos(phi)) * (0.1e1 + cos(phi)) ^ 5 - 0.272160e6 * (0.1e1 - cos(phi)) ^ 2 * (0.1e1 + cos(phi)) ^ 4 + 0.60480e5 * (0.1e1 - cos(phi)) ^ 3 * (0.1e1 + cos(phi)) ^ 3) * sqrt(0.2e1) + (0.1e1 / 0.3072e4*i) * exp((3*i) * phi2) * exp((4*i) * phi1) * sqrt(0.30e2) * ((0.1e1 - cos(phi)) ^ (-0.1e1 / 0.2e1)) * ((0.1e1 + cos(phi)) ^ (-0.7e1 / 0.2e1)) * (0.6e1 * (0.1e1 - cos(phi)) * (0.1e1 + cos(phi)) ^ 9 - 0.54e2 * (0.1e1 - cos(phi)) ^ 2 * (0.1e1 + cos(phi)) ^ 8 + 0.72e2 * (0.1e1 - cos(phi)) ^ 3 * (0.1e1 + cos(phi)) ^ 7) * sqrt(0.2e1) * sqrt(0.14e2);
out_tvalues(21, :) = -exp((4*i) * phi2) * exp((-4*i) * phi1) * ((0.1e1 - cos(phi)) ^ 4) * (0.163296000e9 * (0.1e1 + cos(phi)) ^ 2 - 0.72576000e8 * (0.1e1 - cos(phi)) * (0.1e1 + cos(phi)) + 0.3628800e7 * (0.1e1 - cos(phi)) ^ 2) * sqrt(0.2e1) * sqrt(0.14e2) / 1857945600 + exp((4*i) * phi2) * sqrt(0.14e2) * ((0.1e1 - cos(phi)) ^ 2) / ((0.1e1 + cos(phi)) ^ 2) * (0.151200e6 * (0.1e1 + cos(phi)) ^ 6 - 0.362880e6 * (0.1e1 - cos(phi)) * (0.1e1 + cos(phi)) ^ 5 + 0.151200e6 * (0.1e1 - cos(phi)) ^ 2 * (0.1e1 + cos(phi)) ^ 4) * sqrt(0.2e1) / 2580480 - exp((4*i) * phi2) * exp((4*i) * phi1) / ((0.1e1 + cos(phi)) ^ 4) * (0.2e1 * (0.1e1 + cos(phi)) ^ 10 - 0.40e2 * (0.1e1 - cos(phi)) * (0.1e1 + cos(phi)) ^ 9 + 0.90e2 * (0.1e1 - cos(phi)) ^ 2 * (0.1e1 + cos(phi)) ^ 8) * sqrt(0.2e1) * sqrt(0.14e2) / 1024;
out_tvalues(22, :) = (-0.1e1 / 0.20437401600e11*i) * exp((5*i) * phi2) * exp((-4*i) * phi1) * sqrt(0.22e2) * ((0.1e1 - cos(phi)) ^ (0.9e1 / 0.2e1)) * ((0.1e1 + cos(phi)) ^ (-0.1e1 / 0.2e1)) * (-0.199584000e9 * (0.1e1 + cos(phi)) ^ 2 + 0.39916800e8 * (0.1e1 - cos(phi)) * (0.1e1 + cos(phi))) * sqrt(0.2e1) * sqrt(0.14e2) + (0.1e1 / 0.14192640e8*i) * exp((5*i) * phi2) * sqrt(0.77e2) * ((0.1e1 - cos(phi)) ^ (0.5e1 / 0.2e1)) * ((0.1e1 + cos(phi)) ^ (-0.5e1 / 0.2e1)) * (-0.332640e6 * (0.1e1 + cos(phi)) ^ 6 + 0.332640e6 * (0.1e1 - cos(phi)) * (0.1e1 + cos(phi)) ^ 5) * sqrt(0.2e1) + (-0.1e1 / 0.11264e5*i) * exp((5*i) * phi2) * exp((4*i) * phi1) * sqrt(0.22e2) * sqrt(0.1e1 - cos(phi)) * ((0.1e1 + cos(phi)) ^ (-0.9e1 / 0.2e1)) * (-0.22e2 * (0.1e1 + cos(phi)) ^ 10 + 0.110e3 * (0.1e1 - cos(phi)) * (0.1e1 + cos(phi)) ^ 9) * sqrt(0.2e1) * sqrt(0.14e2);
out_tvalues(23, :) = exp((6*i) * phi2) * exp((-4*i) * phi1) * sqrt(0.66e2) * ((0.1e1 - cos(phi)) ^ 5) * (0.1e1 + cos(phi)) * sqrt(0.2e1) * sqrt(0.14e2) / 512 - exp((6*i) * phi2) * sqrt(0.231e3) * ((0.1e1 - cos(phi)) ^ 3) * ((0.1e1 + cos(phi)) ^ 3) * sqrt(0.2e1) / 128 + exp((6*i) * phi2) * exp((4*i) * phi1) * sqrt(0.66e2) * (0.1e1 - cos(phi)) * ((0.1e1 + cos(phi)) ^ 5) * sqrt(0.2e1) * sqrt(0.14e2) / 512;
