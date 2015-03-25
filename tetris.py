# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 11:34:18 2015

@author: thorodriguez
"""
from tkinter import *

# Création de la fenêtre principale (main window)
Monjeu = Tk()
Monjeu.title('Tetris de Thomas et Maxime')
Monjeu.geometry('1500x1000')
photo = PhotoImage(file="fondtetris.gif")
print(photo)

def grille():
    case = 0
    ligne = []
    colonne = []
    for i in range (10):
        ligne.append(case)
        for i in range (14):
            colonne.append(case), end="\n"
    print(colonne)
grille()