# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 22:18:59 2023

@author: Gerardo González

from https://realpython.com/python-menus-toolbars/
"""

import sys

#from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QAction, QMainWindow
#from PyQt5.QtWidgets import QToolBar,  QLabel
from GMol_python import  Atom as Atom, Mol as Mol
from vispy import scene

Molecule = Mol ()

class Canvas(scene.SceneCanvas):

    def __init__(self):
        scene.SceneCanvas.__init__(self, keys=None)
        self.size = 800, 600
        self.unfreeze()
        self.view = self.central_widget.add_view()
        self.radius = 2.0
        self.view.camera = 'turntable'
     
        #self.freeze()

        # Add a 3D axis to keep us oriented
        scene.visuals.XYZAxis(parent=self.view.scene)


class Window(QMainWindow):
    """Main Window."""
    def __init__(self, parent=None):
        """Initializer."""
        super(Window, self).__init__(parent)
        self.setWindowTitle("3D- Molecular representations by Gerardo")
        self.resize(600, 400)
        #self._createActions()
        
        self._createActions()
        self._connectActions()
        self._createMenuBar()
                
        self.canvas = Canvas()
        self.canvas.create_native()
        self.canvas.native.setParent(self)
        
        #splitter.addWidget(self.canvas.native)

        self.setCentralWidget(self.canvas.native)
        #self.update_view()
        
        
        self.displayIt()
        
        #self._createToolBars()   # I want it??
        
    def _createMenuBar(self):
        menuBar = self.menuBar()
        # Creating menus using a QMenu object
        fileMenu = menuBar.addMenu("&File")
        fileMenu.addAction(self.newAction)
        fileMenu.addAction(self.openAction)
        fileMenu.addAction(self.saveAction)
        fileMenu.addAction(self.exitAction)
        # Creating menus using a title
        editMenu = menuBar.addMenu("&Edit")
        helpMenu = menuBar.addMenu("&Help")

    def _connectActions(self): # creo que esto se puede poner a seguir al la definic
        # Connect File actions
        
        self.newAction.triggered.connect(self.newFile)                                          #see
        self.openAction.triggered.connect(self.openFile)
        self.saveAction.triggered.connect(self.saveFile)
        self.exitAction.triggered.connect(self.close)
        # Connect Edit actions
        self.copyAction.triggered.connect(self.copyContent)
        self.pasteAction.triggered.connect(self.pasteContent)
        self.cutAction.triggered.connect(self.cutContent)
        # Connect Help actions
        self.helpContentAction.triggered.connect(self.helpContent)
        self.aboutAction.triggered.connect(self.about)
        
    def _createActions(self):         
        #Creating action using the first constructor         
        self.newAction = QAction("&New",self)
        self.openAction = QAction("&Open...", self)
        self.saveAction = QAction("&Save", self)
        self.exitAction = QAction("&Exit", self)
        self.copyAction = QAction("&Copy", self)
        self.pasteAction = QAction("&Paste", self)
        self.cutAction = QAction("C&ut", self)
        self.helpContentAction = QAction("&Help Content", self)
        self.aboutAction = QAction("&About", self)
   
    def Scenified (self):
           # Create canvas and view
           #canvas = scene.SceneCanvas(keys='interactive', size=(600, 600), show=True)
           self.view = self.canvas.central_widget.add_view()
           self.view.camera = scene.cameras.ArcballCamera(fov=0)
           self.view.camera.scale_factor = 200
      
    def  displayIt(self):
               self.Scenified()
               Molecule.prepareData()
               pos= Molecule.data
               if Molecule.nAtoms > 0 :
                   self.vis = scene.visuals.Markers(
                               pos = pos,
                               size=15,
                               antialias=0,
                               face_color=Molecule.colors,
                               edge_color='white',
                               edge_width=0,
                               scaling=True,
                               spherical=True,
                               )
               self.vis.parent = self.view.scene
                  
    


    def newFile(self):
        # Logic for creating a new file goes here...
        #self.centralWidget.setText("<b>File > New</b> clicked")
        print('NewFile')

    def openFile(self):
        # Logic for opening an existing file goes here...
        #self.centralWidget.setText("<b>File > Open...</b> clicked")
        print('Open File')
        
    def saveFile(self):
        # Logic for saving a file goes here...
        #self.centralWidget.setText("<b>File > Save</b> clicked")
        print('Save File')

    def copyContent(self):
        # Logic for copying content goes here...
        #self.centralWidget.setText("<b>Edit > Copy</b> clicked")
        print('Copy')

    def pasteContent(self):
        # Logic for pasting content goes here...
        #self.centralWidget.setText("<b>Edit > Paste</b> clicked")
        print('Paste')

    def cutContent(self):
        # Logic for cutting content goes here...
        #self.centralWidget.setText("<b>Edit > Cut</b> clicked")
        print('Cut')

    def helpContent(self):
        # Logic for launching help goes here...
        #self.centralWidget.setText("<b>Help > Help Content...</b> clicked")
        print('Help!')

    def about(self):
        # Logic for showing an about dialog content goes here...
        #self.centralWidget.setText("<b>Help > About...</b> clicked")
        print('About')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    Atoms=Atom(1, 30,30,30)
    Molecule.append (Atoms)
    Atoms=Atom(8, 30,20,30)
    Molecule.append (Atoms)
    Atoms=Atom(1, 30,20,20)
    Molecule.append (Atoms)
    
    win = Window()
    win.show()
    #sys.exit(
    app.exec_()
