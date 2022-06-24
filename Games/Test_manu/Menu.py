from turtle import width
import pygame
import pygame_menu


WIDTH = 1280
HEIGHT = 700

pygame.init()
surface = pygame.display.set_mode((WIDTH, HEIGHT))

def set_difficulty(value, difficulty):
    # Do the job here !
    pass

def start_the_game():
    # Do the job here !
    pass

menu = pygame_menu.Menu('Welcome', WIDTH, HEIGHT, theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Name :', default='TheSawe')
menu.add.selector('Difficulty :', [('Hard', 2), ('Easy', 1)], onchange=set_difficulty)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(surface)