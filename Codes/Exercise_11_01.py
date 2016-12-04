import numpy as np
from pylab import *
from math import *
import mpl_toolkits.mplot3d

def Hyperion(theta0):
    x=[]
    x.append(1)
    v_x=[]
    v_x.append(0)
    y=[]
    y.append(0)
    v_y=[]
    v_y.append(2*pi+1)
    
    omega=[]
    omega.append(10)
    theta=[]
    theta.append(theta0)
    t=[]
    t.append(0)
    time=10.0
    dt=0.0001
    for i in range(int(time/dt)):
        r=sqrt(x[i]**2+y[i]**2)
        v_x.append(v_x[i]-4*pi**2*x[i]*r**(-3)*dt)
        x.append(x[i]+v_x[i+1]*dt)
        v_y.append(v_y[i]-4*pi**2*y[i]*r**(-3)*dt)
        y.append(y[i]+v_y[i+1]*dt)
        
        omega.append(omega[i]-dt*12*pi**2*r**(-5)*(x[i]*sin(theta[i])-y[i]*cos(theta[i]))*(x[i]*cos(theta[i])+y[i]*sin(theta[i])))
        theta.append(theta[i]+omega[i+1]*dt)
        t.append(t[i]+dt)
    return [theta,omega,t,x,y]
H0=Hyperion(0)
theta=H0[0]
omega=H0[1]
t=H0[2]
x=H0[3]
y=H0[4]
H1=Hyperion(0.01)
dtheta=np.array(H1[0])-np.array(H0[0])
#plot

figure(figsize=[15,10])
subplot(121)
plot(t,theta)
title('angle versus time',fontsize=16)
xlabel('time(yr)')
ylabel('angle(radians)')
subplot(122)
plot(t,omega)
title('omega versus time',fontsize=16)
xlabel('time(yr)')
ylabel('omega(radians)')
savefig('Hyperion.png')
show()

plot(t,dtheta)
title('dtheta versus time',fontsize=16)
xlabel('time(yr)')
ylabel('dtheta(radians)')
savefig('Hyperion dtheta.png')
show()
