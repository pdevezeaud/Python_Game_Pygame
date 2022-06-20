import pygame
from player import Player
pygame.init()

pygame.display.set_caption("Arcane Game")
screen = pygame.display.set_mode((400,600))

#CHARGEMENT IMAGE DE FOND
background = pygame.image.load('ressource/ressource/fond.jpg').convert()

#creation instance de player
player = Player()

#boucle d'animation
running = True
while running:

    screen.blit(background,(-109,0))
    screen.blit(player.image,player.rect)
    print(player.rect)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()