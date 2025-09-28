from cmu_graphics import *


class ChestCard:
    def __init__(self, name, description, amount):
        self.name = name
        self.description = description
        self.amount = amount   


def makeChestCards():
    return [
        ChestCard('ChestCard1', 'You win First Year \n Showcase' + 
                  ' talent Show! \n Collect $200', 200),
        ChestCard('ChestCard2', "Textbook's fees. \n Pay $50", -50),
        ChestCard('ChestCard3', 'Coffee chat with your mentor. ' +
                    '\n Pay $10', -10),
        ChestCard('ChestCard4', 'You won a raffle \n from CMU Senate! '
                  + '\n Collect $100', 100),
        ChestCard('ChestCard5', 'You lost your CMU ID! \n Pay $30 ' 
                  + 'for a replacement', -30),
        #ChatGPT generated other cards:
        ChestCard('ChestCard6', 'You aced your 15-112 exam! \n' 
                  +'Collect $150', 150),
        ChestCard('ChestCard7', 'You get a summer internship!.'
                  +' \n Collect $120', 120),
        ChestCard('ChestCard8', 'Your org won booth! '+
                  '\n Collect $100', 100),
        ChestCard('ChestCard9', 'Your buggy team broke a record! ' 
                  + '\n Collect $200', 200),
        ChestCard('ChestCard10', 'Alumni donated to \n your startup'+
                  ' idea! \n Collect $250', 250),
        ChestCard('ChestCard11', 'You dropped your \n laptop off'+
                  ' Hamerschlag! \n Pay $200 for repairs', -200),
        ChestCard('ChestCard12', 'You got locked out of your dorm.'+
                  ' \n Pay $25 for a locksmith', -25),
        ChestCard('ChestCard13', "You buy a brownie from SAE." +
                  " \n Pay $10", -10),
        ChestCard('ChestCard14', "Late night study session \n at La Prima."
                  +" \n Pay $15 for coffe", -15),
        ChestCard('ChestCard15', 'Lost your CMU ID *again*. \n Pay $30', -30),
        ChestCard('ChestCard16', "Late-night trip to Canes. \n Pay $15", -15)
       ]

def initializeChest(app):
    app.chestDeck = makeChestCards()
    app.chestDrawn = False
    app.drawnCard = None
    app.chestX = app.height//2
    app.chestY = app.height //2
    app.chestWidth = 360
    app.chestHeight = 240

def loadChestPage(app):
    drawImage(app.chestUrl,0,0,width=app.height, height=app.height)
    if app.chestDrawn == False:
        drawLabel('Draw Chest Card!', app.chestX, app.chestY, 
                  size = 25, fill='white', bold = True)
    else:
        drawRect(app.height-75,25,50,50,fill='lightBlue')
        drawLabel('X',app.height - 50,50,size=30,fill='white',bold = True)
        i = 0
        for line in app.drawnCard.description.splitlines():
            spacing = 25
            drawLabel(line, app.chestX, app.chestY - 15 + i*spacing, 
                      size = 20, fill='white', bold = True )
            i += 1