# Abigail Andre, Isabella Sanglade
# 06-13/23
# Python 2
# Space Mario with other aliens

import pygame
import random
from pygame.locals import *
global alienList
alienList  = []
global width
width = 1000
global height
height = 500
global screen
screen = pygame.display.set_mode([width, height])
               
class Aliens:
    
    def __init__(self, xPos, yPos, color):
        self.x = xPos
        self.y = yPos
        self.color = color
        self.size = 20
        self.health = 150
        #self.defense = 100
        self.damage = 15
        self.hitbox = pygame.Rect(self.x, self.y, 100, 80)
        #self.alienIOne = pygame.image.load(sprite)
        alienList.append(self)

    def fightt(self, player):
        player.health -= self.damage

                
    def updateX(self, movement):
        self.x = movement
        self.hitbox.update(self.x, self.y, 80, 60)
    def updateY(self, movement):
        self.y = movement
        self.hitbox.update(self.x, self.y, 80, 60)
        
    def drawAlien(self, x, y):
        alienIOne = pygame.image.load("shroob(1).png")
        alienIoneSize = pygame.transform.scale(alienIOne, (80, 60))
        screen.blit(alienIoneSize, (self.x, self.y))

class WeakAlien(Aliens):
    def __init__(self,  xPos, yPos, color):
        self.x = xPos
        self.y = yPos
        self.color = color
        self.size = 15
        self.health = 50
        #self.defense = 100
        self.damage = 10
        self.hitbox = pygame.Rect(self.x, self.y, 100, 80)
        alienList.append(self)
    def fightt(self, player):
        player.health -= self.damage      
    def updateX(self, movement):
        self.x = movement
        self.hitbox.update(self.x, self.y, 80, 60)
    def updateY(self, movement):
        self.y = movement
        self.hitbox.update(self.x, self.y, 80, 60)
    def drawAlien(self, x, y):
        #super().drawAlien()
        alienIOne = pygame.image.load("weakAlien.png")
        alienIoneSize = pygame.transform.scale(alienIOne, (80, 60))
        screen.blit(alienIoneSize, (self.x, self.y))
        
class PeachAlien(Aliens):
    def __init__(self,  xPos, yPos, color):
        self.x = xPos
        self.y = yPos
        self.color = color
        self.size = 30
        self.health = 1000
        self.damage = 25
        self.hitbox = pygame.Rect(self.x, self.y, 201, 250)
        alienList.append(self)
    def fightt(self, player):
        player.health -= self.damage
    def updateX(self, movement):
        self.x = movement
        self.hitbox.update(self.x, self.y, 201, 250)
    def updateY(self, movement):
        self.y = movement
        self.hitbox.update(self.x, self.y, 201, 250)
        
    def drawAlien(self, x, y):
        alienIOne = pygame.image.load("Aliens_Peach.png")
        alienIoneSize = pygame.transform.scale(alienIOne, (201, 250))
        screen.blit(alienIoneSize, (self.x, self.y))
                    

#Playerrrrrr!!!!!!!!!!!!
class Player:

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.size = 10
        self.health = 100
        self.powerUp = False
        self.damage = 50
        self.hitbox = pygame.Rect(self.x, self.y, 120, 100)
        self.dy = 0
        
    def powersUp(self, powerUp):
        if self.powerUp:
            while self.powerUp:
                self.size = 20
                self.health = 100
                self.damage = 100 
        self.size = 10
        self.defense = 100
        
    def fight(self, alien):
        alien.health -= self.damage
        
    def takeDamage(self):
        self.health -= Alien.damage

    def gameOver(self):
        if self.health <= 0:
            self.x = 500
            self.y = 250

    def update(self, movement):
        self.x = movement
        self.hitbox.update(self.x, self.y, 120, 100)
        
    def drawMario(self, x, y):
        marioOne = pygame.image.load("baby_mario(1).png")
        marioOneResize = pygame.transform.scale(marioOne, (120, 100))
        screen.blit(marioOneResize, (self.x, self.y))
        






    


    


