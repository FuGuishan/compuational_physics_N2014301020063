import pylab as pl
import math
class trajectories:
    def __init__(self,mass=10, time_step=0.1,total_time=10,initial_velocity_x=50,initial_velocity_y=50,
    initial_x=0,initial_y=0,B2=0):
        self.m = mass
        self.dt = time_step
        self.time = total_time
        self.initial_velocity_x=initial_velocity_x
        self.initial_velocity_y=initial_velocity_y
        self.v_x = [initial_velocity_x]
        self.v_y = [initial_velocity_y]
        self.v=[math.sqrt(pow(initial_velocity_x,2)+pow(initial_velocity_y,2))]
        self.x=[initial_x]
        self.y=[initial_y]
        self.t = [0]
        self.B2=B2
    def calculate(self):
        _time = 0
        while(_time < self.time):
            self.v.append(math.sqrt(pow(self.v_x[-1],2)+pow(self.v_y[-1],2)))
            self.v_x.append(self.v_x[-1]-(self.B2/self.m)\
            *self.v[-1]*self.dt*self.v_x[-1])
            self.v_y.append(self.v_y[-1]-(4.03*pow(10,14)\
        /pow((self.y[-1]+6.37*pow(10,6)),2))*self.dt-\
        (self.B2/self.m)*self.v[-1]*self.dt*self.v_y[-1])
            self.x.append(self.v_x[-1]*self.dt+self.x[-1])
            self.y.append(self.v_y[-1]*self.dt+self.y[-1])
            self.t.append(_time)
            _time += self.dt    
    def show_results(self):
        font = {'family': 'serif',
                'color':  'darkred',
                'weight': 'normal',
                'size': 15,}
        pl.plot(self.x, self.y,label='g is not a constant')
        pl.title('Cannon shell trajectories', fontdict = font)
        pl.xlabel('x ($km$)')
        pl.ylabel('y ($km$)')
        pl.legend()
        pl.show()
a = trajectories()
a.calculate()
a.show_results()
