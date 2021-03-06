import sys
import pygame
from settings import Settings 
from ship import Ship


class AlienInvasion:

    def __init__(self):
        pygame.init() #initialisation du jeu et des ressources
        pygame.display.set_caption("Alien Invasion")
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        self.ship = Ship(self)

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()

    def _check_events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        

    def _update_screen(self):
            self.screen.fill(self.settings.bg_color) #remettre la couleur bg de l'ecran a chaque passage dans ce boucle
            self.ship.blitme()

            pygame.display.flip() #rendre visible l'ecran le plus recent
    
        

if __name__ == "__main__": #creation des instances et lancement du jeu
    ai = AlienInvasion()
    ai.run_game()
