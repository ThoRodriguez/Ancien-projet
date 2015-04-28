# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
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
blanc = (255,255,255)
noir = (0,0,0)

surf_hauteur = 1208
surf_largeur = 986


fenetre = pygame.display.set_mode((surf_hauteur, surf_largeur)) #taille fenetre
fenetre.fill(blanc)

fond = pygame.image.load("fondtetris.png")
cube = pygame.image.load('cubetetris.png')
pygame.display.set_caption("Jeu de Thomas et Maxime") #nom fenetre


def crea_zone():
    zone = []
    for x in range (10):
        ligne = []
        for y in range (12):
            if y == 0 and x == 7:
                ligne.append(1)
            else: 
                ligne.append(1)
        zone.append(ligne)
    return zone
    

            

def main ():
    #x = 0
    zone = crea_zone()
    game_over = False
    while (game_over == False) :  #quitter boucle inf
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            #if event.type == pygame.KEYDOWN:
            #    if event.key == pygame.K_DOWN:
                    
            
        fenetre.blit(fond, (0, 0))
        pygame.display.update() #rafraichissement
main()
pygame.quit()
quit()