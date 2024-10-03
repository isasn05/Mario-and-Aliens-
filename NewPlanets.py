#Isabella Sanglade, Abigail Andre
#9/15/2023
#NewPlanets
import pygame, random

class NewPlanets:
    def __init__(self, x, y, size):
        self.alive = True
        self.x = x
        self.y = y
        self.width = random.randint(10, 150)
        self.image = pygame.image.load(NewPlanets.typePicture())
        self.size = random.randint(25, 350)
        self.image = pygame.transform.scale(self.image,(size,size))
        self.hitbox = pygame.Rect(self.x, self.y, size, size)
        self.dx = 2
        #print(name)
    def update(self, delta_time, speed):
        self.x -= speed *.5 * delta_time
        if (self.x < -self.width):
            self.alive = False
        self.hitbox.x = self.x
    def draw(self, screen):
        
        screen.blit(self.image, self.hitbox)
        
        
    def typePicture():
        pictureNum = random.randint(1,12)
        if pictureNum == 1:
            name = "planet_Mercury-removebg-preview (1).png"
        elif pictureNum == 2:
            name = "planets_Comet-removebg-preview.png"
        elif pictureNum == 3:
            name = "planets_earth-removebg-preview.png"
        elif pictureNum == 4:
            name = "planets_Jupiter-removebg-preview.png"
        elif pictureNum == 5:
            name = "planets_Mars-removebg-preview.png"
        elif pictureNum == 6:
            name = "planets_Moon-removebg-preview.png"
        elif pictureNum == 7:
            name = "planets_Neptun-removebg-preview.png"
        elif pictureNum == 8:
            name = "planets_Pluto-removebg-preview.png"
        elif pictureNum == 9:
            name = "planets_Saturn-removebg-preview.png"
        elif pictureNum == 10:
            name = "planets_Sun-removebg-preview.png"
        elif pictureNum == 11:
            name = "planets_Uranus-removebg-preview.png"
        elif pictureNum == 12:
            name = "planets_Venus-removebg-preview.png"

        return name
        
