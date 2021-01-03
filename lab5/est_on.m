clear all;
close all;
clc; 

samples = 50;
b = [3,4,5];
p = [1000,1000,1000];
P = diag(p);
estim_on = [0,0,0];

% 1st iteration
u = [rand(),0,0];
z = randn();

y = u(1)*b(1)+u(2)*b(2)+u(3)*b(3)+z;
estim_on = transpose(estim_on);
phi = transpose(u);

E = y-transpose(phi)*estim_on;
P = P-((P*phi*transpose(phi)*P) / (1+transpose(phi)*P*phi));
estim_on = estim_on + P*phi*E;
norm_(1) = norm(estim_on - b);

plot(1, norm_(1), "bo");
figure(1)
grid on;
hold on;
xlabel("Number of samples");
ylabel("Estimator");

% 2nd iteration
u = [rand(), rand(), 0];
z = randn();
y = u(1)*b(1)+u(2)*b(2)+u(3)*b(3)+z;
phi = transpose(u);
E = y-transpose(phi)*estim_on;
P = P-((P*phi*transpose(phi)*P) / (1+transpose(phi)*P*phi));
estim_on = estim_on + P*phi*E;
norm_(2) = norm(estim_on - b);

plot(2, norm_(2), "bo");
figure(1)
grid on;
hold on;
xlabel("Number of samples");
ylabel("Estimator");

% other iterations
for i=1 : samples-2
    u = [rand(), rand(), rand()];
    z = randn();
    y = u(1)*b(1)+u(2)*b(2)+u(3)*b(3)+z;
    phi = transpose(u);
    E = y-transpose(phi)*estim_on;
    P = P-((P*phi*transpose(phi)*P) / (1+transpose(phi)*P*phi));
    estim_on = estim_on + P*phi*E;
    norm_(i+2) = norm(estim_on - b);
    figure(1)
    plot(i+2, norm_(i+2), "bo");
    grid on;
    hold on;
    xlabel("Number of samples");
    ylabel("Estimator");
end





























