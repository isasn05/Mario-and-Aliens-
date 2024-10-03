#isabella Sanglade, Abigail Andre
#06/13/2023
#Spaceeee MARIO!

import pygame, random, NewPlanets, time, oops_mario
from pygame.locals import *

class SpriteImage(pygame.sprite.Sprite):
    def __init__(self, width, height, xPos, yPos, color, picture, screen):
        super().__init__()
        width = 1000
        height = 500
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = [xPos, yPos]
        self.image = pygame.image.load(picture)
        self.rect = self.image.get_rect()
        self.rect.center = [xPos, yPos]
        background = pygame.image.load("actual_space_background.jpg")
        screen.blit(background, (0, 0))

def main():
    pygame.init()
    running = True
    last_time = time.time()
    planets = []
    width = 1000
    height = 500
    color = (0,0,0)
    pygame.display.set_mode((width,height))
    screen = pygame.display.set_mode([width,height])
    background = SpriteImage( width, height, 0, 0, color, "actual_space_background.jpg",screen)
    background = pygame.image.load("actual_space_background.jpg")
    backgrounReSize = pygame.transform.scale(background, (width, height))
    for i in range (20):
        yLocRect = random.randint(10,450)
        rectSize = random.randint(25, 275)
        planets.append(NewPlanets.NewPlanets(500 + i * random.randint(50,2000), yLocRect , rectSize ))
    

    while running == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(backgrounReSize, (0, 0))
        #time
        curr_time = time.time()
        delta_time = curr_time - last_time
        last_time = curr_time
        #update
        speed = 200
        for b in planets:
            b.update(delta_time, speed)
        for i in range(len(planets)-1, -1, -1):
            if (planets[i].alive == False):
                planets.pop(i)
                yLocRect = random.randint(25,475)
                planets.append(NewPlanets.NewPlanets(1100 + random.randint(0,400), yLocRect, rectSize ))
        for b in planets:
            b.draw(screen)
                
        pygame.display.flip()
    pygame.quit()

#calling lol
main()
