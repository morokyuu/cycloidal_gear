# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 07:55:22 2023

@author: square
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
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

def drawCircle(ax, x, y, r):
    ax.add_patch(patches.Circle((x,y), radius=r, fill=False))
        
def drawLine(ax,x0,y0,x1,y1,color='blue'):
    ax.plot(np.array([x0,x1]),np.array([y0,y1]),color=color)

def drawPolyline(ax,poly,color='blue'):
    poly = poly.T
    poly = np.vstack((poly,poly[0,:]))
    for i in range(poly.shape[0]-1):
        drawLine(ax,poly[i,0],poly[i,1],poly[i+1,0],poly[i+1,1],color=color)


rc = 600
rs = 120
L = 100
Lx = 55
NUM = 100
GRRANGE = 800


class RollingCircle:
    def __init__(self,th):
        self.RATIO = (rs+rc)*2*np.pi / (rs*2*np.pi)
        self.pxy_ini = np.array([[rs*0.5],[0],[1]])
        self.track = np.zeros(1)
        self.setPos(th)

    def revolve(self,th):
        return rotZ(-th) @ tr(-rs+rc,0)

    def rotate(self,th):
        return rotZ(self.RATIO * th)

    def setPos(self,th):
        #self.rotate = rotZ(-th) @ tr(-rs+rc,0) @ rotZ(self.RATIO * th)
        
        self.xy = self.revolve(th) @ np.array([[0],[0],[1]])
        self.pxy = self.revolve(th) @ self.rotate(th) @ self.pxy_ini

        if self.track.shape[0] > 1:
            self.track = np.hstack((self.track, self.pxy))
        else:
            self.track = self.revolve(th) @ self.pxy_ini

    def draw(self,ax):
        drawCircle(ax, self.xy[0], self.xy[1], rs)
        ax.scatter(self.pxy[0],self.pxy[1])
        ax.plot(self.track[0],self.track[1])

view = tr(0,0)
sc = RollingCircle(0)
sc1 = RollingCircle((2*np.pi)/6)

for th in np.linspace(0,np.pi*2,NUM):
    fig,ax = plt.subplots(figsize=(8,8))

    sc.setPos(th)
    sc.draw(ax)

    sc1.setPos(th + (2*np.pi)/6)
    sc1.draw(ax)

    drawCircle(ax, 0,0, rc)

    ax.set_xlim([-GRRANGE,GRRANGE])
    ax.set_ylim([-GRRANGE,GRRANGE])
    ax.set_aspect('equal')
    ax.grid()
    
    plt.show()
    
    plt.clf()
    plt.close()
    # break



