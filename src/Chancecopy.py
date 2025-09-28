from cmu_graphics import *
from handdetection import * 
from types import SimpleNamespace
import cv2
from PIL import Image
import random

class Chance:
    def __init__(self, app):

        self.obstacles = []
        self.timer = 0
        self.roadOffset = 0
        self.win = None
        self.width = app.width
        self.height = app.height
        self.buggyWidth = self.width // 3
        self.buggyHeight = self.height // 5
        self.buggyX = 10
        self.buggyY = 0
        self.framesToWin = 60 * 8  # 20 seconds
        self.scrollSpeed = 10
        self.finishLineX = self.width + 400 
        self.startLineX = 100
        self.cap = cv2.VideoCapture(0)
        self.fingersUp = 0
        self.pointMultiplier = self.height// 7
        self.location = 0
        self.urlBuggy = 'src/PNG/Buggy.png'
        self.urlBuggy = self.convertImage(self.urlBuggy)
        self.chanceGameOver = True
        self.obstacleUrl = self.convertImage('src/PNG/banana.png')
    
    def initializeObstacles(self, app):
        obstacle = SimpleNamespace()
        obstacle.X = random.randint(app.width + 100, app.width + 400) 
        obstacle.Y = random.randint(0, app.height - 50)
        obstacle.height = app.height // 8
        obstacle.width = app.height // 8

        self.obstacles.append(obstacle)
    
    #instead of moving buggy the obstacles move left
    def moveObstacle(self):
        for obstacle in self.obstacles:
            obstacle.X -= 10
    #checks to remove obstacles when moves off board
    def checkPosition(self, app):
        for obstacle in self.obstacles:
            selfRight = obstacle.X + obstacle.width/2
            if selfRight <= 0:
                self.obstacles.remove(obstacle)


    #checks if the buggy collided with any obstacles
    def checkCollision(self, obstacle):
        self.buggyLeft = self.buggyX
        self.buggyRight = self.buggyX + self.buggyWidth
        self.buggyTop = self.buggyY
        self.buggyBottom = self.buggyY + self.buggyHeight
        self.oLeft = obstacle.X
        self.oRight = obstacle.X + obstacle.width
        self.oTop = obstacle.Y
        self.oBottom = obstacle.Y + obstacle.height
        if (self.buggyLeft < self.oRight and self.buggyRight > self.oLeft and
            self.buggyTop < self.oBottom and self.buggyBottom > self.oTop):
            return True
        return False
    
    def resetChance(self, app):
        self.chanceGameOver = True
        self.timer = 0
        self.obstacles = []
        
    def drawRoad(self, app): #used ChatGPT
        drawRect(0, 0, self.width, self.height, fill='dimGray')
        lineHeight = 10
        dashWidth = 30
        gap = 20
        y = self.height / 2 - lineHeight / 2
        for x in range(-dashWidth, self.width + dashWidth, 
                       dashWidth + gap):
            drawRect(x + self.roadOffset, y, dashWidth, lineHeight, 
                     fill='white')
        #draw Start
        drawRect(self.startLineX, 0, 10, self.height, fill='white')
        # Finish line
        if self.timer >= 60 * 20:
            drawRect(self.finishLineX, 0, 10, self.height, fill='gold')
        # checkerboard effect:
            squareSize = 10
            for yOffset in range(0, self.height, squareSize * 2):
                drawRect(self.finishLineX, yOffset, 10, squareSize, 
                         fill='black')
                drawRect(self.finishLineX, yOffset + squareSize, 
                        10, squareSize, fill='white')

    def onExit(self, app):
        self.cap.release()

    def startChance(self):
        self.chanceGameOver = not self.chanceGameOver

    def drawChance(self, app):
        if self.chanceGameOver:
            drawRect(0, 0, self.width, self.height, fill='lightgray')
            if self.win == True:
                drawLabel("You Win! Collect $200. Press enter to " 
                "return to board.", self.width/2, self.height/2, 
                size=40, bold=True, fill='red')
            elif self.win == False:
                drawLabel("You Lose! Pay $200 in Fees. " 
                "Press enter to return to board.", self.width/2, 
                self.height/2, size=40, bold=True, fill='red')
            else:
                drawLabel('Welcome to chance!', self.width/2, 
                          self.height/3, size=30, bold=True, fill='red')
                drawLabel('Use your hand motions to move the buggy to ' 
                            'avoid obstacles.', self.width/2, self.height/2, 
                            size=30, bold=True, fill='red')
                drawLabel('Press enter to start!', 
                self.width/2, 2*self.height/3, size=30, 
                bold=True, fill='red')
        elif self.chanceGameOver == False:
            self.drawRoad(app)
            drawImage(self.urlBuggy, self.buggyX, self.buggyY, 
                    width = self.buggyWidth, height = self.buggyHeight)
            drawLabel(f'Number of fingers up: {self.fingersUp}', 
                    200, 30, size = 25, fill = 'white', bold = True)
            for obstacle in self.obstacles:
                drawImage(self.obstacleUrl, obstacle.X, obstacle.Y, 
                          width = self.width//5, height = 
                          self.height//10)

    def takeChanceStep(self):
        if self.chanceGameOver == False:
            success, frame = self.cap.read() #get the camera to record
            if success: 
                self.fingersUp = detectFingers(frame) 
                self.buggyY = ((self.fingersUp * self.pointMultiplier)
                            -(self.buggyHeight//2))
            else: 
                self.fingersUp = 0
                self.buggyY = 0
            self.timer += 1
            self.roadOffset -= self.scrollSpeed
            if self.roadOffset <= -(50): 
                self.roadOffset = 0
            self.startLineX -= self.scrollSpeed
            self.finishLineX -= self.scrollSpeed
            if self.timer % 60 == 0:
                self.initializeObstacles(app)
            if (self.timer >= 60 * 8):
                self.startLineX -= self.scrollSpeed
                self.finishLineX -= self.scrollSpeed
            if ((self.timer >= 60 * 8) and 
                (self.finishLineX <= self.buggyX + self.buggyWidth)):
                self.chanceGameOver = True
                self.win = True
                return
            for obstacle in self.obstacles:
                self.moveObstacle()
                self.checkPosition(app)
                if self.checkCollision(obstacle):
                    self.chanceGameOver = True
                    self.win = False
    
    def loadPilImage(self, url):
        return Image.open(url)

    def convertImage(self, url):
        pil = Image.open(url)
        w, h = pil.size
        pil = pil.resize((w//2,h//2))
        return CMUImage(pil)
