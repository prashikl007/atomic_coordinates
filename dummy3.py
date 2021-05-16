# -*- coding: utf-8 -*-
"""
Created on Sat May  1 11:58:40 2021

@author: PRASHIK
"""
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 22:47:35 2021

@author: PRASHIK
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import (QApplication, QWidget, QFileDialog, QPushButton, QLabel, QGridLayout, QVBoxLayout)


class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Protein Sequence Analysis - Prashik Lokhande")
        self.setLayout(QVBoxLayout())
        
        label_1 = QLabel("Protein Sequence Analysis from the Protein Data Bank Database, (PDB databse can be found on NCBI website). Build by Prashik Lokhande")
        label_2 = QLabel("Select PDB file")
        
        button_1 = QPushButton("Select file", clicked = lambda: view_plot(self))     
             
        self.layout().addWidget(label_1)
        self.layout().addWidget(label_2)
        self.layout().addWidget(button_1)
        self.show()
        
        
        
def view_plot(self):
        filepath, _ = QFileDialog.getOpenFileName(self, 'select PDB file')
      
        protein = open(filepath)

        lines = protein.readlines()
        
        atom_line = []
        count = 0
        atom_count=0
        for line in lines :
            count = count+1
            if (line[0]=="A" and line[1]=="T" and line[2]=="O" and line[3]=="M"):
                atom_count = atom_count+1
                atom_line.append(line)
        
        i = 0
        x = []
        y = []
        z = []
        while (i < atom_count+1):
            atom_parameters=  str(atom_line[i]).split()
            x.append(float(atom_parameters[6]))
            y.append(float(atom_parameters[7]))
            z.append(float(atom_parameters[8]))
            i=i+1
            if i== atom_count:
                break
        
        fig = plt.figure()
        ax = Axes3D(fig)
        ax.plot(x, y, z, '.')
        plt.show()

      
        
app = QApplication([])
mw = MainWindow()

app.exec_()
        
