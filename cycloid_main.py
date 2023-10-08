# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 07:55:22 2023

@author: square
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys
import time

import matplotlib.style as mplstyle
mplstyle.use('fast')

def rotZ(th):
    return np.array([
        [ np.cos(th), np.sin(th), 0.0],
        [-np.sin(th), np.cos(th), 0.0],
        [          0,          0, 1.0]
        ])

def tr(x,y):
    return np.array([
        [        1.0,          0,   x],
        [          0,        1.0,   y],
        [          0,          0, 1.0]
        ])

def drawLine(ax,x0,y0,x1,y1,color='blue'):
    ax.plot(np.array([x0,x1]),np.array([y0,y1]),color=color)

def drawPolyline(ax,poly,color='blue'):
    poly = poly.T
    poly = np.vstack((poly,poly[0,:]))
    for i in range(poly.shape[0]-1):
        drawLine(ax,poly[i,0],poly[i,1],poly[i+1,0],poly[i+1,1],color=color)


rc = 200
rs = 100
L = 100
Lx = 55
NUM = 100

def circle(r):
    PITCH = 300
    d = np.linspace(0,np.pi*2,PITCH)
    circle = np.array([
        r * np.cos(d),
        r * np.sin(d),
        np.ones(PITCH)
        ])
    return circle


class RollingCircle:
    def __init__(self,x,y,th):
        
        self.pxy_ini = np.array([[rs],[0],[1]])
        self.track = self.pxy_ini * 1 ##copy to track
        
        #self.setPos(x,y,th)
        

    def setPos(self,x,y,th):
        self.x = x
        self.y = y
        self.th = th
        self.rotate = tr(x,y) @ rotZ(-th*3)
        
        self.c = self.rotate @ circle(rs)
        self.pxy = self.rotate @ self.pxy_ini
        
        self.track = np.hstack((self.track, self.pxy))

    def dot(self,H):
        self.rotate = H @ self.rotate
    
    def draw(self,ax):
        ax.scatter(self.c[0],self.c[1],s=0.1)
        ax.scatter(self.pxy[0],self.pxy[1])
        
        

        #self.track.append(np.array(line[:,1]))

view = tr(0,0)
sc = RollingCircle(rc+rs,0,0)
cc = circle(rc)

for th in np.linspace(0,np.pi*2,NUM):
    fig,ax = plt.subplots(figsize=(8,8))

    x = (rc + rs) * np.cos(th)
    y = (rc + rs) * np.sin(th)
    # print(f'{x},{y}')
    sc.setPos(x,y,th)

    sc.draw(ax)
    ax.plot(cc[0],cc[1])

    ax.set_xlim([-500,500])
    ax.set_ylim([-500,500])
    ax.set_aspect('equal')
    ax.grid()
    
    plt.show()
    
    plt.clf()
    plt.close()
    # break



