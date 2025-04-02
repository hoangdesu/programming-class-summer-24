import pygame as pg

pg.init()

# setup the game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

while True:

    screen.fill((209, 13, 58))
    
    pg.display.flip()
    

