import pygame


class Ship:

    def __init__(self, ai_game):
        #initialisation du vaisseau et sa position de lancement
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('images\ship.bmp') #charger l'image du vaisseau et de rect
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom #debuter chaque vaisseau au centre de l'ecran en bas

    def blitme(self):
        self.screen.blit(self.image, self.rect)