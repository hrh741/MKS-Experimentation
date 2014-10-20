%% Prepare GSH Coefficients for the optimization
% Noah Paulson, Dipen Patel 2014-10-17
%
% Select orientations from the Hexagonal-Triclinic fundamental zone and
% generate the set of GSH coefficients which each represent the ODF
% function for a single orientation.

%% Orientation Selection

% v_phi1,V_phi,v_phi2: vectors which discretize the hexagonal fundamental
% zone into a number of orienations
v_phi1 = linspace(0,2*pi(),15);
v_Phi = linspace(0,pi()/2,6);
v_phi2 = linspace(0,pi()/3,4);

[X,Y,Z] = meshgrid(v_phi1,v_Phi,v_phi2);

% ori: array containing bunge-euler angles for all trial orientations
ori = [X(:), Y(:), Z(:)];

% plot the selected orientations for phi1 vs. Phi and Phi vs. phi2
close('all')

figure(1)
scatter(ori(:,1),ori(:,2),'.')
xlabel phi1 ; ylabel Phi; axis equal;

figure(2)
scatter(ori(:,2),ori(:,3),'.')
xlabel Phi ; ylabel phi2; axis equal;

% ori_len: number of trial orientations
N = length(ori(:,1));

%% Read OIM coefficient file

fileID = fopen('OIM_coeff_L07.txt','r');
formatSpec = '%d %d %d %f %f';
sizeA = [5, inf];
A = fscanf(fileID,formatSpec,sizeA)';

%% Regression

% ocf: number of coefficients from the original ODF harmonic description
ocf = 56;

% lvec: vector containing the sequence of l-numbers from 0 to L
lvec = A(:,1);

% w: "half width of the gaussian peak located at the orientation g_i" OIM
% software (is this the same as the Gaussian Smoothing angle?)
w = 2.5 * (pi()/180);

% Y_coeff: vector of the coefficients used
Y_coeff = A(:,4) + A(:,5)*1i;

X_coeff = zeros(ocf, N);

for ii = 1:N
    
    gsh_res = gsh_hcp_tri_L_7(ori(ii,1),ori(ii,2),ori(ii,3))';
    
    for jj = 1:length(gsh_res)

        l = lvec(jj);

        K = (exp(-0.25*(l^2)*(w^2))-exp(-0.25*((l+1)^2)*(w^2)))/(1-exp(-0.25*w^2));
        
        X_coeff(jj,ii) = (2*l+1)*K*gsh_res(jj);
%         X_coeff(jj,ii) = gsh_res(jj);

    end
end

save orientations.mat ori % Save array of the orientations used in the optimization
save X_coeff.mat X_coeff % Corresponding GSH basis function evaluated at discrete orientation
save Y_coeff.mat Y_coeff % Target ODF