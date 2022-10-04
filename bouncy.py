import pygame, sys, random
from pygame.locals import *

clock = pygame.time.Clock()

pygame.init()

pygame.mixer.pre_init(44100, -16, 2, 512)

pygame.display.set_caption('Bounce or Die in Space')

WINDOW_SIZE = (600, 400)

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

scaleUp_display = pygame.Surface((300, 200))

font = pygame.font.SysFont(None, 15)

pygame.mixer.music.load('soundtrack.wav')
pygame.mixer.music.play(-1)

#load in sounds
bounce_sound = pygame.mixer.Sound('bounce_sound.wav')
coin_sound = pygame.mixer.Sound('coin_sound.wav')
fuel_sound = pygame.mixer.Sound('fuel_sound.wav')

global sfx_v
sfx_v = 0.7

bounce_sound.set_volume(1)
coin_sound.set_volume(1)
fuel_sound.set_volume(1)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def draw_end_screen():
    textobj = font.render('GAME OVER', 1, (255, 0, 0))
    textrect = textobj.get_rect()
    textrect.center = (150, 80)
    scaleUp_display.blit(textobj, textrect)


def end_screen():

    death_sound = pygame.mixer.Sound('death_sound.wav')
    death_sound.set_volume(0.8)
    death_sound.play()

    selected = "start"

    global score

    while True:
        scaleUp_display.fill((0, 0, 0))

        draw_end_screen()
        
        button_1 = pygame.Rect(125, 100, 60, 10)
        button_2 = pygame.Rect(125, 130, 60, 10)

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_UP or event.key == K_w:
                    selected = "start"
                elif event.key == K_DOWN or event.key == K_s:
                    selected = "quit"
                if event.key == K_RETURN:
                    if selected == "start":
                        print("Play again")
                        death_sound.set_volume(0)
                        game()
                    if selected == "quit":
                        pygame.quit()
                        sys.exit()

        if selected == "start":
            pygame.draw.rect(scaleUp_display, (0, 215, 0), button_1)
            pygame.draw.rect(scaleUp_display, (255, 25, 0), button_2)
        elif selected == "quit":
            pygame.draw.rect(scaleUp_display, (255, 25, 0), button_1)
            pygame.draw.rect(scaleUp_display, (0, 215, 0), button_2)

        draw_text('Play again', font, (255, 255, 255), scaleUp_display, 125, 100)
        draw_text('Quit', font, (255, 255, 255), scaleUp_display, 125, 130)
        draw_text('Score ', font, (255, 255, 255), scaleUp_display, 125, 160)
        draw_text(str(score), font, (255, 255, 255), scaleUp_display, 160, 160)

        surface = pygame.transform.scale(scaleUp_display, WINDOW_SIZE)
        screen.blit(surface, (0, 0))
        pygame.display.update()
        clock.tick(60)


