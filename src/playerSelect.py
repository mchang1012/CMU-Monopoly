from cmu_graphics import *
from board import *

#Setting number of Players
def onPlayerCountScreenStart(app):
    startX = app.width / 8
    buttonY = app.height / 1.3
    spacing = app.width/22
    buttonWidth = app.width / 4.9
    app.playerNumberSelectButtons = []
    for i in range(4): # 2, 3, 4, 5
        buttonX = startX + (i*(buttonWidth+spacing))
        number = i+2
        app.playerNumberSelectButtons.append((buttonX, buttonY, number))

def drawPlayerCountScreen(app):
    playerCountUrl = 'src/PNG/playerCount.png'
    drawImage(playerCountUrl,0,0,width = app.width,height = app.height)
    for button in app.playerNumberSelectButtons: # 2, 3, 4, 5
        buttonX, buttonY, number = button
        #draw the player number text
        drawLabel(f'{number}', buttonX, 
                  buttonY - app.width/30, bold = True, fill = 'white', 
                  size = app.height/20)
        drawLabel('players', buttonX, 
                  buttonY + app.width/30, bold = True, fill = 'white', 
                  size = app.height/20)

def playerCountClicked(app, mouseX, mouseY): #returns number of button clicked
    for button in app.playerNumberSelectButtons:
        buttonX, buttonY, number = button
        buttonWidth = app.width / 4.9
        buttonHeight = app.height / 3.64
        buttonLeft = buttonX - (buttonWidth/2)
        buttonRight = buttonX + (buttonWidth/2)
        buttonTop = buttonY - (buttonHeight/2)
        buttonBottom = buttonY + (buttonHeight/2)
        if ((buttonLeft <= mouseX <= buttonRight) and 
            (buttonTop <= mouseY <= buttonBottom)):
            return number
# Creating each player

def onPlayerSelectionScreen(app):
    app.selectButtonX = app.width/2
    app.selectButtonY = 4*app.height/5
    app.selectButtonWidth = app.height/8
    app.selectButtonHeight = app.height/12

def drawPlayerSelectionScreen(app):
    drawImage(app.selectCharacterUrl,0,0,width=app.width,height=app.height)
    drawLabel(f'Player {app.currPlayer +1} Choose Your Character!', 
              app.width/2, app.height/4, size= app.height/20, 
              fill= 'white',bold=True)
    character = app.characterChoices[app.currCharacterIndex]
    url = character['url']
    name = character['name']
    if url not in app.chosenCharacters:
        drawImage(url, app.width/2, app.height/2,
            width=app.height/5, height=app.height/5, align='center')
        drawLabel(name, app.width/2, app.height/2 + 120, size=20)
        drawRect(app.selectButtonX, app.selectButtonY, app.selectButtonWidth, 
                app.selectButtonHeight, align='center', 
                fill='lightBlue', border='black')
        drawLabel("Select", app.width/2, app.height*4/5, size=app.height/50)

    drawLabel("←", app.width/4, app.height/2, size=40)
    drawLabel("→", app.width*3/4, app.height/2, size=40)

def selectArrowClicked(app, mouseX, mouseY):
    if (app.width/4 - 20 <= mouseX <= app.width/4 + 20 and 
        app.height/2 - 20 <= mouseY <= app.height/2 + 20):
        return 'left'
    elif app.width*3/4 - 20 <= mouseX <= app.width*3/4 + 20 and \
        app.height/2 - 20 <= mouseY <= app.height/2 + 20:
        return 'right'

def selectCharacterClicked(app, mouseX, mouseY):
    buttonLeft = app.selectButtonX - (app.selectButtonWidth/2)
    buttonRight = app.selectButtonX + (app.selectButtonWidth/2)
    buttonTop = app.selectButtonY - (app.selectButtonHeight/2)
    buttonBottom = app.selectButtonY + (app.selectButtonHeight/2)
    
    if ((buttonLeft <= mouseX <= buttonRight) and 
        (buttonTop <= mouseY <= buttonBottom)):
        return True

    
def selectCharacter(app):
    url = app.characterChoices[app.currCharacterIndex]
    app.chosenCharacters.append(url)
    createPlayer(app,app.currPlayer, url)
    app.characterChoices.pop(app.currCharacterIndex)

def createPlayer(app, number, url):
    newPlayer = Player(number,url)
    app.players.append(newPlayer)
