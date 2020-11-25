import matplotlib.pyplot as plt
import control 
import numpy as np

s = control.TransferFunction.s

def MISE(Kp, Ki):
    a=1; b=1; c=2
    K_ob = 1/(a*s**2+b*s+c)
    K_reg = Kp + Ki/s
    K_otw=K_ob*K_reg
    K_e = 1/(1 + K_otw)
    t = np.linspace(0,30,1000)
    t, yout = control.step_response(K_e, T=t)
    return t, yout
    

Kp = 4; Ki = 5
t, yout = MISE(Kp, Ki)
plot1 = plt.plot(t, yout, label = "uchyb")
plot2 = plt.plot(t, yout**2, label = "kwadrat uchybu")
plt.title('Uchyb')
plt.xlabel('Time [sec]')
plt.ylabel('e^2(t)')
plt.legend(loc="lower right")
plt.grid()
plt.show()
