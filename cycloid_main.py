# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 07:55:22 2023

@author: square
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
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


NUM = 100
GRRANGE = 100

SAVEFIG = False
SAVEFIG = True

R = 48#36
r = 8
l = 4
extr = R/r

print(f'extrude:{extr}')

## outer pin
##=----------------
pnum = int((R+r)/r)
pth = np.linspace(0,np.pi*2,pnum+1)
px = (R+r) * np.cos(pth)
py = (R+r) * np.sin(pth)

pole = np.vstack((px,py,np.ones(pnum+1)))
pole = rotZ(2*np.pi*4/(extr+1)) @ pole

## epitrochoid 
##----------------
epit = np.zeros((3,1))
for th in np.linspace(0,np.pi*2,NUM):
    phi = (R+r)/r*th
    x = (R+r)*np.cos(th)-l*np.cos(phi)
    y = (R+r)*np.sin(th)-l*np.sin(phi)
    a = np.array([[x],[y],[1]])
    epit = np.hstack((epit,a))

## inner roter
##----------------

offs = -r
inner = np.zeros((3,1))
for i in range(1,epit.shape[1]-1):
    tr0 = epit[:,i]
    tr1 = epit[:,i+1]

    # normal vector
    nn = (rotZ(np.pi/2.0) @ (tr1-tr0))
    unit = nn / np.linalg.norm(nn)
    ofv = ((offs * unit) + tr0).reshape(-1,1)

    inner = np.hstack((inner,ofv))
inner = np.hstack((inner,inner[:,1].reshape(-1,1)))
#inner = tr(l,0) @ inner

##----------------



num = 0
rot_ratio = (pnum-1)/pnum
for th in np.linspace(0,2*np.pi*(1/rot_ratio),NUM):
    fig,ax = plt.subplots(figsize=(8,8))
    
    ecce = rotZ(rot_ratio*th) @ np.array([[l],[0],[1]])
    inner_m = tr(ecce[0,0],ecce[1,0]) @ rotZ((rot_ratio-1)*th) @ inner

    drawCircle(ax,0,0,R)
    for i in range(pnum+1):
        drawCircle(ax,pole[0,i],pole[1,i],r)
    #ax.scatter(px,py)
    #ax.plot(epit[0,1:],epit[1,1:])
    ax.scatter(ecce[0,0],ecce[1,0])
    ax.scatter(pole[0],pole[1],c='g')
    ax.plot(inner_m[0,1:],inner_m[1,1:])

    ax.set_xlim([-GRRANGE,GRRANGE])
    ax.set_ylim([-GRRANGE,GRRANGE])
    ax.set_aspect('equal')
    ax.grid()
    
    if SAVEFIG:
        plt.savefig(f"anim/{num}.png")
    else:
        plt.show()
        
    num += 1
    
    plt.clf()
    plt.close()
    # break



