from pyexpat.errors import XML_ERROR_SUSPENDED
import pygame
from Player import Player




class Ball:

    ###class vars
    size = 10
    xSpeed = 10
    ySpeed = 10

    topBound = 0
    bottomBound = 0
    leftBound = 0
    rightBound = 0

    #constructor function
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

    #render function
    def render(self, aSurface):
        #Drawing Ball
        pygame.draw.circle(aSurface, (255, 255, 255), [self.x, self.y], self.size)

    #move the ball
    def move(self):
        self.x = self.x + self.xSpeed
        self.y = self.y + self.ySpeed

    #detect when the ball hits the wall
    def wallDetect(self):
        if self.y <= 0:
            self.ySpeed = abs(self.ySpeed)
        elif self.y >= 600:
            self.ySpeed = self.ySpeed * -1 

        if self.x <= 0:
            self.xSpeed = abs(self.xSpeed)
        elif self.x >= 800:
            self.xSpeed = self.xSpeed * -1

    ##boundaries for ball
    def updateBounds(self):
        self.topBound = self.y - self.size
        self.bottomBound = self.y + self.size
        self.leftBound = self.x - self.size
        self.rightBound = self.x + self.size

        ##collision detection for ball and player
    def collide(self, aPlayer):
        if (self.topBound < aPlayer.bottomBound):
            if (self.bottomBound > aPlayer.topBound):
                if (self.rightBound > aPlayer.leftBound):
                    if(self.leftBound < aPlayer.rightBound):
                        if self.y >= 400:
                            self.ySpeed = -abs(self.ySpeed) 

                        elif self.y < 400:
                            self.ySpeed = abs(self.ySpeed)



