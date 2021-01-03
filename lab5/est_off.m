clear all;
close all;
clc; 

samples = 1000;
b = [3,4,5];
Y = ones(1,samples);
Phi = ones(samples,3);

% 1st iteration
u = [rand(),0,0];
z = randn();
Y(1) = u(1)*b(1)+u(2)*b(2)+u(3)*b(3)+z;
Phi(1,:) = u;

% 2nd iteration
u = [rand(),rand(),0];
z = randn();
Y(1) = u(1)*b(1)+u(2)*b(2)+u(3)*b(3)+z;
Phi(2,:) = u;

for i=1 : samples-2
    u = rand(1,3);
    z = randn();
    Y(i+2) = u(1)*b(1)+u(2)*b(2)+u(3)*b(3)+z;
    Phi(i+2,:) = u;
end

estim_off = inv(transpose(Phi)*Phi)*transpose(Phi)*transpose(Y);
for i=1 : samples
    estim_off = inv(transpose(Phi(1:i,:))*Phi(1:i,:))*transpose(Phi(1:i,:))*transpose(Y(1:i));
    norm_(i) = norm(estim_off-b);
end

for i=1 : samples-2
    figure(1)
    plot(i+2, norm_(i+2),"ro");
    grid on;
    hold on;
    xlabel("Number of samples");
    ylabel("Estimator");
end

