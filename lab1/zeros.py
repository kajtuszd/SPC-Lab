import control
import matplotlib.pyplot as plt
import numpy 
import math
'''
           a*s + b
K(s) = -------------------
        c*s**2 + d*s + e
'''
s = control.TransferFunction.s


p1 = plt.figure(1)

G = (s+2)/((s-1)*(s+5))
print(G)


p, z = control.pzmap(G)

angle = numpy.linspace(-numpy.pi, numpy.pi, 200)
plt.plot(numpy.sin(angle), numpy.cos(angle), color='gray', linewidth=0.4)
plt.plot(numpy.real(p), numpy.imag(p), '--', color='gray')

plt.show()
print(p)

p2 = plt.figure(2)

t = numpy.linspace(0,30,1000)


t, yout = control.impulse_response(G, t)
plot1 = plt.plot(t, yout)
plt.xlim((0,30))
plt.ylim((-20,20))
plt.title('Impulse response')
plt.xlabel('Time [sec]')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

t, yout = control.step_response(G, t)
plot1 = plt.plot(t, yout)
plt.xlim((0,30))
plt.ylim((-20,20))
plt.title('Step response')
plt.xlabel('Time [sec]')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

