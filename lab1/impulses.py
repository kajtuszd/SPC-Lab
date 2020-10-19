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


'''
step responses to different parameters
'''
# proportional term

p1 = plt.figure(1)

G = -2*(s - 2)/(0*s**2 + s - 2)
H = -1/2*(s - 2)/(0*s**2 + s - 2)
I = 0*(s - 2)/(0*s**2 + s - 2)
J = 1/2*(s - 2)/(0*s**2 + s - 2)
K = 1*(s - 2)/(0*s**2 + s - 2)
L = 2*(s - 2)/(0*s**2 + s - 2)

t = numpy.linspace(0,30,1000)

t, yout = control.impulse_response(G, T=t)
plot1 = plt.plot(t, yout, label = "K=-2")

t, yout = control.impulse_response(H, T=t)
plot2 = plt.plot(t, yout, label = "K=-1/2")

t, yout = control.impulse_response(I, T=t)
plot3 = plt.plot(t, yout, label = "K(s) = 0")

t, yout = control.impulse_response(J, T=t)
plot4 = plt.plot(t, yout, label = "K(s) = 1/2")

t, yout = control.impulse_response(K, T=t)
plot5 = plt.plot(t, yout, label = "K(s) = 1")

t, yout = control.impulse_response(L, T=t)
plot6 = plt.plot(t, yout, label = "K(s) = 2")

plt.xlim((0,30))
plt.ylim((-3,3))
plt.title('Proportional')
plt.xlabel('Time [sec]')
plt.ylabel('Amplitude')
plt.legend(loc="upper right")
plt.grid()

# inertial I term
'''
             k
K(s) = ----------------
           1 + sT
'''
p2 = plt.figure(2)

G = 2/(s+1)
H = 3/(3*s+1)
I = 5/(6*s+1)
J = 4/(2*s+1)

t = numpy.linspace(0,30,1000)

t, yout = control.impulse_response(G, T=t)
plot1 = plt.plot(t, yout, label = "K(s) = 2/(s+1)")

t, yout = control.impulse_response(H, T=t)
plot2 = plt.plot(t, yout, label = "K(s) = 3/(3*s+1)")

t, yout = control.impulse_response(I, T=t)
plot3 = plt.plot(t, yout, label = "K(s) = 5/(6*s+1)")

t, yout = control.impulse_response(J, T=t)
plot4 = plt.plot(t, yout, label = "K(s) = 4/(2*s+1)")

plt.xlim((0,30))
plt.ylim((-3,6))
plt.title('Inertial I')
plt.xlabel('Time [sec]')
plt.ylabel('Amplitude')
plt.legend(loc="lower right")
plt.grid()

# oscillating inertial II
'''
               k
K(s) = -------------------
         (1+sT1)*(1+sT2)
'''
# |ksi| < 1

p3 = plt.figure(3)

G = 1/(s**2 - 3*s + 9)
H = 1/(s**2 + 2*s + 4)
I = 1/(s**2 + 0*s + 1)


t = numpy.linspace(0,30,1000)

t, yout = control.impulse_response(G, T=t)
plot1 = plt.plot(t, yout, label = "K(s) = 1/(s**2 - 3*s + 9)")

t, yout = control.impulse_response(H, T=t)
plot2 = plt.plot(t, yout, label = "K(s) = 1/(s**2 + 2*s + 4)")

t, yout = control.impulse_response(I, T=t)
plot3 = plt.plot(t, yout, label = "K(s) = 1/(s**2 + 0*s + 1)")

plt.xlim((0,15))
plt.ylim((-10,10))
plt.title('Oscillating inertial II')
plt.xlabel('Time [sec]')
plt.ylabel('Amplitude')
plt.legend(loc="upper right")
plt.grid()


# integral
'''
             k
K(s) = ---------------
          s*(Ts+1)
'''



p4 = plt.figure(4)

G = 1/(s*(1 + 2*s))
H = 2/(s*(1 + 3*s))
I = 3/(s*(1 + 2*s))

t = numpy.linspace(0,30,1000)

t, yout = control.impulse_response(G, T=t)
plot1 = plt.plot(t, yout, label = "K(s) = 1/(s*(1 + 2*s))")

t, yout = control.impulse_response(H, T=t)
plot2 = plt.plot(t, yout, label = "K(s) = 2/(s*(1 + 3*s))")

t, yout = control.impulse_response(I, T=t)
plot3 = plt.plot(t, yout, label = "K(s) = 3/(s*(1 + 2*s))")


plt.xlim((0,20))
plt.ylim((-3,10))
plt.title('Integral')
plt.xlabel('Time [sec]')
plt.ylabel('Amplitude')
plt.legend(loc="upper right")
plt.grid()


# derivative

'''
              T*s
K(s) = ------------------
             Td*s+1
'''

p5 = plt.figure(5)


G = s/(s+1)
H = 2*s/(3*s+1)
I = 3*s/(2*s+1)
J = 8*s/(4*s+1)


t = numpy.linspace(0,30,1000)

t, yout = control.impulse_response(G, T=t)
plot1 = plt.plot(t, yout, label = "K(s) = s/(s+1))")

t, yout = control.impulse_response(H, T=t)
plot2 = plt.plot(t, yout, label = "K(s) = 2*s/(3*s+1)")

t, yout = control.impulse_response(I, T=t)
plot3 = plt.plot(t, yout, label = "K(s) = 3*s/(2*s+1)")

t, yout = control.impulse_response(J, T=t)
plot4 = plt.plot(t, yout, label = "K(s) = 4*s/(4*s+1)")

plt.xlim((0,15))
plt.ylim((-3,3))
plt.title('Derivative')
plt.xlabel('Time [sec]')
plt.ylabel('Amplitude')
plt.legend(loc="upper right")
plt.grid()



# non - oscillating in II
'''
               k
K(s) = -------------------
         (1+sT1)*(1+sT2)     
'''
# |ksi| > 1

p6 = plt.figure(6)

G = 1/(s**2 - 8*s + 4)
H = 1/(s**2 + 4*s + 1)
# I = 1/(s**2 + s + 1)
# J = 1/(s**2 + 2*s + 1)

t = numpy.linspace(0,30,1000)

t, yout = control.impulse_response(G, T=t)
plot1 = plt.plot(t, yout, label = "K(s) = 1/(s**2 - 8*s + 4)")

t, yout = control.impulse_response(H, T=t)
plot2 = plt.plot(t, yout, label = "K(s) = 1/(s**2 + 4*s + 1)")

# t, yout = control.impulse_response(I, T=t)
# plot3 = plt.plot(t, yout, label = "d=1")

# t, yout = control.impulse_response(J, T=t)
# plot4 = plt.plot(t, yout, label = "d=2")

plt.xlim((0,20))
plt.ylim((-10,10))
plt.title('Non-oscillating inertial II')
plt.xlabel('Time [sec]')
plt.ylabel('Amplitude')
plt.legend(loc="upper right")
plt.grid()

plt.show()