def options():
    
    selected = 'music'
    button_number = 1

    button_1 = pygame.Rect(30, 60, 70, 15)
    button_2 = pygame.Rect(30, 90, 70, 15)
    button_3 = pygame.Rect(30, 120, 70, 15)
    button_4 = pygame.Rect(30, 150, 60, 15)

    global sfx_v

    while True:

        scaleUp_display.fill((66, 160, 215))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    if button_number == 1:
                        selected = 'music'
                    elif button_number == 2:
                        button_number = 1
                        selected = 'music'
                    elif button_number == 3:
                        button_number = 2
                        selected = 'sfx'
                    elif button_number == 4:
                        button_number = 3
                        selected = 'resolution'
                elif event.key == K_DOWN:
                    if button_number == 1:
                        button_number = 2
                        selected = 'sfx'
                    elif button_number == 2:
                        button_number = 3
                        selected = 'resolution'
                    elif button_number == 3:
                        button_number = 4
                        selected = 'back'
                if event.key == K_RIGHT:
                    if selected == 'music':
                        pass
                    elif selected == 'sfx' and sfx_v < 1:
                        if sfx_v >= -0.1:
                            sfx_v += 0.1
                            print(sfx_v)
                            #bounce_sound.set_volume(sfx_vol)
                            #coin_sound.set_volume(sfx_vol)
                            #fuel_sound.set_volume(sfx_vol)
                if event.key == K_LEFT:
                    if selected == 'music':
                        pass
                    elif selected == 'sfx' and sfx_v <= 1:
                        if sfx_v > -0:
                            sfx_v -= 0.1
                            print(sfx_v)
                            #bounce_sound.set_volume(sfx_vol)
                            #coin_sound.set_volume(sfx_vol)
                            #fuel_sound.set_volume(sfx_vol)
                if event.key == K_RETURN:
                    if selected == 'back':
                        print('main_meniu')
                        main_menu()
                    
        if selected == 'music':
            pygame.draw.rect(scaleUp_display, (200, 200, 200), button_1)
            pygame.draw.rect(scaleUp_display, (66, 100, 245), button_2)
            pygame.draw.rect(scaleUp_display, (66, 100, 245), button_3)
            pygame.draw.rect(scaleUp_display, (66, 100, 245), button_4)
        elif selected == 'sfx':
            pygame.draw.rect(scaleUp_display, (66, 100, 245), button_1)
            pygame.draw.rect(scaleUp_display, (200, 200, 200), button_2)
            pygame.draw.rect(scaleUp_display, (66, 100, 245), button_3)
            pygame.draw.rect(scaleUp_display, (66, 100, 245), button_4)
        elif selected == 'resolution':
            pygame.draw.rect(scaleUp_display, (66, 100, 245), button_1)
            pygame.draw.rect(scaleUp_display, (66, 100, 245), button_2)
            pygame.draw.rect(scaleUp_display, (200, 200, 200), button_3)
            pygame.draw.rect(scaleUp_display, (66, 100, 245), button_4)
        elif selected == 'back':
            pygame.draw.rect(scaleUp_display, (66, 100, 245), button_1)
            pygame.draw.rect(scaleUp_display, (66, 100, 245), button_2)
            pygame.draw.rect(scaleUp_display, (66, 100, 245), button_3)
            pygame.draw.rect(scaleUp_display, (200, 200, 200), button_4)
        
        draw_text('Music volume', font, (255, 255, 255), scaleUp_display, 32, 64)
        draw_text('SFX volume', font, (255, 255, 255), scaleUp_display, 32, 92)
        draw_text('Resolution', font, (255, 255, 255), scaleUp_display, 32, 122)
        draw_text('Back', font, (255, 255, 255), scaleUp_display, 32, 152)

        surface = pygame.transform.scale(scaleUp_display, WINDOW_SIZE)
        screen.blit(surface, (0, 0))
        pygame.display.update()
        clock.tick(60)

def main_menu():


    selected = 'play'
    button_number = 1

    while True:
        scaleUp_display.fill((66, 160, 215))

        button_1 = pygame.Rect(30, 60, 80, 20)
        button_2 = pygame.Rect(30, 100, 70, 15)
        button_3 = pygame.Rect(30, 130, 70, 15)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    if button_number == 1:
                        selected = 'play'
                    elif button_number == 2:
                        button_number = 1
                        selected = 'play'
                    elif button_number == 3:
                        button_number = 2
                        selected = 'options'
                elif event.key == K_DOWN:
                    if button_number == 1:
                        button_number = 2
                        selected = 'options'
                    elif button_number == 2:
                        button_number = 3
                        selected = 'quit'
                if event.key == K_RETURN:
                    if selected == 'play':
                        print('play')
                        pygame.mixer.music.fadeout(10)
                        game()
                    elif selected == 'quit':
                        pygame.quit()
                        sys.exit()
                    elif selected == 'options':
                        print('OPTIONS')
                        options()
    
        if selected == 'play':
            pygame.draw.rect(scaleUp_display, (200, 200, 200), button_1)
            pygame.draw.rect(scaleUp_display, (66, 100, 245), button_2)
            pygame.draw.rect(scaleUp_display, (66, 100, 245), button_3)
        elif selected == 'options':
            pygame.draw.rect(scaleUp_display, (66, 100, 245), button_1)
            pygame.draw.rect(scaleUp_display, (200, 200, 200), button_2)
            pygame.draw.rect(scaleUp_display, (66, 100, 245), button_3)
        elif selected == 'quit':
            pygame.draw.rect(scaleUp_display, (66, 100, 245), button_1)
            pygame.draw.rect(scaleUp_display, (66, 100, 245), button_2)
            pygame.draw.rect(scaleUp_display, (200, 200, 200), button_3)

        draw_text('Play', font, (255, 255, 255), scaleUp_display, 32, 64)
        draw_text('Options', font, (255, 255, 255), scaleUp_display, 32, 102)
        draw_text('Quit', font, (255, 255, 255), scaleUp_display, 32, 132)

        surface = pygame.transform.scale(scaleUp_display, WINDOW_SIZE)
        screen.blit(surface, (0, 0))
        pygame.display.update()
        clock.tick(60)


