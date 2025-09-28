from cmu_graphics import *
from types import SimpleNamespace
from PIL import Image
import random
import cv2
import mediapipe as mp

class Jail:
    #initializes all variables used for jail
    def __init__(self, app):
        #gets all image urls (as CMU image)
        images = ['src/PNG/starfish (2).png', 'src/PNG/starfish (3).png', 
                  'src/PNG/starfish (4).png', 'src/PNG/starfish (5).png']
        self.images = []
        urlD = 'src/PNG/donner_1.png'
        urlD2 = 'src/PNG/donner.png'
        urlD3 = 'src/PNG/donner_win.png'
        urlD4 = 'src/PNG/donner_lose.png'
        urlB1 = 'src/PNG/bucket.png'
        urlB2 = 'src/PNG/bucket (1).png'
        urlB3 = 'src/PNG/bucket (2).png'
        self.urlRules = self.convertImage(urlD)
        self.urlBackground = self.convertImage(urlD2)
        self.urlWin = self.convertImage(urlD3)
        self.urlLose = self.convertImage(urlD4)
        self.urlBucket = [self.convertImage(urlB1), self.convertImage(urlB2)
                          , self.convertImage(urlB3)]
        for image in images: 
            self.images.append(self.convertImage(image))
        
        self.starfish = []
        self.stepsPerSecond = 850
        self.lose = False
        self.stepCount = 0
        self.width = 796
        self.height=796

        #initialize all bucket variables
        self.bucketX = self.width//2
        self.bucketHeight = 200
        self.bucketWidth = 200
        self.bucketY = self.height - self.bucketHeight - 20

        #hand tracking
        #used https://gautamaditee.medium.com/hand-recognition-
        # using-opencv-a7b109941c88 as a guide:  
        self.cap = cv2.VideoCapture(0)
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(max_num_hands=1, 
                                        min_detection_confidence=0.7)
        self.mpDraw = mp.solutions.drawing_utils

        #win/lose/game over logic
        self.score = 0
        self.started = False
        self.lose = False
        self.won = False
        self.addStarfish(app)

    def loadPilImage(self, url):
        return Image.open(url)
        
    def convertImage(self, url):
        pil = Image.open(url)
        w, h = pil.size
        pil = pil.resize((w//2,h//2))
        return CMUImage(pil)
        
    #simple name space adding all the starfish
    def addStarfish(self, app):
        starfish = SimpleNamespace()
        starfish.index = random.randrange(len(self.images))
        starfish.width = 150
        starfish.height = 150
        starfish.x = random.randrange(starfish.width, 
                                      self.width - starfish.width)
        starfish.y = -10
        self.starfish.append(starfish)
    
    #checking if the starfish and bucket collides
    def collision(self, bucketX, bucketY, bucketSize, starfishX, 
                  starfishY, starfishSize):
        starfishBottom = starfishY + starfishSize
            
        #code by chatGPT
        if (starfishX < bucketX + bucketSize and
        starfishX + starfishSize > bucketX and
        starfishBottom > bucketY + 50):
            return True
        return False
    
    #moving the starfish with each step
    def takeStep(self, app):
        if self.started:
            if self.lose or self.won:
                self.cap.release()

                
            # Hand tracking
            # used https://gautamaditee.medium.com/hand-recognition-
            # using-opencv-a7b109941c88 as guide:
            success, frame = self.cap.read()
            if success:
                frame = cv2.flip(frame, 1)
                rgbFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                results = self.hands.process(rgbFrame)

                if results.multi_hand_landmarks:
                    for handLms in results.multi_hand_landmarks:
                        middle = handLms.landmark[12]  # wrist
                        middleX = middle.x 
                         # gets a value between 0-1 of wrist position

                        # Map wrist Y to buggy Y by mutiplying wristY by 
                        # the height of our app.
                        self.bucketX = max(0, min(self.width - self.bucketWidth, 
                                                  middleX * self.width))
        
        #goes through each starfish to see if it collides wsith ground or bucket
            for currStarfish in self.starfish:
                starfishIndex = self.starfish.index(currStarfish)
                currStarfish.y += 5
                if (currStarfish.y + currStarfish.height - 25 >= self.height 
                    and self.score <= 1000):
                    self.lose = True
                if (self.collision(self.bucketX, self.bucketY, 
                                   self.bucketWidth, currStarfish.x, 
                                   currStarfish.y, currStarfish.width)):
                    self.starfish.pop(starfishIndex)
                    self.score += 100
            if self.score >= 1000:
                self.won = True

            if self.stepCount % 30 == 0 and self.stepCount != 0:
                self.addStarfish(app) 
            self.stepCount += 1

    def startStarfish(self):
        self.started = True

    #draws everything
    def drawJailGame(self, app):
        if not self.started:
            drawImage(self.urlRules, 0, 0, width=self.width, 
                      height=self.height)
        else:
            if self.won:
                drawImage(self.urlWin, 0, 0, width = self.width, 
                          height = self.height)
            elif self.lose:
                drawImage(self.urlLose, 0, 0, width = self.width, 
                          height = self.height)
            else:
                drawImage(self.urlBackground, 0, 0, width=self.width, 
                          height=self.height)
                if self.score <= 1000:
                    if self.score < 200:
                        bucketIndex = 0
                    elif self.score < 600:
                        bucketIndex = 1
                    else:
                        bucketIndex = 2
                    drawImage(self.urlBucket[bucketIndex], self.bucketX, 
                              self.bucketY, width = self.bucketWidth, 
                              height = self.bucketHeight)

                    for starfish in self.starfish:
                        drawImage(self.images[starfish.index], 
                                  starfish.x, starfish.y, 
                                  width = starfish.width, 
                                  height = starfish.height)
