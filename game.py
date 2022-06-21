import pygame
from player import Player

class Game():

    def __init__(self):
        #creation instance de player
        self.player = Player()
        #dictionnaire vide pour stocké les touches pressées
        self.pressed = {}
    