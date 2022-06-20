import pygame
from player import Player
pygame.init()

#Gestion du Frame/image
clock = pygame.time.Clock()

pygame.display.set_caption("Arcane Game")
screen = pygame.display.set_mode((400,600))

#CHARGEMENT IMAGE DE FOND
background = pygame.image.load('ressource/ressource/fond.jpg').convert()

#creation instance de player
player = Player()

#initialisation du background et de son positionnement en y
y_background = 0


#boucle d'animation
running = True
while running:
    #Defilement fond ecran

    y_background += 1
    if y_background < 619:
        screen.blit(background,(-109,y_background))
        screen.blit(background,(-109,y_background - 619))
    else:
        y_background = 0
        screen.blit(background,(-109,y_background))
        
    screen.blit(player.image,player.rect)
    #print(player.rect)

    #information sur le framerate
    clock.tick(60)
    print(f"{clock.get_fps()} FPS")



    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()