def game():

    player_image = pygame.image.load('player1.png')
    fuel_image = pygame.image.load('energy_orb.png')
    coin_image = pygame.image.load('coin.png')
    background = pygame.image.load('background.png')

    moving_right = False
    moving_left = False

    class Fuel_orb():
        def __init__(self, loc):
            self.loc = loc
    
        def render(self, surface):
            surface.blit(fuel_image,(self.loc[0], self.loc[1]))

        def get_rect(self):
            return pygame.Rect(self.loc[0], self.loc[1], 16, 16)

        def test_collision(self, rect):
            orb_rect = self.get_rect()
            return orb_rect.colliderect(rect)
    
    class Coin():
        def __init__(self, loc):
            self.loc = loc
        def render(self, surface):
            surface.blit(coin_image,(self.loc[0], self.loc[1]))
        def get_rect(self):
            return pygame.Rect(self.loc[0], self.loc[1], 16, 16)
        def test_collision(self, rect):
            coin_rect = self.get_rect()
            return coin_rect.colliderect(rect)

    player_loc = [138, 60]

    player_falling_momentum = 0

    player_air_time = 0

    player_rect = pygame.Rect(player_loc[0], player_loc[1], player_image.get_width(), player_image.get_height())

    fuel_loc = [random.randint(0, 284), random.randint(0, 184)]

    coin_loc = [random.randint(0,284), random.randint(0, 184)]

    if coin_loc == fuel_loc:
        coin_loc = [random.randint(0,284), random.randint(0, 184)]

    power = 120 #120

    global score
    score = 0

    #starting music
    pygame.mixer.music.play(-1)

    #gameloop start
    while True:
        
        #scaleUp_display.fill((255, 190, 100))
        scaleUp_display.blit(background, (0, 0))

        if power < 10:
            print("GAME OVER!!!!")
            pygame.mixer.music.fadeout(10)
            end_screen()
        
        if player_loc[1] > (WINDOW_SIZE[1]/2) - player_image.get_height(): # check collision with the ground
            player_falling_momentum = -3
            player_loc[1] += player_falling_momentum
        elif player_loc[1] < 0: # Check collision with the ceiling
            player_falling_momentum = 1
            player_loc[1] += player_falling_momentum
        else:
            player_loc[1] += player_falling_momentum
            player_falling_momentum += 0.2
        if player_falling_momentum > 3:
            player_falling_momentum = 3
        
        player_air_time += 1

        #Changing sides
        if player_loc[0] > 300:
            player_loc[0] = 0
        elif player_loc[0] < -1:
            player_loc[0] = 300

        if moving_right:
            player_loc[0] += 1.5
        if moving_left:
            player_loc[0] -= 1.5

        player_rect.x = player_loc[0]
        player_rect.y = player_loc[1]

        #Creating an orb
        fuel = Fuel_orb(fuel_loc)
        #Creating a coin
        coin = Coin(coin_loc)
        
        #Collision with the orb
        if fuel.test_collision(player_rect):
            fuel_sound.play()
            power += 20
            fuel_loc = [random.randint(0, 284), random.randint(0, 184)]
        
        #Collision with the coin
        if coin.test_collision(player_rect):
            coin_sound.play()
            score += 1
            coin_loc = [random.randint(0, 284), random.randint(0, 184)]
        
        #Checking coin and fuel orb locations are not the same
        if coin_loc == (fuel_loc + [10, 10]):
            coin_loc = [random.randint(0,284), random.randint(0, 184)]

        fuel.render(scaleUp_display) #displaying the orb
        coin.render(scaleUp_display) #displaying the coin


        scaleUp_display.blit(player_image, (player_loc[0], player_loc[1])) #drawing the player
        
        #drawing fuel counter
        draw_text('FUEL', font, (255, 255, 255), scaleUp_display, 10, 10)
        draw_text(str(power), font, (255, 255, 255), scaleUp_display, 40, 10)

        #drawing score counter
        draw_text ('COINS ', font, (255, 255, 255), scaleUp_display, 220, 10)
        draw_text(str(score), font, (255, 255, 255), scaleUp_display, 255, 10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT or event.key == K_d:
                    moving_right = True
                if event.key == K_LEFT or event.key == K_a:
                    moving_left = True
                if event.key == K_UP or event.key == K_w:
                    if player_loc[1] > 2 and player_air_time >= 10 and power >= 10:
                        bounce_sound.play()
                        player_air_time = 0
                        power -= 10
                        player_falling_momentum += -6
            if event.type == KEYUP:
                if event.key == K_RIGHT or event.key == K_d:
                    moving_right = False
                if event.key == K_LEFT or event.key == K_a:
                    moving_left = False
                


        surface = pygame.transform.scale(scaleUp_display, WINDOW_SIZE)
        screen.blit(surface, (0, 0))
        pygame.display.update()
        clock.tick(60)
main_menu()