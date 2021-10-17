import pygame, sys, random
from pygame.locals import *

clock = pygame.time.Clock()

pygame.init()

pygame.display.set_caption('Bounce or Die in Space')

WINDOW_SIZE = (600, 400)

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

scaleUp_display = pygame.Surface((300, 200))


player_image = pygame.image.load('player1.png')
fuel_image = pygame.image.load('energy_orb.png')

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

player_loc = [138, 60]

player_falling_momentum = 0

player_air_time = 0

power = 120

player_rect = pygame.Rect(player_loc[0], player_loc[1], player_image.get_width(), player_image.get_height())

fuel_loc = [random.randint(0, 284), random.randint(0, 184)]

'''
def main_menu():

    while True:
        scaleUp_display.fill((255, 10, 100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_p:
                    game()
                    break
    
        surface = pygame.transform.scale(scaleUp_display, WINDOW_SIZE)
        screen.blit(surface, (0, 0))
        pygame.display.update()
        clock.tick(60)
'''

while True:
        
        scaleUp_display.fill((255, 190, 100))

        if power <= 10:
            print("GAME OVER!!!!")
        
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
        
        #Collision with the orb
        if fuel.test_collision(player_rect):
            power += 20
            fuel_loc = [random.randint(0, 284), random.randint(0, 184)]

        fuel.render(scaleUp_display) #displaying the orb


        scaleUp_display.blit(player_image, (player_loc[0], player_loc[1])) #drawing the player




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    moving_right = True
                if event.key == K_LEFT:
                    moving_left = True
                if event.key == K_UP:
                    if player_loc[1] > 2 and player_air_time > 10 and power > 10:
                        player_air_time = 0
                        power -= 10
                        player_falling_momentum += -6
                        print(power)
            if event.type == KEYUP:
                if event.key == K_RIGHT:
                    moving_right = False
                if event.key == K_LEFT:
                    moving_left = False
                


        surface = pygame.transform.scale(scaleUp_display, WINDOW_SIZE)
        screen.blit(surface, (0, 0))
        pygame.display.update()
        clock.tick(60)