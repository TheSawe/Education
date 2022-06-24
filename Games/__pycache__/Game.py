import pygame
import sys
from ass import Ass


BLUE = (0, 255, 255)

def run():

    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption('Sniper(noscope)')
    bg_color = (BLUE)
    ass = Ass(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(bg_color)
        ass.output()
        pygame.display.flip()
run()