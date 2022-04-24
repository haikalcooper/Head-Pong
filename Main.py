##########
# Imports
##########
import pygame
import cv2
from Ball import Ball
from Player import Player
from PoseDetector import PoseDetector

# Define the size of the game window
WIDTH = 800
HEIGHT = 600
# make the game window object
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
# name the game window
pygame.display.set_caption("Pong with Eyes")

# frame rate of game
FPS = 60

#player vars
player1 = Player(WIDTH/2, HEIGHT - 100)
player2 = Player(WIDTH/2, 100)
ball1 = Ball(WIDTH/2, HEIGHT/2)

# main game function
def main():

     # make a hand detector
    poseDetector = PoseDetector()

    # make a clock object that will be used
    # to make the game run at a consistent framerate
    clock = pygame.time.Clock()

     # make a boolean that represents whether the game should continue to run or not
    running = True
 
    # while the opencv window is running
    # while handDetector.shouldClose == False and gameIsRunning == True
    while not poseDetector.shouldClose and running:
        # update the webcam feed and hand tracker calculations
        poseDetector.update()

	   # this makes it so this function can run at most FPS times/sec
        clock.tick(FPS)

    # for all the game events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # this gets a list of booleans showing which keys are currently pressed
        keysPressed = pygame.key.get_pressed()

         # if the leftarrow key is pressed
        if keysPressed[pygame.K_LEFT] == True and player1.x > 0:
            player1.x = player1.x - player1.speed
        
        elif keysPressed[pygame.K_RIGHT] == True and player1.x + player1.width < WIDTH:
            player1.x = player1.x + player1.speed
        if len(poseDetector.landmarkDictionary) > 0:

            if poseDetector.landmarkDictionary[6][1] < poseDetector.landmarkDictionary[3][1]:
                player1.x = player1.x - player1.speed

            elif poseDetector.landmarkDictionary[6][1] > poseDetector.landmarkDictionary[3][1]:
                player1.x = player1.x + player1.speed
            # else:
            #     handIsOpen = False
            #     circleC = (255, 0, 0)
        # This fills the game window to be the given RGB color
        WINDOW.fill((0,0,0))



        player1.render(WINDOW)
        player1.updateBounds()
        player2.render(WINDOW)
        player2.updateBounds()
        player2.ease(ball1.x)
        ball1.render(WINDOW)
        ball1.move()
        ball1.wallDetect()
        ball1.updateBounds()
        ball1.collide(player1)
        ball1.collide(player2)

        # put code here that should be run every frame
        # of your game             
        pygame.display.update() 

    # Closes all the frames
    cv2.destroyAllWindows()


main()