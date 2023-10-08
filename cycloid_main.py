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


rc = 50
rs = 25
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
        #self.pxy = np.array([[rs],[0],[1]])
        self.track = []
        self.set(x,y,th)

    def set(self,x,y,th):
        self.x = x
        self.y = y
        self.th = th
        self.rotate = tr(x,y) @ rotZ(-th*3)

    def getTrack(self,ax,track):
        return self.rotate @ track 
    
    def dot(self,H):
        self.rotate = H @ self.rotate
    
    def draw(self,ax):
        c = circle(rs)
        line = np.array([[0,rs],[0,0],[1,1]])

        c = self.rotate @ c
        line = self.rotate @ line
        ax.scatter(c[0],c[1],s=0.1)
        ax.plot(line[0],line[1])

        #self.track.append(np.array(line[:,1]))

view = tr(0,0)
#track = np.array([[rs],[0],[1]])
#track = []
sc = RollingCircle(rc+rs,0,0)

for th in np.linspace(0,np.pi*2,NUM):
    fig,ax = plt.subplots(figsize=(8,8))

    x = (rc + rs) * np.cos(th)
    y = (rc + rs) * np.sin(th)
    sc.set(x,y,th)

    sc.draw(ax)
#    sc.getTrack(ax,track)
    # newpxy = sc.getTrack(ax,track[:,0])
    # track = np.hstack((track,newpxy))
    # ax.plot(track[0],track[1])

    cc = circle(rc)
    ax.plot(cc[0],cc[1])


    ax.set_xlim([-500,500])
    ax.set_ylim([-500,500])
    ax.set_aspect('equal')
    ax.grid()
    
    plt.show()
    
    plt.clf()
    plt.close()
#    break



