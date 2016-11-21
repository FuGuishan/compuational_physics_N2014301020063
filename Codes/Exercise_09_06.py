import math
import matplotlib.pyplot as plt
def sep(xini):
    alpha=0
    vtho=math.sqrt(2)
    vthe=[math.pi/4]
    vx=[vtho*math.cos(vthe[-1])]
    vy=[vtho*math.sin(vthe[-1])]
    x=[xini]
    y=[0]
    the=[0]
    t=[0]
    dt=0.01
    while t[-1]<1000:
        if -alpha*20<=x[-1]<=alpha*20:
            if y[-1]>20 or y[-1]<-20:
                vy.append(-vy[-1])
                vx.append(vx[-1])
                vthe.append(math.atan(float(vy[-1]/vx[-1])))
            else:
                vx.append(vx[-1])
                vy.append(vy[-1])
                vthe.append(vthe[-1])
        if x[-1]>alpha*20:
            if y[-1]**2+(x[-1]-alpha*20)**2>=400:
                thee=math.atan(float(y[-1]/(x[-1]-alpha*20)))
                vthe.append(math.pi-vthe[-1]+2*thee)
                vx.append(vtho*math.cos(vthe[-1]))
                vy.append(vtho*math.sin(vthe[-1]))
            else:
                vx.append(vx[-1])
                vy.append(vy[-1])
                vthe.append(vthe[-1])
        if x[-1]<-alpha*20:
            if y[-1]**2+(x[-1]+alpha*20)**2>=400:
                thee=math.atan(float(y[-1]/(x[-1]+alpha*20)))
                vthe.append(math.pi-vthe[-1]+2*thee)
                vx.append(vtho*math.cos(vthe[-1]))
                vy.append(vtho*math.sin(vthe[-1]))
            else:
                vx.append(vx[-1])
                vy.append(vy[-1])
                vthe.append(vthe[-1])
        x.append(x[-1]+vx[-1]*dt)
        y.append(y[-1]+vy[-1]*dt)
        the.append(math.atan(y[-1]/x[-1]))
        t.append(t[-1]+dt)
    return x,y,t
x1=sep(1)[0]
y1=sep(1)[1]
time=sep(1)[2]
x2=sep(1+10**(-5))[0]
y2=sep(1+10**(-5))[1]
length=len(x1)
sepa=[]
for i in range(length):
    new2=(x2[i]-x1[i])**2+(y2[i]-y1[i])**2
    new=math.sqrt(new2)
    sepa.append(new)
plt.plot(time,sepa)
plt.semilogy(time,sepa)
plt.title('divergence alpha=0')
plt.xlabel('time(s)')
plt.ylabel('separation')
plt.grid(True)
plt.show()
