import pygame as pg
import random

pg.init()

pg.display.set_caption('Beo săn mồi 😋') 

# setup the game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

FPS = pg.time.Clock()

# Load game sprites
beo_sprite = pg.image.load('beo.png').convert_alpha()
beo_sprite = pg.transform.scale(beo_sprite, (100, 100 * (350 / 339)))

x = 400
y = 300
direction = 'right'
speed = 6


takoyaki_sprite = pg.image.load('takoyaki.png').convert_alpha()
takoyaki_sprite = pg.transform.scale(takoyaki_sprite, (80, 80 * (350 / 339)))

tako_x = random.randint(10, 900)
tako_y = random.randint(10, 700)


# Game loop
running = True
while running:
    # check when the game will quit
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            
        # test random food position
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                tako_x = random.randint(10, 900)
                tako_y = random.randint(10, 700)
    
    screen.fill((232, 241, 255))
    
    screen.blit(takoyaki_sprite, (tako_x, tako_y))
    
    screen.blit(beo_sprite, (x, y))


    # move the food left and right
    # if direction == 'right':
    #     if x <= SCREEN_WIDTH - takoyaki_sprite.get_width():
    #         x += speed
    #     else:
    #         direction = 'left'
    # elif direction == 'left':
    #     if x >= 0:
    #         x -= speed
    #     else:
    #         direction = 'right'
        
    
    # use the keyboard to move the food left and right
    key_pressed = pg.key.get_pressed()
    if key_pressed[pg.K_RIGHT]:
        # if y >= circle_radius:
            x += speed
    elif key_pressed[pg.K_LEFT]:
        # if y <= SCREEN_HEIGHT - circle_radius:
            x -= speed
    
    if key_pressed[pg.K_UP]:
        # if y >= circle_radius:
            y -= speed
    elif key_pressed[pg.K_DOWN]:
        # if y <= SCREEN_HEIGHT - circle_radius:
            y += speed
     
    
    pg.display.flip()
    FPS.tick(60)
    # FPS: Frames per second

pg.quit()