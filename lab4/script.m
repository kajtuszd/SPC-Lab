clear all;
K_ob = tf([1], [12, 7, 1, 0]);
figure(10)
step(K_ob)
grid on;
grid minor;

P = 0.2897;
I = 0.006773;
D = 2.007;
N = 35.18;

K_p = P;
K_i = tf(I, [1, 0]);
K_d = tf([D*N, 0], [1, N]);
K_r = K_p + K_i + K_d;

K_otw = K_ob*K_r;
K_z = K_otw/(1 + K_otw);
K_e = 1/(1 + K_otw);

figure(1)
step(K_z)
grid on;
grid minor;

figure(2)
[e,time] = step(K_e, 10)
plot(time,e);
step(K_e, 100)
grid on;
grid minor;

figure(3)
lsim(K_r, e, time);
grid on;
grid minor;

% to discrete

Ts = 0.01:0.01:0.2;
for i=1:1:length(Ts)
    Ts_ = Ts(i);
    K_r_d = c2d(K_r, Ts_, 'zoh');
    G1 = K_r_d.Numerator{1, 1};
    G2 = K_r_d.Denominator{1, 1};
    sim("scheme.slx");
    tab(i) = ans.difference(length(ans.difference));    
end

figure(4)
plot(Ts, tab);
title("Difference of the integrals of the error squares depending on the sampling time");
xlabel("time [sec]");
ylabel("difference");
grid on;
grid minor;
Ts_ = 0.1;
K_r_d = c2d(K_r, Ts_, 'zoh');

G1 = K_r_d.Numerator{1, 1};
G2 = K_r_d.Denominator{1, 1};
sim("scheme.slx");


