clear all
kp=1:0.05:3;
ki=1:0.05:3;
for i=1:1:length(kp)
    for j=1:1:length(kp)
        Z(i,j)=MISE(kp(i),ki(j));
    end
end

[X,Y] = meshgrid (kp, ki)
mesh(X,Y,Z)
title("MISE w zależności od Kp i Ki");
xlabel("Kp"); ylabel("Ki"); zlabel("MISE");


clear all;
func=@(x,y)MISE(x,y);
x=3;
f=@(y)MISE(x,y);
x0=[0];
[x1,y1] = fminsearch(f,x0)

y=3;
f=@(x)MISE(x,y);
x0=[0];
[x2,y2] = fminsearch(f,x0)







