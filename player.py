import pygame


class Player(pygame.sprite.Sprite):

    #fonction d'initialisation de la classe
    def __init__(self,):
        super().__init__()
        self.image = pygame.image.load('ressource/ressource/player_avion2.png').convert_alpha()
        #recuperer la taille de l'image
        self.rect = self.image.get_rect()
        self.rect.x = 150
        self.rect.y = 520
        self.velocity = 5

    #deplacement
    def move_right(self):
        self.rect.x += self.velocity
    
    def move_left(self):
        self.rect.x -= self.velocity