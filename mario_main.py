#isabella Sanglade, Abigail Andre
#06/13/2023
#Spaceeee MARIO!

import pygame, random, NewPlanets, time, oops_mario, math
from pygame.locals import *
from pygame import mixer

width = 1000
height = 500
screen = pygame.display.set_mode([width, height])

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
    # mario addition
    keys = [False, False, False]
    mario = [500, 400]
    alienPos = [500, 0, 580, 0, 420, 0]
    white = (255, 255, 255)
    gameOver = False
    alienDead = pygame.image.load("pow_2_-removebg-preview.png")
    alienDeath = pygame.transform.scale(alienDead, (80, 60))
    marioDead = pygame.image.load("dead mario.jpg")
    font = pygame.font.Font("SuperMario256.ttf" , 24)
    deathSound = pygame.mixer.Sound("deadLoser.mp3")
    winSound = pygame.mixer.Sound("youWin.mp3")
    themeSound = pygame.mixer.Sound("SuperMarioBros.mp3")
    playerOne = oops_mario.Player(mario[0], mario[1], (0, 0, 0))
    alienOne = oops_mario.Aliens(alienPos[0], -100, (0,0,0))
    alienTwo = oops_mario.Aliens(alienPos[2], -100, (0,0,0))
    alienThr = oops_mario.Aliens(alienPos[4], -100, (0,0,0))
    WeakalienOne = oops_mario.WeakAlien(alienPos[0], alienPos[1], (0,0,0))
    WeakalienTwo = oops_mario.WeakAlien(alienPos[2], alienPos[3], (0,0,0))
    WeakalienThr = oops_mario.WeakAlien(alienPos[4], alienPos[5], (0,0,0))
    BadalienOne = oops_mario.Aliens(alienPos[0], -600, (0,0,0))
    BadalienTwo = oops_mario.Aliens(alienPos[2], -600, (0,0,0))
    BadalienThr = oops_mario.Aliens(alienPos[4], -600, (0,0,0))
    BadalienFor = oops_mario.Aliens(alienPos[0], -600, (0,0,0))
    BadalienFiv = oops_mario.Aliens(alienPos[2], -680, (0,0,0))
    BadalienSix = oops_mario.Aliens(alienPos[4], -680, (0,0,0))
    BadalienSev = oops_mario.Aliens(alienPos[0], -680, (0,0,0))
    BadalienEig = oops_mario.Aliens(alienPos[2], -760, (0,0,0))
    BadalienNin = oops_mario.Aliens(alienPos[4], -760, (0,0,0))
    BadalienTen = oops_mario.Aliens(alienPos[0], -760, (0,0,0))

    bigBoss = oops_mario.PeachAlien(500, -550, (0,0,0))
    alienHealth = []
    alienDead = []
    for i in range(len(oops_mario.alienList)):
        alienHealth.append(oops_mario.alienList[i].health)
        alienDead.append(False)
    mousePos = pygame.mouse.get_pos()
    game_state = 1
    last_time = time.time()
    planets = []
    width = 1000
    height = 500
    color = (0,0,0)
    score = 0
    pygame.display.set_mode((width,height))
    screen = pygame.display.set_mode([width,height])
    background = SpriteImage( width, height, 0, 0, color, "actual_space_background.jpg",screen)
    background = pygame.image.load("actual_space_background.jpg")
    backgrounReSize = pygame.transform.scale(background, (width, height))
    for i in range (20):
        yLocRect = random.randint(10,450)
        rectSize = random.randint(25, 275)
        planets.append(NewPlanets.NewPlanets(500 + i * random.randint(50,2000), yLocRect , rectSize ))
    
    themeSound.play()
    while running == True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    keys[0] = True
                if event.key == pygame.K_a:
                    keys[1] = True
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    keys[0] = False
                if event.key == pygame.K_a:
                    keys[1] = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                #print(mousePos)
                for i in range(len(oops_mario.alienList)):
                    checkOne = pygame.Rect.colliderect(mouses, oops_mario.alienList[i].hitbox)
                    if checkOne == True:
                        playerOne.fight(oops_mario.alienList[i])
                        alienHealth[i] = oops_mario.alienList[i].health
                        #print("HIT")
                            
                        if oops_mario.alienList[i].health <= 0:
                            alienDead[i] = True
                            #print("Alien is dead")
        screen.blit(backgrounReSize, (0, 0))
        #time
        curr_time = time.time()
        delta_time = curr_time - last_time
        last_time = curr_time
        #mario add again
        if keys[0] == True:
            mario[0] += 1
            playerOne.update(mario[0])
        if keys[1] == True:
            mario[0] -= 1
            playerOne.update(mario[0])

        for o in range(len(oops_mario.alienList)):
            if oops_mario.alienList[o].y >= 440:
                oops_mario.alienList[o].y = 440
                gameOver = True
        if  all(alienDead):
            gameOver = True

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
        for j in range(len(oops_mario.alienList)):
            if oops_mario.alienList[j].health > 0:
                oops_mario.alienList[j].drawAlien(oops_mario.alienList[j].x, oops_mario.alienList[j].y)
                oops_mario.alienList[j].y += 1.9
                oops_mario.alienList[j].updateY(oops_mario.alienList[j].y)
                oops_mario.alienList[j].updateX(oops_mario.alienList[j].x)
            else:
                screen.blit(alienDeath, (oops_mario.alienList[j].x, oops_mario.alienList[j].y))
        if gameOver == True:
            for i in range(len(oops_mario.alienList)):
                if (oops_mario.alienList[i].y >= 440):
                    text = font.render(("Gameover You Lose"), True, (255, 0, 0), (255, 255, 255))
                    textRect = text.get_rect()
                    textRect.center = (500, 250)
                    screen.blit(text, textRect)
                    themeSound.stop()
                    deathSound.play()
            if all((health <= 0 for health in alienHealth)):
                text = font.render(("You WIN?"), True, (255, 0, 0), (255, 255, 255))
                textRect = text.get_rect()
                textRect.center = (500, 250)
                screen.blit(text, textRect)
                themeSound.stop()
                winSound.play()
        playerOne.drawMario(mario[0], mario[1])
        mouses = pygame.draw.rect(screen, (245, 245, 245), Rect((mousePos), (20, 20)))

        
                    
        pygame.display.flip()
    pygame.quit()

#calling lol
main()
