
from re import X
import pygame
#from Ball import Ball

class Player:
     
    ############## class vars with constant starting values
    width = 100
    height = 20
    speed = 10
    easing = 1
    isHit = False

    topBound = 0
    bottomBound = 0
    leftBound = 0
    rightBound = 0

    #constructor function
    def __init__(self, _x, _y):
        self.x = _x-self.width
        self.y = _y

    #render function
    def render(self, aSurface):
        playerRect = pygame.Rect(self.x, self.y, self.width, self.height)

        #Drawing Rectangle
        pygame.draw.rect(aSurface, (255,0,255),playerRect)

    #players ease towards the ball
    def ease(self, aBallX):
        self.dx = aBallX - self.x
        self.x += self.dx * self.easing
    
    ##boundaries for player
    def updateBounds(self):
        self.topBound = self.y
        self.bottomBound = self.y + self.height
        self.leftBound = self.x
        self.rightBound = self.x + self.width





