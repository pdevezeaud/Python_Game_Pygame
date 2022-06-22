import pygame
from player import Player
from game import Game
pygame.init()

#Gestion du Frame/image
clock = pygame.time.Clock()

pygame.display.set_caption("Arcane Game")
screen = pygame.display.set_mode((400,600))

#CHARGEMENT IMAGE DE FOND
background = pygame.image.load('ressource/ressource/fond.jpg')

#creation instance de game (qui lance player)
game = Game()

#initialisation du background et de son positionnement en y
y_background = 0


#boucle d'animation
running = True
while running:


    #Defilement fond ecran en y
    y_background += 0.5

    #Defilement fond ecran en x
    x_background = int(-0.66 * game.player.rect.x)

    if y_background < 619:
        screen.blit(background,(x_background,int(y_background)))
        screen.blit(background,(x_background,int(y_background - 619)))
    else:
        y_background = 0
        screen.blit(background,int(x_background,int(y_background)))
        
    screen.blit(game.player.image,game.player.rect)
    #print(player.rect)

    #information sur le framerate
    clock.tick(60)
    #print(f"{clock.get_fps()} FPS")



    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # sinon si une autre toche est présse je la stocke
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
    
    #print(game.pressed)
    # si la touche droit est pressé et que le player + ajout de la taille player est plus petit que la taille ecran alors à droite

    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    
    if game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()