#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 18:18:45 2021

@author: carl
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib import animation

# parameter values

b = 10   # friction coefficient
g = 1    # gravity acceleration
H = 10   # mean height of the surface


# discretize the space (x, y) and time (t)

xs = np.linspace(0, 1, 100)
ys = np.linspace(0, 1, 100)
ts = np.linspace(0, 1, 1024)

dx = xs[1] - xs[0]
dy = ys[1] - ys[0]
dt = ts[1] - ts[0]

x, y = np.meshgrid(xs, ys)


# finite difference treatment of grad h = [h(x+∆x) - h(x-∆x)]/(2∆x)

def grad(h):
    grad_h_x = (np.roll(h, -1, axis = 0) - np.roll(h, 1, axis = 0))/(2*dx)
    grad_h_x[0, :] = 0   # boundary condition: reflecting
    grad_h_x[-1, :] = 0  # boundary condition: reflecting

    grad_h_y = (np.roll(h, -1, axis = 1) - np.roll(h, 1, axis = 1))/(2*dy)
    grad_h_y[:, 0] = 0   # boundary condition: reflecting
    grad_h_y[:, -1] = 0  # boundary condition: reflecting
    
    return np.array([grad_h_x, grad_h_y])


# finite difference treatment of div v

def div(vec):
    return np.gradient(vec[0], axis = 0)/dx + np.gradient(vec[1], axis = 1)/dy


# prepare the list to store the numerical solutions

h_list = []
v_list = []


# initial condition: a single Gaussian pulse, no initial velocities

h_init = np.exp( (- (x - 0.2)**2 - (y - 0.2)**2) / (2 * 0.05**2) )
v_init = np.zeros(grad(x).shape)


# store the initial condition into the lists

h_list.append(h_init)
v_list.append(v_init)


# add another Gaussian pulse at a stochastic position (not used)

def add_a_drop(h):
    return h + 0.5 * np.exp(  (- (x - np.random.normal())**2 - (y - np.random.random())**2) / (2 * 0.02**2)  )


# start the simulation, for loop over the descritized time

for i in range(1, len(ts)):
    
    # calculate the velocities based on the current h(x, y, t)
    v = np.zeros(v_init.shape)
    v[0] = (1 - dt * b) * v_list[-1][0] - dt * g * grad(h_list[-1])[0]
    v[1] = (1 - dt * b) * v_list[-1][1] - dt * g * grad(h_list[-1])[1]
    
    # calculate the next-step h(x, y, t+∆t) based on the velocities
    h = h_list[-1] - dt * H * div(v)
    h[0, :] = h[1, :]
    h[-1, :] = h[-2, :]
    h[:, 0] = h[1, :]
    h[:, -1] = h[:, -2]
    
    # store the numerical results into the lists
    v_list.append(v)
    h_list.append(h)


# plot the animation of results
def time_plot(h_list):
    
    fig = plt.figure(figsize = (5, 5))
    ax = plt.axes(projection='3d')
    ax.relim()
    ax.autoscale_view()
    
    def init():
        return
    
    def animate(i):
        ax.clear()
        ax.plot_surface(x, y, h_list[i * 2], rstride=1, cstride=1,)
        ax.set_zlim(-0.4, 2)
        plt.title(str(i))
        print(i)
        return
    
    anim = animation.FuncAnimation(fig, animate, init_func = init, frames = 500, interval = 0.04, blit = False)
    anim.save('test.mp4', fps = 1/0.04, writer = 'ffmpeg', dpi = 100)

time_plot(h_list)

