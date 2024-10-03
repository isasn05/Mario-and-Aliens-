#Isabella Sanglade
#6/14/2023
#Planets

import pygame, random

class Planets:
    """def __init__(self, x):
        self.x = x
        self.y = y
        self.hitbox = pygame.Rect(self.x, self.y, 50, 50)
        self.color = (0, 255, 0)
        self.alive = True
        self.time = .25
    def update(self, delta_time, speed):
        self.x -= speed * delta_time
        self.hitbox.x = self.x
    if self.x < -50:
        self.alive = False
        self.time -= delta_time
    if (self.time < 0):"""
    def __init__(self, x):
        self.alive = True
        self.type = random.randint(0, 1)
        self.x = x
        if self.type == 0:
            self.y = 450
            self.r = random.randint(100, 300)
        if self.type == 1:
            self.y = random.randint(-10, 400)
            self.width = random.randint(10, 150)
            self.height = 450 - self.y
""" number = random.randint(1, 12)
    if pictureNum == 1:
            name = ""
    elif pictureNum == 2:
            name = ""
    elif pictureNum == 3:
            name = ""
    elif pictureNum == 4:
            name = ""
    elif pictureNum == 5:
            name = ""
    elif pictureNum == 6:
            name = ""
    elif pictureNum == 7:
            name = ""
    elif pictureNum == 8:
            name = ""
    elif pictureNum == 9:
            name = ""
    elif pictureNum == 10:
            name = ""
    elif pictureNum == 11:
            name = ""
    elif pictureNum == 12:
            name = ""
self.time = .25"""

"""def reset(self, last_box):
    self.x = last_box.x + 50
    self.hitbox.x = self.x
    self.alive = True"""
def update(self, delta_time, speed):
    self.x -= speed *.5 * delta_time
    if (self.type == 0):
        if self.x < -self.r:
            self.alive = False
    if (self.type == 1):
        if (self.x < -self.width):
            self.alive = False
def draw(self, screen):
    pygame.draw.rect(screen, self.color1, (self.x, self.y, self.width,
self.height))

