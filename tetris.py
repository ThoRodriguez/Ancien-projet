# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 11:34:18 2015

@author: thorodriguez
"""

import tkinter as tk


def lancement_jeu(monjeu):

    BoutonLancer = tk.Button(monjeu, text ='Lancer le jeu', \
    command = lancement_jeu)
    BoutonLancer.pack(padx = 5, pady = 5)

    BoutonQuitter = tk.Button(monjeu, text ='Quitter', command = monjeu.destroy)
    BoutonQuitter.pack(padx = 5, pady = 5)

def main():
    monjeu = tk()     #probleme : TypeError: 'module' object is not callable
    monjeu.title('Tetris de Thomas et Maxime')
    monjeu.geometry()
    lancement_jeu(monjeu)


main()
