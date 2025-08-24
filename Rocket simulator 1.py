import numpy as np
import matplotlib.pyplot as pp
mass = 500  # kg
thrust = 7000  # N
g = 9.81  # m/s²
burn_time = 60  # seconds
total_time=120
dt = 0.5  # time step in seconds
burn_rate=2
rho = 1.225 # air density
Cd = 0.5 #drag coefficient
CSA = 0.75 # cross-sectional area


time = np.arange(0,total_time,dt)
acceleration = np.zeros_like(time)
velocity = np.zeros_like(time)
altitude=np.zeros_like(time)
masses = np.zeros_like(time)
F_drag = np.zeros_like(time)
altitude[0]=0
acceleration[0]=0
velocity[0]=0
masses[0] = 500
F_drag[0]=0
for i in range(1,len(time)):
    if time[i] <= burn_time:
        masses[i]= max(masses[i-1]-burn_rate*dt, 50)
        weight = masses[i]*g
        F_drag[i]=0.5*rho*CSA*Cd*((velocity[i-1])**2)
        drag_direction = np.sign(velocity[i-1])
        drag_force = F_drag[i]*drag_direction
        net_force = thrust-weight-drag_force
        acceleration[i] = net_force/masses[i]
        velocity[i] = velocity[i-1] + acceleration[i] * dt
        altitude[i] = altitude[i-1]+ velocity[i]*dt
    else:
        F_drag[i]=0.5*rho*CSA*Cd*((velocity[i-1])**2)
        drag_direction = np.sign(velocity[i-1])
        drag_force = F_drag[i]*drag_direction
        masses[i]= masses[i-1]
        weight=masses[i]*g
        net_force = -weight-drag_force
        acceleration[i] = net_force/masses[i]
        velocity[i] = velocity[i-1] + acceleration[i] * dt
        altitude[i] = altitude[i-1]+ velocity[i]*dt

terminal_velocity=np.sqrt((masses[-1]*g)/(rho*CSA*Cd))
pp.plot(time,altitude, label = "altitude (m)")
pp.plot(time,velocity, label = "velocity (m/s)")
pp.plot(time,acceleration, label = "acceleration (m/s^2)")
pp.plot(time,masses, label = "Mass (Kg)", linestyle = '--')
pp.plot(time,F_drag,label = "Drag(N)" )
pp.axvline(burn_time, color = 'red', linestyle = ':', label = 'Burnout Point')
pp.axhline(-terminal_velocity, color = 'gray', linestyle = ":", label = 'Terminal velocity' )
pp.legend()
pp.title("rocket ascent simulation")
pp.grid("True")
pp.show()