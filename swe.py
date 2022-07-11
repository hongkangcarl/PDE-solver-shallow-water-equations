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

b = 10
g = 1
H = 10

xs = np.linspace(0, 1, 100)
ys = np.linspace(0, 1, 100)
ts = np.linspace(0, 1, 1024)

dx = xs[1] - xs[0]
dy = ys[1] - ys[0]
dt = ts[1] - ts[0]

x, y = np.meshgrid(xs, ys)

def grad(h):
    grad_h_x = (np.roll(h, -1, axis = 0) - np.roll(h, 1, axis = 0))/(2*dx)
    grad_h_x[0, :] = 0
    grad_h_x[-1, :] = 0

    grad_h_y = (np.roll(h, -1, axis = 1) - np.roll(h, 1, axis = 1))/(2*dy)
    grad_h_y[:, 0] = 0
    grad_h_y[:, -1] = 0
    
    return np.array([grad_h_x, grad_h_y])

def div(vec):
    return np.gradient(vec[0], axis = 0)/dx + np.gradient(vec[1], axis = 1)/dy


h_list = []
v_list = []

h_init = np.exp( (- (x - 0.2)**2 - (y - 0.2)**2) / (2 * 0.05**2) )
# h_init = np.zeros(x.shape)
v_init = np.zeros(grad(x).shape)

h_list.append(h_init)
v_list.append(v_init)

def add_a_drop(h):
    return h + 0.5 * np.exp(  (- (x - np.random.normal())**2 - (y - np.random.random())**2) / (2 * 0.02**2)  )


for i in range(1, len(ts)):
    
    v = np.zeros(v_init.shape)
    v[0] = (1 - dt * b) * v_list[-1][0] - dt * g * grad(h_list[-1])[0]
    v[1] = (1 - dt * b) * v_list[-1][1] - dt * g * grad(h_list[-1])[1]
    h = h_list[-1] - dt * H * div(v)
    # if i%10 == 0:
    #     h = add_a_drop(h)
    h[0, :] = h[1, :]
    h[-1, :] = h[-2, :]
    h[:, 0] = h[1, :]
    h[:, -1] = h[:, -2]
    
    v_list.append(v)
    h_list.append(h)

#%%

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
    


#%% without friction

h_list = []
v_list = []

h_init = np.exp( (- (x - 0.2)**2 - (y - 0.2)**2) / (2 * 0.05**2) )
# h_init = np.zeros(x.shape)
v_init = np.zeros(grad(x).shape)

h_list.append(h_init)
v_list.append(v_init)

for i in range(1, len(ts)):
    
    v = np.zeros(v_init.shape)
    v[0] = (1) * v_list[-1][0] - dt * g * grad(h_list[-1])[0]
    v[1] = (1) * v_list[-1][1] - dt * g * grad(h_list[-1])[1]
    h = h_list[-1] - dt * H * div(v)
    # if i%10 == 0:
    #     h = add_a_drop(h)
    h[0, :] = h[1, :]
    h[-1, :] = h[-2, :]
    h[:, 0] = h[1, :]
    h[:, -1] = h[:, -2]
    
    v_list.append(v)
    h_list.append(h)
    
    
    