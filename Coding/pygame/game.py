import pygame as pg

pg.init()

pg.display.set_caption('Beo săn mồi 😋') 

# setup the game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

FPS = pg.time.Clock()

# Load game sprites
takoyaki_sprite = pg.image.load('takoyaki.png').convert_alpha()
takoyaki_sprite = pg.transform.scale(takoyaki_sprite, (100, 100 * (350 / 339)))

x = 0
direction = 'right'
speed = 5

# Game loop
running = True
while running:
    # check when the game will quit
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    screen.fill((232, 241, 255))
    
    screen.blit(takoyaki_sprite, (x, 300))

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
                
    
    pg.display.flip()
    FPS.tick(60)
    # FPS: Frames per second

pg.quit()