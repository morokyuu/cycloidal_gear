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
from ezdxf.addons import r12writer

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


# NUM = 400
NUM = 100
GRRANGE = 50

SAVEFIG = False
#SAVEFIG = True

R = 24#36
r = 3
l = 1.8
extr = R/r

print(f'extrude:{extr}')

## outer pin
##=----------------
pnum = int((R+r)/r)
pth = np.linspace(0,np.pi*2,pnum+1)
px = (R+r) * np.cos(pth)
py = (R+r) * np.sin(pth)

pole = np.vstack((px,py,np.ones(pnum+1)))[:,:-1]
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
inner = inner[:,1:]

##----------------


# ## inner-roter dxf output 
# ##---------------
# with r12writer("scad/inner_roter.dxf") as dxf:
#     for i in range(0,NUM-1):
#         v0 = inner[:,i]
#         v1 = inner[:,i+1]
#         dxf.add_line((v0[0],v0[1]),(v1[0],v1[1]))
      

## output pin-hole
##---------------

OUTPIN_NUM = 4
OUTPIN_R   = 16
outpin = np.zeros((3,1))
for d in np.linspace(0,2*np.pi,OUTPIN_NUM+1):
    # print(d*180/np.pi)
    outpin = np.hstack((outpin,rotZ(d + np.pi/8) @ tr(OUTPIN_R,0) @ np.array([[0],[0],[1]])))
outpin = outpin[:,1:]



num = 0
rot_ratio = (pnum-1)/pnum
for th in np.linspace(0,2*np.pi*(1/rot_ratio),NUM):
    fig,ax = plt.subplots(figsize=(8,8))
    
    ## eccentric shaft
    ecce = rotZ(rot_ratio*th) @ np.array([[l],[0],[1]])
    # ax.scatter(ecce[0,0],ecce[1,0])
    drawCircle(ax,ecce[0,0],ecce[1,0],5/2.0)
    drawCircle(ax, 0, 0, 5)

    ## inner roter
    inn_rot = tr(ecce[0,0],ecce[1,0]) @ rotZ((rot_ratio-1)*th)
    inner_m = inn_rot @ inner
    outpin_m = inn_rot @ outpin
    ax.plot(inner_m[0,1:],inner_m[1,1:])
    #### output pin
    for i in range(OUTPIN_NUM):
        opx,opy = (outpin_m[0,i],outpin_m[1,i])
        # ax.scatter(opx,opy)
        drawCircle(ax, opx, opy, l)

    ## outer pole
    drawCircle(ax,0,0,R)
    for i in range(pnum):
        drawCircle(ax,pole[0,i],pole[1,i],r)
    # ax.scatter(pole[0],pole[1],c='g')
    
    

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
    break



