import pygame


class Player(pygame.sprite.Sprite):

    #fonction d'initialisation de la classe
    def __init__(self,):
        super().__init__()
        self.image = pygame.image.load('ressource/ressource/player_avion.png').convert_alpha()
        #recuperer la taille de l'image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0