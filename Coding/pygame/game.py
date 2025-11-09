import pygame as pg
import random

pg.init()
pg.font.init()
pg.mixer.init()

pg.display.set_caption('Beo săn mồi 😋') 

# setup the game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

FPS = pg.time.Clock()

# Load game sprites
beo_sprite = pg.image.load('beo.png').convert_alpha()
beo_sprite = pg.transform.scale(beo_sprite, (100, 100))

beo_x = 400
beo_y = 300
direction = 'right'
speed = 8

takoyaki_sprite = pg.image.load('takoyaki.png').convert_alpha()
takoyaki_sprite = pg.transform.scale(takoyaki_sprite, (80, 80 * (350 / 339)))

tako_x = random.randint(10, 900)
tako_y = random.randint(10, 700)

# Bomb
bomb_sprite = pg.image.load('bomb.png').convert_alpha()
bomb_sprite = pg.transform.scale(bomb_sprite, (80, 80 * (350 / 339)))
bomb_x = random.randint(10, 900)
bomb_y = random.randint(10, 700)
# bomb_x = 700
# bomb_y = 100
bomb_speed = 5

# Changes in velocity (directions)
bomb_dx = bomb_speed if random.randint(0, 1) == 1 else -bomb_speed
bomb_dy = bomb_speed if random.randint(0, 1) == 1 else -bomb_speed

score = 1
my_font = pg.font.SysFont('Comic Sans MS', 30)
score_box = my_font.render(f'Score: {score}', False, (0, 0, 0))

nom_sound = pg.mixer.Sound('nom.mp3')
nom_sound.set_volume(0.8) # 0 (0%) -> 1.0 (100%)

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
    
    screen.blit(bomb_sprite, (bomb_x, bomb_y))
    
    screen.blit(beo_sprite, (beo_x, beo_y))
    
    screen.blit(score_box, (SCREEN_WIDTH - score_box.get_width() - 20, 20))


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
            beo_x += speed
    elif key_pressed[pg.K_LEFT]:
        # if y <= SCREEN_HEIGHT - circle_radius:
            beo_x -= speed
    
    if key_pressed[pg.K_UP]:
        # if y >= circle_radius:
            beo_y -= speed
    elif key_pressed[pg.K_DOWN]:
        # if y <= SCREEN_HEIGHT - circle_radius:
            beo_y += speed

    
    # axis-aligned bounding boxes (AABB)
    # Collision detection between the character and the food
    
    if (
        beo_x < tako_x + takoyaki_sprite.get_width() and
        beo_x + beo_sprite.get_width() > tako_x and
        beo_y < tako_y + takoyaki_sprite.get_height() and
        beo_y + beo_sprite.get_height() > tako_y):

        print('NOM NOM NOM', score)
        score += 1
        score_box = my_font.render(f'Score: {score}', False, (0, 0, 0))
        
        nom_sound.play()
        
        tako_x = random.randint(10, 900)
        tako_y = random.randint(10, 700)
        
        print(bomb_speed)
        
    # Move the bomb automatically
    if bomb_x > SCREEN_WIDTH - bomb_sprite.get_width():
        bomb_dx = -bomb_dx
    elif bomb_y > SCREEN_HEIGHT - bomb_sprite.get_height():
        bomb_dy = -bomb_dy
    elif bomb_x < 0:
        bomb_dx = -bomb_dx
    elif bomb_y < 0:
        bomb_dy = -bomb_dy

    bomb_x += bomb_dx
    bomb_y += bomb_dy

    if (
        beo_x < bomb_x + bomb_sprite.get_width() and
        beo_x + beo_sprite.get_width() > bomb_x and
        beo_y < bomb_y + bomb_sprite.get_height() and
        beo_y + beo_sprite.get_height() > bomb_y):
        
        score -= 1
        score_box = my_font.render(f'Score: {score}', False, (0, 0, 0))
        
    
    pg.display.flip()
    FPS.tick(60)
    # FPS: Frames per second

pg.quit()
