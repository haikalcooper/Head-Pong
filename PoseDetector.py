
##code made with the help of Chris Whitmire and adapted from mediapipe 


###########
# imports
###########

import pygame
import mediapipe as mp
import cv2

class PoseDetector:

    
    def __init__(self, a_min_detection_confidence=0.8, a_min_tracking_confidence=0.8) -> None:
        """_summary_

        Args:
            a_min_detection_confidence (float, optional): _description_. Defaults to 0.5.
            a_min_tracking_confidence (float, optional): _description_. Defaults to 0.5.
        """
        # load the video from the webcam
        self.capture = cv2.VideoCapture(0)

        #### setting parameters for the webcam capture
        self.capture.set(3, 640) # the width of the window
        self.capture.set(4, 480) # height of the window

        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.mp_pose = mp.solutions.pose

        self.pose = self.mp_pose.Pose(min_detection_confidence=a_min_detection_confidence, min_tracking_confidence=a_min_tracking_confidence)

        self.shouldClose = False

        # dictionary to store hand landmarks
        self.landmarkDictionary = {}
        

    def update(self) -> None:
        """Opens and updates a window that displays webcam feed. It also stores the positions of
        landmark points on an identified hand in a dictionary.
        """
        # loop through every frame of the video and show it (stops when you reach the end of the video)
        if self.capture.isOpened():
            # read the next frame of the video. "isLoaded" is a boolean representing whether the frame was loaded or not
            isLoaded, img = self.capture.read()

            if isLoaded == True:
                # To improve performance, optionally mark the image as not writeable to
                # pass by reference.
                img.flags.writeable = False

                # the hand predictive model was trained on BGR images
                # so we need to convert our image to RGB
                imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

                # get all the landmarks for every body in the image
                results = self.pose.process(img)

                # clear the dictionary of all the hand's landmarks
                self.landmarkDictionary = {}

                # if there are any hands detected on the image (via their landmarks)
                if results.pose_landmarks:
                    
                    # for every set of landmarks (1 set per hand) in the image
                    for landmarkId, landmarkSet in enumerate(results.pose_landmarks.landmark):
                        # get the width height and channels of the image
                        height, width, channels = img.shape
                        # convert the position of the landmarks from a fraction to a location on the img
                        xPos, yPos, zPos = int(landmarkSet.x*width), int(landmarkSet.y*height), int(landmarkSet.z*height)
                        # Save list of lists storing x and y pos
                        self.landmarkDictionary[landmarkId] = [xPos, yPos, zPos]

                 # Draw the pose annotation on the image.
                img.flags.writeable = True
                image = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
                self.mp_drawing.draw_landmarks(
                    img,
                    results.pose_landmarks,
                    self.mp_pose.POSE_CONNECTIONS,
                    landmark_drawing_spec=self.mp_drawing_styles.get_default_pose_landmarks_style())
                # Flip the image horizontally for a selfie-view display.
                cv2.imshow('MediaPipe Pose', cv2.flip(img, 1))

                if cv2.waitKey(1) & 0xFF == ord('q') or cv2.getWindowProperty('MediaPipe Pose', 0) < 0:
                    self.shouldClose = True


    