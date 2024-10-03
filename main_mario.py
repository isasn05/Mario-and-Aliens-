import pygame, random, oops_mario, math, time
from pygame.locals import *

width = 1000
height = 500
screen = pygame.display.set_mode([width, height])

def main():

    running = True
    keys = [False, False, False]
    pygame.init()
    mario = [500, 400]
    alienPos = [500, 250, 580, 250, 420, 250]
    white = (255, 255, 255)
    last_time = time.time()
    gameOver = False
    alienDead = pygame.image.load("pow_2_-removebg-preview.png")
    alienDeath = pygame.transform.scale(alienDead, (80, 60))
    marioDead = pygame.image.load("dead mario.jpg")
    font = pygame.font.Font("SuperMario256.ttf" , 24)
    playerOne = oops_mario.Player(mario[0], mario[1], (0, 0, 0))
    alienOne = oops_mario.Aliens(alienPos[0], alienPos[1], (0,0,0))
    alienTwo = oops_mario.Aliens(alienPos[2], alienPos[3], (0,0,0))
    alienThr = oops_mario.Aliens(alienPos[4], alienPos[5], (0,0,0))
    alienHealth = []
    alienDead = []
    for i in range(len(oops_mario.alienList)):
        alienHealth.append(oops_mario.alienList[i].health)
        alienDead.append(False)
    mousePos = pygame.mouse.get_pos()
    while running:
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
                print(mousePos)
                for i in range(len(oops_mario.alienList)):
                    checkOne = pygame.Rect.colliderect(mouses, oops_mario.alienList[i].hitbox)
                    if checkOne == True:
                        playerOne.fight(oops_mario.alienList[i])
                        alienHealth[i] = oops_mario.alienList[i].health
                        print("HIT")
                        
                        if oops_mario.alienList[i].health <= 0:
                            alienDead[i] = True
                            print("Alien is dead")
                        
        curr_time = time.time()
        delta_time = curr_time - last_time
        last_time = curr_time
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


        screen.fill((255, 255, 255))
        for j in range(len(oops_mario.alienList)):
            if oops_mario.alienList[j].health > 0:
                oops_mario.alienList[j].drawAlien(oops_mario.alienList[j].x, oops_mario.alienList[j].y)
                oops_mario.alienList[j].y += 0.25
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
            if all(health <= 0 for health in alienHealth):
                text = font.render(("You WIN?"), True, (255, 0, 0), (255, 255, 255))
                textRect = text.get_rect()
                textRect.center = (500, 250)
                screen.blit(text, textRect)
                
        playerOne.drawMario(mario[0], mario[1])
        mouses = pygame.draw.rect(screen, (245, 245, 245), Rect((mousePos), (20, 20)))
        


        pygame.display.flip()
        
    pygame.quit()
    
main()
            




