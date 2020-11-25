import matplotlib.pyplot as plt
import control 
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import scipy.interpolate as interp


s = control.TransferFunction.s

def MISE(Kp, Ki, t_lins):
    a=1; b=1; c=2
    K_ob = 1/(a*s**2+b*s+c)
    K_reg = Kp + Ki/s
    K_otw=K_ob*K_reg
    K_e = 1/(1 + K_otw)
    t = np.linspace(0,t_lins,100)
    t, yout = control.step_response(K_e, T=t)
    delta_t = t[1] - t[0]
    result = delta_t*sum(yout**2)
    return result

'''
Ki = const
'''
time = 20
Kp = np.linspace(0, time, 200)
Ki = 2
mise = [None] * 200

for i in range(200):
    mise[i] = MISE(Kp[i], Ki, time)

plt.figure(1)
plot1 = plt.plot(Kp, mise)
plt.title('Badanie MISE przy zmianie Kp')
plt.xlabel('Kp')
plt.ylabel('MISE(Kp, Ki)')
plt.grid()

'''
Kp = const     
'''

time = 6
Kp = 2
Ki = np.linspace(0, time, 600)
mise = [None] * 600

for i in range(600):
    mise[i] = MISE(Kp, Ki[i], time)

plt.figure(2)
plot2 = plt.plot(Ki, mise)
plt.title('Badanie MISE przy zmianie Ki')
plt.xlabel('Ki')
plt.ylabel('MISE(Kp, Ki)')
plt.grid()
plt.show()
