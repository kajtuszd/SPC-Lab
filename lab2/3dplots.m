clear all;

figure(1)
T = 2;
omega = 0.0:0.1:50;
K = exp(-omega*T*j);
re = real(K);
im = imag(K);
plot3(re,im,omega)
xlabel('Real axis')
ylabel('Imagine axis')
zlabel('\omega')
title('Delay term')
grid on;

figure(2)
k = 3;
T = 2;
omega = 0.0:0.1:50;
K1 = k./(1+omega*T*j);
re = real(K1);
im = imag(K1);
plot3(re,im,omega)
xlabel('Real axis')
ylabel('Imagine axis')
zlabel('\omega')
title('Inertial term')
grid on;

figure(3)
T1 = 2;
T2 = 1;
omega = 0.0:0.1:50;
M = (T1.*omega*j+1).*(T2.*omega*j+1);
Kr = 1./M;
re = real(Kr);
im = imag(Kr);
plot3(re,im,omega)
xlabel('Real axis')
ylabel('Imagine axis')
zlabel('\omega')
title('Inertial II term')
grid on;

figure(4)
T = 3;
k = 1;
omega = 0.0:0.1:50;
L = k;
M = (1.*omega*j).*(T.*omega*j+1);
Krr = L./M;
re = real(Krr);
im = imag(Krr);
plot3(re,im,omega)
xlabel('Real axis')
ylabel('Imagine axis')
zlabel('\omega')
title('Integral')
grid on;

figure(5)
T = 2;
Td = 2;
omega = 0.0:0.1:100;
L = T.*omega*j;
M = Td.*omega*j+1;
Kp = L/M;
re = real(Kp);
im = imag(Kp);
plot3(re,im,omega)
xlabel('Real axis')
ylabel('Imagine axis')
zlabel('\omega')
title('Derivative')
grid on;



