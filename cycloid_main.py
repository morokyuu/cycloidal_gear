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


rc = 240
rs = 120
offs = 60
NUM = 100
GRRANGE = 800
TRACK_ENB = False
TRACK_ENB = True
SAVEFIG = False

class RollingCircle:
    def __init__(self,th_ini):
        self.th_ini = th_ini
        self.RATIO = (rs+rc)*2*np.pi / (rs*2*np.pi)
        self.pxy_ini = np.array([[rs*0.5],[0],[1]])
        self.track = np.zeros((3,1))

    def revolve(self,th):
        return rotZ(th-self.th_ini) @ tr(rs+rc,0)

    def rotate(self,th):
        return rotZ(self.RATIO * (th-self.th_ini))

    def setPos(self,th):
        self.xy = self.revolve(th) @ np.array([[0],[0],[1]])
        self.pxy = self.revolve(th) @ self.rotate(th) @ self.pxy_ini

    def getTrack(self):
        for th in np.linspace(0,2*np.pi,NUM):
            pxy = self.revolve(th) @ self.rotate(th) @ self.pxy_ini
            self.track = np.hstack((self.track, pxy))
        return self.track

    def draw(self,ax):
        drawCircle(ax, self.xy[0], self.xy[1], rs)
        ax.plot(np.array([self.xy[0],self.pxy[0]]),
                np.array([self.xy[1],self.pxy[1]]),
                color='green')
        ax.scatter(np.array([self.xy[0],self.pxy[0]]),
                np.array([self.xy[1],self.pxy[1]]),
                color='green')
        drawCircle(ax, self.pxy[0], self.pxy[1], offs)

view = tr(0,0)

sc = []
for th_offs in np.linspace(0,2*np.pi,5):
    sc.append(RollingCircle(th_offs))

track = sc[0].getTrack()


##----------------

track_offs = np.zeros((3,1))
for i in range(1,track.shape[1]-1):
    tr0 = track[:,i]
    tr1 = track[:,i+1]

    # normal vector
    nn = (rotZ(np.pi/2.0) @ (tr1-tr0))
    unit = nn / np.linalg.norm(nn)
    ofv = ((offs * unit) + tr0).reshape(-1,1)

    track_offs = np.hstack((track_offs,ofv))
track_offs = np.hstack((track_offs,track_offs[:,1].reshape(-1,1)))

##----------------

num = 0
for th in np.linspace(0,np.pi*2,NUM):
    fig,ax = plt.subplots(figsize=(8,8))

    poly = np.array([[0],[0],[1]])
    for s in sc:
        s.setPos(th)
        s.draw(ax)
        poly = np.hstack((poly,s.pxy))
    
    ax.plot(track[0,1:],track[1,1:])
    ax.plot(track_offs[0,1:],track_offs[1,1:])
    
    drawCircle(ax, 0,0, rc)
    drawCircle(ax, 0,0, rs+rc)

    drawPolyline(ax,poly[:,1:])
    
#    ecce = rotZ(((rc-rs)/rs+1) * th) @ sc[0].pxy_ini
#    ecce = np.hstack((np.zeros((3,1)),ecce))
#    ax.scatter(ecce[0],ecce[1])

    ax.set_xlim([-GRRANGE,GRRANGE])
    ax.set_ylim([-GRRANGE,GRRANGE])
    ax.set_aspect('equal')
    ax.grid()
    
    plt.show()

    if SAVEFIG:
        plt.savefig(f"anim/{num}.png")
    num += 1
    
    plt.clf()
    plt.close()
    # break



