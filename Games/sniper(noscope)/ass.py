import pygame


PURPLE = (255, 0, 255)

class Ass():

    def __init__(self, screen):
        
        self.screen = screen
        self.image = pygame.Surface((50, 50))
        self.image.fill(PURPLE)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect ()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def output(self):
        self.screen.blit(self.image, self.rect)
