# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 11:34:18 2015

@author: thorodriguez
"""

import pygame
from random import randint

pygame.init()

#couleurs
rose = (255,192,203)
jaune = (255,215,0)
orange = (255,102,0)
bleu = (102,204,255)
violet = (204,0,255)


moooodoooom
mooooooooom
mooooooooom
mooooooooom
mooooooooom
mooooooooom
mooooooooom
mooooooooom
mooooooooom
mooooooooom
mooooooooom
mooooooooom
mooooooooom
mooooooooom
mooooooooom

time.set_timer(KEYDOWN,30)
surf_hauteur = 600
surf_largeur = 480
blanc = (255,255,255)
noir = (0,0,0)

surface = pygame.display.set_mode((surf_hauteur, surf_largeur)) #taille fenetre
surface.fill(blanc)


cube = pygame.image.load('cubetetris.png')
position_cube = cube.get_rect()
surface.blit(cube, (position_cube))


pygame.display.update() #rafraichissement

pygame.display.set_caption("Jeu de Thomas et Maxime") #nom fenetre



def main ():
    game_over = False
    while (game_over == False) :  #quitter boucle inf
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
    

main()
pygame.quit()
quit()
