# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 11:34:18 2015

@author: thorodriguez
"""

import pygame

pygame.init()

surf_hauteur = 1208
surf_largeur = 986

surface = pygame.display.set_mode((surf_hauteur, surf_largeur)) #taille fenetre
pygame.display.set_caption("Jeu de Thomas et Maxime") #nom fenetre


def fenetre_principale():
    
    fond = pygame.image.load("fondtetris.jpg").convert

    game_over = False
    while (game_over == False) : 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
    pygame.quit()
    quit()

fenetre_principale()