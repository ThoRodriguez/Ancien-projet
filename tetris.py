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
surf_largeur = 843


fenetre = pygame.display.set_mode((surf_hauteur, surf_largeur)) #taille fenetre
fenetre.fill(blanc)

fond = pygame.image.load("fondtetris.png")
cube = pygame.image.load('cubetetris.png')
pygame.display.set_caption("Jeu de Thomas et Maxime") #nom fenetre
carre = pygame.Surface((64,64))
carre.fill(blanc)


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
    
def affichage(zone):
    x = 32
    for i in zone:
        y = 50
        for j in i:
            if j == 1:
                fenetre.blit(carre, (x, y))
            y += 65
        x += 65
            
def bouge_carre(zone):
    x = 65
    carre.fill(bleu)
    fenetre.blit(carre,(200,200))
    continuer = True
    while continuer:
        for event in pygame.event.get():   
            if event.type == pygame.K_ESCAPE:   
                continuer = False
            elif event.type == pygame.K_LEFT:
                fenetre.blit(carre, (200-x,200))
            elif event.type == pygame.K_RIGHT:
                fenetre.blit(carre, (200+x,200))
            elif event.type == pygame.K_DOWN:
                fenetre.blit(carre, (200,200-x))
    #probleme : evenements non gerés et bug boucle while
    


def main ():
    x = surf_hauteur//2
    y = 0
    zone = crea_zone()
    game_over = False
    while (game_over == False) :  #quitter boucle inf
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    fenetre.blit(carre,(x, y-64))
            
        fenetre.blit(fond, (0, 0))
        affichage(zone)
        #bouge_carre(zone)
        pygame.display.update() #rafraichissement
main()
pygame.quit()
quit()
