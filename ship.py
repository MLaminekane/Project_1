import pygame


class Ship:

    def __init__(self, ai_game):
        #initialisation du vaisseau et sa position de lancement
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('images\ship.bmp') #charger l'image du vaisseau et de rect
        self.rect = self.image.get_rect() #permet de placer le navire dans la bonne position
        self.rect.midbottom = self.screen_rect.midbottom #debuter chaque vaisseau au centre de l'ecran en bas
        self.moving_right = False
        self.moving_left = False
        self.x = float(self.rect.x)
    
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right: 
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)
    
  