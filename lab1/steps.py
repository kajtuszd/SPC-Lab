import control
import matplotlib.pyplot as plt
import numpy 


'''
           a*s + b
K(s) = -------------------
        c*s**2 + d*s + e
'''

s = control.TransferFunction.s


'''
step responses to different parameters
'''
# a)
p1 = plt.figure(1)

G = (1/2*s + 1)/(s**2 + s + 1)
H = (s + 1)/(s**2 + s + 1)
I = (2*s + 1)/(s**2 + s + 1)
J = (4*s + 1)/(s**2 + s + 1)

t = numpy.linspace(0,30,1000)

t, yout = control.step_response(G, T=t)
plot1 = plt.plot(t, yout, label = "a=1/2")

t, yout = control.step_response(H, T=t)
plot2 = plt.plot(t, yout, label = "a=1")

t, yout = control.step_response(I, T=t)
plot3 = plt.plot(t, yout, label = "a=2")

t, yout = control.step_response(J, T=t)
plot4 = plt.plot(t, yout, label = "a=4")

plt.xlim((0,30))
plt.ylim((0,3))
plt.title('Changing a')
plt.xlabel('Time [sec]')
plt.ylabel('Amplitude')
plt.legend(loc="upper right")
plt.grid()

# b)
p2 = plt.figure(2)

G = (s - 2)/(s**2 + s + 1)
H = (s)/(s**2 + s + 1)
I = (s + 1)/(s**2 + s + 1)
J = (s + 2)/(s**2 + s + 1)

t = numpy.linspace(0,30,1000)

t, yout = control.step_response(G, T=t)
plot1 = plt.plot(t, yout, label = "b=-2")

t, yout = control.step_response(H, T=t)
plot2 = plt.plot(t, yout, label = "b=0")

t, yout = control.step_response(I, T=t)
plot3 = plt.plot(t, yout, label = "b=1")

t, yout = control.step_response(J, T=t)
plot4 = plt.plot(t, yout, label = "b=2")

plt.xlim((0,30))
plt.ylim((-3,3))
plt.title('Changing b')
plt.xlabel('Time [sec]')
plt.ylabel('Amplitude')
plt.legend(loc="upper right")
plt.grid()


# c)
p3 = plt.figure(3)

G = (s + 1)/((- 3/4)*s**2 + s + 1)
H = (s + 1)/(s + 1)
I = (s + 1)/(1/2*s**2 + s + 1)
J = (s + 1)/(5* s**2 + s + 1)

t = numpy.linspace(0,30,1000)

t, yout = control.step_response(G, T=t)
plot1 = plt.plot(t, yout, label = "c=-3/4")

t, yout = control.step_response(H, T=t)
plot2 = plt.plot(t, yout, label = "c=0")

t, yout = control.step_response(I, T=t)
plot3 = plt.plot(t, yout, label = "c=1/2")

t, yout = control.step_response(J, T=t)
plot4 = plt.plot(t, yout, label = "c=5")

plt.xlim((0,20))
plt.ylim((-3,3))
plt.title('Changing c')
plt.xlabel('Time [sec]')
plt.ylabel('Amplitude')
plt.legend(loc="upper right")
plt.grid()


# d)
p4 = plt.figure(4)

G = (s + 1)/(s**2 - 1/2*s + 1)
H = (s + 1)/(s**2 + 1)
I = (s + 1)/(s**2 + s + 1)
J = (s + 1)/(s**2 + 2*s + 1)

t = numpy.linspace(0,30,1000)

t, yout = control.step_response(G, T=t)
plot1 = plt.plot(t, yout, label = "d=-1/2")

t, yout = control.step_response(H, T=t)
plot2 = plt.plot(t, yout, label = "d=0")

t, yout = control.step_response(I, T=t)
plot3 = plt.plot(t, yout, label = "d=1")

t, yout = control.step_response(J, T=t)
plot4 = plt.plot(t, yout, label = "d=2")

plt.xlim((0,20))
plt.ylim((-10,10))
plt.title('Changing d')
plt.xlabel('Time [sec]')
plt.ylabel('Amplitude')
plt.legend(loc="upper right")
plt.grid()


# e)
p5 = plt.figure(5)

G = (s + 1)/(s**2 + s - 1)
H = (s + 1)/(s**2 + s)
I = (s + 1)/(s**2 + s + 1/2)
J = (s + 1)/(s**2 + s + 2)

t = numpy.linspace(0,30,1000)

t, yout = control.step_response(G, T=t)
plot1 = plt.plot(t, yout, label = "e=-1")

t, yout = control.step_response(H, T=t)
plot2 = plt.plot(t, yout, label = "e=0")

t, yout = control.step_response(I, T=t)
plot3 = plt.plot(t, yout, label = "e=1/2")

t, yout = control.step_response(J, T=t)
plot4 = plt.plot(t, yout, label = "e=2")

plt.xlim((0,20))
plt.ylim((-1,20))
plt.title('Changing e')
plt.xlabel('Time [sec]')
plt.ylabel('Amplitude')
plt.legend(loc="upper right")
plt.grid()

plt.show()