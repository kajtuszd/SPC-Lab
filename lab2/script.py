import control
import control.matlab
import matplotlib.pyplot as plt
import numpy
import cmath

'''
             1
K(s) = --------------
          Ts + 1
'''

s = control.TransferFunction.s

w = numpy.pi
T = 5

j = complex(0,1)

K1 = 1/(T*s+1)

K_jw = 1/(j*T*w+1)
A = abs(K_jw)
phi = numpy.angle(K_jw)

print("Amplitude = " + str(A))
print("Phase =  " + str(phi))

t = numpy.arange(0, 20, 0.01)
pulse = numpy.sin(w*t)
func = A*numpy.sin(w*t+phi)

yout, T, xout = control.matlab.lsim(sys=K1, U=pulse, T=t)
plt.plot(T, pulse, label = "Signal")
plt.plot(T, yout, label = "sin(wt)")
plt.plot(T, func, label = "A*sin(wt+y)")

plt.grid()
plt.title('Sine response')
plt.xlabel('Time [sec]')
plt.ylabel('Amplitude')
plt.legend(loc="lower right")

plt.show()


G1 = 1/(2*s+1)
G2 = 1/((2*s+1)*(s+1))
G3 = 2*s/(3*s+1)
G4 = 1/(s*(1 + 2*s))

omega = numpy.arange(0, 20, 1)

phi = 1
T = 2
G5 = 4*numpy.sin(omega*T+phi)

real, imag, freq = control.nyquist_plot(G1)
plt.title('Inertial I')
plt.show()

real, imag, freq = control.nyquist_plot(G2)
plt.title('Inertial II')
plt.show()

real, imag, freq = control.nyquist_plot(G3)
plt.title('Integral')
plt.show()

real, imag, freq = control.nyquist_plot(G4)
plt.title('Derivative')
plt.show()


