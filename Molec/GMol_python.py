# -*- coding: utf-8 -*-
"""
Spyder Editor

Lessons in OOP.
"""


import numpy as np
from vispy import app, scene
import vispy

import sys

from PyQt5.QtWidgets import QMenuBar, QMenu
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtWidgets import QToolBar, QAction



class Atom:
    def __init__(self, AtomicN, x,y,z):
        self.AtomicN= AtomicN
        self.x = x
        self.y = y
        self.z = z
        #self.data = np.array([x, y, z])
        self.colors = np.array([0, 0, 0])
    
class Mol():
    def __init__ (self):
        #QMainWindow.__init__(self)
        self.AtomList =[]
        self.nAtoms = 0
   

    def append(self, theAtom):
        #print("atom ",theAtom.x,' - ', theAtom.y,' - ',theAtom.z)
        self.AtomList.append(theAtom)
        
    
    def prepareData (self):
        i=0
        self.nAtoms = len(self.AtomList)
        print ("There are %i atoms in the molecule" %self.nAtoms)
        self.data = np.zeros((self.nAtoms, 3))
        self.colors = np.zeros((self.nAtoms,3))
        if self.nAtoms > 0:
            for anAtom in self.AtomList:
                match anAtom.AtomicN:
                    case 1: self.colors[i]= [0.99,0.99,0.99]
                    case 6: self.colors[i]= [0.49,0.49,0.49]
                    case 8: self.colors[i]= [0.99,0.0,0.0]
                    case _: self.colors[i]= [0.99,0.99,0.99]
            
                self.data[i][0] = anAtom.x
                self.data[i][1] = anAtom.y 
                self.data[i][2] = anAtom.z
                print ("An Atom ",self.data[i][0],' -- ' , self.data[i][1], ' -- ' ,self.data[i][2])
                i += 1
            #print ( self.data ) 
        
     # Create and show visual


        ''' 
        lines = np.array([[self.data[i], self.data[-1]]
                       for i in range(len(self.data) - 1)])
        line_vis = []

        for line in lines:
            vis2 = scene.visuals.Tube(line, radius=5)
            vis2.parent = self.view.scene
            line_vis.append(vis2)
        '''

        
