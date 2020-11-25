function res=MISE(Kp, Ki)
a=1; b=1; c=2;
Kob=tf(1,[a,b,c]);
K_p=tf(Kp);
K_i=tf(Ki,[1,0]);
Kreg=K_p+K_i;
Kotw=Kob*Kreg;
Ke=1/(1+Kotw);
[k,t]=step(Ke,30);
delta_t=t(2)-t(1);
res=delta_t.*sum(k.*k);
end
