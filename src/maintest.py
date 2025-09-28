from cmu_graphics import *
from board import *
from questions import *
from playerSelect import *
from Chest import *
from PIL import Image
from jail import *
from Chancecopy import *
import random

def loadPilImage(url):
    return Image.open(url)

def convertImage(url):
    pil = Image.open(url)
    w, h = pil.size
    pil = pil.resize((w//2,h//2))
    return CMUImage(pil)

def onAppStart(app):
    startGame(app)

def resetCards(app):
    app.questions = makeQuestions()
    app.questionIndex = None
    app.state = 'board' 
    app.currQuestion = '' 
    app.options = [] 
    app.optionCircles = [] 
    app.optionLabels = []
    app.answer = '' 
    app.feedback = '' 
    app.selectedOptionIndex = None 
    app.answered = False
    app.cardLabel = None 
    app.showExitButton = False 
    app.playerRolled = False
    app.taxPaid = False
    app.currTax = None
    app.currRent = None
    app.paidRent = False
    app.ChestAmount = None
    loadQuestionScreen(app) 

def startGame(app):
    app.stepCount = 0
    app.stepsPerSecond = 20
    app.gameTimeLeft = 90
    
    #Player 
    app.numPlayers = None
    onPlayerCountScreenStart(app)
    app.players = []
    app.characterChoices= [
        {'url': convertImage('src/PNG/112Dragon.png'),
               'name': '112 Dragon'},
        {'url': convertImage('src/PNG/cmuBagpipe.png'),
              'name': 'CMU Bagpipe'},
        {'url': convertImage('src/PNG/donnerWhale.png'),
             'name': 'Donner Whale'},
        {'url': convertImage('src/PNG/ranchFlamingoFix.png'),
           'name': 'Ranch Flamingo'},
        {'url': convertImage('src/PNG/scottyDog.png'),
               'name': 'Scotty Dog'},
        {'url': convertImage('src/PNG/whescoPenguin.png'),  
         'name': 'Whesco Penguin'}
    ]

    #Player selection options
    app.chosenCharacters = []  
    app.currPlayer = 0
    app.characterButtons = []
    app.currCharacterIndex = 0
    onPlayerSelectionScreen(app)


    #Dice
    app.diceWidth = 60
    app.diceHeight = 60
    app.diceIndex = 0
    app.diceNumber = random.randrange(1, 7)
    app.allDice = []
    allDice = ['src/PNG/dice1.png', 'src/PNG/dice2.png', 
               'src/PNG/dice3.png', 'src/PNG/dice4.png', 
               'src/PNG/dice5.png', 
                'src/PNG/dice6.png']
    for dice in allDice:
        app.allDice.append(convertImage(dice))
    app.firstRoll = False
    app.isRolling = False
    app.playerRolled = False

    #board
    app.locations = makeLocations()
    app.taxIndicies = [6,12]

    app.board = Board()
    # app.player = Player(10, 'src/PNG/112Dragon.png')
    app.currentTile = 0
    app.availableQuestions = list(range(1,41))
    resetCards(app)
    app.state = 'home'
    
    app.buttonWidth = app.height//2 - 35
    app.buttonHeight = 50

    #images
    app.urlBoard = convertImage('src/PNG/monopolyBoard.png')
    app.playerInfoUrl = convertImage('src/PNG/playerInfo.png')
    app.homeUrl = convertImage('src/PNG/home.png')
    app.questionUrl = convertImage('src/PNG/questions.png')
    app.selectCharacterUrl = convertImage('src/PNG/playerSelect.png')
    app.rulesUrl = convertImage('src/PNG/Rules.png')
    app.chestUrl = convertImage('src/PNG/chestCard.png')
    app.endUrl = convertImage('src/PNG/gameOver.png')

    #chest
    initializeChest(app)
    app.chestIndicies = [8, 17, 33]

    #chance
    app.chance = Chance(app)
    app.chanceIndicies = [3, 14, 28]
    app.chanceGameOver = True

    #logic for jail minigame
    app.jailIndex = {10, 30}
    app.jail = Jail(app)
    app.jailStarted = False

    #winner of game
    app.winner = None

    
def onKeyPress(app, key):
    player = app.players[app.currPlayer]
    if app.state == 'jail' and key =='enter':
        if app.jailStarted == False:
            app.jail.startStarfish()
            app.jailStarted = True
        else:
            app.jailStarted = False
            if app.jail.lose:
                player.money -= 200
            app.state = 'board'
            app.isRolling = False
            app.playerRolled = False
            app.jail.won = False
            app.jail.lose = False
            resetCards(app)
            nextTurn(app)

#code by chatGPT

    if app.state == 'chance' and key == 'enter':
        if app.chanceGameOver == True:
            app.chance.startChance()  
            app.chanceGameOver = False
        else:
            app.chanceGameOver = True
            if app.chance.win == True:
                app.players[app.currPlayer].money += 200
            if app.chance.win == False:
                app.players[app.currPlayer].money -= 200
            app.state = 'board'
            app.isRolling = False
            app.playerRolled = False
            app.chance.win = None
            resetCards(app)
            nextTurn(app)


def onMousePress(app, mouseX, mouseY):
    #app.width = 1470, app.height = 919, 890
    # if the home screen is showing
    if app.state == 'home':
        #rulesButtonDimensions
        rulesButtonWidth = 525
        rulesButtonHeight = 130
        rulesButtonLeft = 15*app.width/32 + 15
        rulesButtonRight = rulesButtonLeft + rulesButtonWidth
        rulesButtonTop = 17*app.height/32 - 10
        rulesButtonBottom = rulesButtonTop + rulesButtonHeight

        #startButtonDimensions
        startButtonHeight = 130
        startButtonLeft = 15*app.width/32 + 15
        startButtonRight = rulesButtonLeft + rulesButtonWidth
        startButtonTop = 24*app.height/32 - 10
        startButtonBottom = startButtonTop + startButtonHeight

        #check if player selects start or rules button     
        if ((rulesButtonLeft <= mouseX <= rulesButtonRight) and 
            (rulesButtonTop <= mouseY <= rulesButtonBottom)):
            app.state = 'rules'
        elif ((startButtonLeft <= mouseX <= startButtonRight) and 
            (startButtonTop <= mouseY <= startButtonBottom)):
            app.state = 'playerCountSelect'
        

    #if the player count select screen is showing
    elif app.state == 'playerCountSelect':
        if playerCountClicked(app, mouseX, mouseY):
            app.numPlayers = playerCountClicked(app, mouseX, mouseY)
            app.state = 'playerSelection' 
    elif app.state == 'playerSelection':
        if selectArrowClicked(app, mouseX, mouseY) is not None:
            if selectArrowClicked(app, mouseX, mouseY) == 'left':
                app.currCharacterIndex = ((app.currCharacterIndex - 1) 
                                          % len(app.characterChoices))
            else:
                app.currCharacterIndex = ((app.currCharacterIndex + 1) 
                                          % len(app.characterChoices))
        elif selectCharacterClicked(app, mouseX, mouseY):
            char = app.characterChoices[app.currCharacterIndex]
            if char not in app.chosenCharacters:
                selectCharacter(app)
                app.currPlayer += 1
                if app.currPlayer == app.numPlayers:
                    app.currPlayer = 0
                    app.currentTile = app.players[app.currPlayer].tileIndex
                    app.timerSteps = [0 for i in range(len(app.players))]
                    app.state = 'board' 
                else:
                    app.currCharacterIndex = 0 
   #if the rules page is showing
    elif (app.state == 'rules' and (app.width - 75 <= mouseX <=app.width - 25)
           and (0 <= mouseY <= 100)) :
        app.state = 'home'

    #if the board is showing
    elif app.state == 'board':
        if not app.playerRolled:  
            centerX = app.height // 2
            centerY = app.height // 2 + 225
            if (centerX - app.diceWidth // 2 < mouseX < 
                centerX + app.diceWidth // 2 and
                centerY - app.diceHeight // 2 < mouseY < 
                centerY + app.diceHeight // 2):
                if not app.isRolling: 
                    app.isRolling = True
                    app.firstRoll = True
                    app.playerRolled = True
                    app.stepCount = 0
                    app.diceNumber = random.randrange(1, 7)
                    #checking if we should load the question
        if app.playerRolled:
            if clickedHere(app,mouseX,mouseY) == True:
                if app.currentTile in app.locations:
                    if app.board.tiles[app.currentTile].owner == None:
                        loadQuestionScreen(app)
                        app.state = 'question'
                    else:
                        app.state = 'rent'
                elif app.currentTile in app.taxIndicies:
                    if not app.taxPaid:
                        app.currTax = app.players[app.currPlayer].money // 10
                        app.players[app.currPlayer].money -= app.currTax 
                         # or however much tax costs
                        app.taxPaid = True
                        app.state = 'tax'
                elif app.currentTile in app.chestIndicies:
                    app.state = 'chest'
                elif app.currentTile in app.chanceIndicies:
                    app.state = 'chance'
                elif app.currentTile == 0 or app.currentTile == 20:
                    app.state = 'jail'
                elif app.currentTile == 10:
                    app.state = 'go'
                elif app.currentTile == 30:
                    app.state = 'free parking'
                
    #if the question screen is showing
    elif app.state == 'question':
        if (app.showExitButton and clickedExitButton(app,mouseX,mouseY)):
            nextTurn(app)
            # app.state = 'board'
            app.cardLabel = None
            resetCards(app)
            
        elif not app.answered:
            for i in range(len(app.optionCircles)):
                cy = app.optionCircles[i]
                if (mouseX-(app.height/4 + 50))**2 + (mouseY-cy)**2 <= 15**2:
                    app.selectedOptionIndex = i
                    selectedOption = app.optionLabels[i][0]
                    if selectedOption == app.answer:
                        app.state = 'buy'
                    else:
                        app.feedback = 'Incorrect.'
                        app.showExitButton = True

                    app.answered = True
                    app.availableQuestions.remove(app.questionIndex)
                    break

    if app.state == 'rent':
        if clickedPayButton(app, mouseX, mouseY) and not app.paidRent:
            payRentReal(app)
            app.paidRent = True
        elif clickedExitButton(app,mouseX,mouseY) and app.paidRent:
            nextTurn(app)
            app.cardLabel = None
            app.paidRent = False
            resetCards(app)
        
    elif app.state == 'buy':
        if clickedBuy(app, mouseX, mouseY):
            buyProperty(app)
        # Check if they clicked the exit button on the buy screen
        elif clickedBuyExit(app, mouseX, mouseY):  
            nextTurn(app)
            # app.state = 'board'
            app.cardLabel = None
            resetCards(app)
    
    elif app.state == 'chance':
        if clickedBuyExit(app,mouseX,mouseY):
            nextTurn(app)
            app.cardLabel = None
            resetCards(app)

    elif app.state == 'tax':
        if clickedExitButton(app,mouseX,mouseY):
            nextTurn(app)
            app.cardLabel = None
            resetCards(app)
    elif app.state == 'go' or app.state == 'free parking':
        if clickedExitButton(app,mouseX,mouseY):
            nextTurn(app)
            app.cardLabel = None
            resetCards(app)

    elif app.state == 'chest' and not app.chestDrawn:
        if ((app.height/2 - 180 <= mouseX <= app.height/2 + 180)
            and (app.height/2 - 120 <= mouseY <= app.height/2 + 120)):
            app.drawnCard = random.choice(app.chestDeck)
            app.chestDeck.remove(app.drawnCard)
            money = app.drawnCard.amount
            selectedPlayer = app.players[app.currPlayer]
            selectedPlayer.money += money        
            app.chestDrawn = True
    elif app.state == 'chest' and app.chestDrawn:
        if clickedExitButton(app,mouseX,mouseY):
            app.chestDrawn = False
            nextTurn(app)
            app.cardLabel = None
            resetCards(app)
    
    if app.state == 'endGame':
        #startButtonDimensions
        restartButtonHeight = 130
        restartButtonLeft = 15*app.width/32 + 15
        restartButtonRight = 15*app.width/32 + 15 + 525
        restartButtonTop = 24*app.height/32 - 10
        restartButtonBottom = restartButtonTop + restartButtonHeight
        if ((restartButtonLeft <= mouseX <= restartButtonRight) and 
            (restartButtonTop <= mouseY <= restartButtonBottom)):
            app.state = 'home'
            startGame(app)

        
def redrawAll(app):   
   
    if (app.state == 'board' or app.state == 'question' 
        or app.state == 'rent' or app.state == 'buy' or 
        app.state == 'chest' or app.state == 'jail' or 
        app.state == 'tax' or app.state == 'go' or 
        app.state == 'free parking' or app.state == 'tuition'):
        player = app.players[app.currPlayer]
        rightDist = app.width - app.height
        drawImage(app.playerInfoUrl,app.height,0, 
                  width = app.width - app.height, height = app.height)
        drawLabel(f'Player {app.currPlayer +1} Information:',app.height + 
                  rightDist/2,120,align = 'center', size = 45, 
                  fill = 'white', bold = True)
        time = timeDisplay(app.gameTimeLeft)
        drawLabel(f'Game Time Remaining: {time}',app.height + 
                  rightDist/2,160,align = 'center', size = 25, 
                  fill = 'white', bold = True)
        drawLabel(player.timer,app.height + rightDist/2,278,
                  size = 30, bold=True)
        drawLabel(f'${player.money}',app.height + 
                  rightDist/2 -25, 367, size = 30, bold = True)
        if player.properties == []:
            drawLabel("You don't own any properties yet.", 
                      app.height + 50, 495, size = 25, 
                      bold = True, align ='left')
            drawLabel('Save up to buy!',app.height + 50, 525, 
                      size = 25, bold = True, align ='left')
        else:
            i = 0
            for tileIndex in player.properties:
                property = app.board.tiles[tileIndex]
                propertyName = property.name
                propertyVal = property.price
                propertRent = property.rent
                drawLabel(f'You own {propertyName}!  Value: ${propertyVal} ' 
                          +  f'Rent: ${propertRent}',
                        app.height + 35, 515 + i*30, size = 20, bold = True,
                          align ='left')
                i += 1
        
    #BOARD
    if app.state == 'board' or app.state == 'jail':
        drawImage(app.urlBoard, 0,0, width = app.height+1, height = app.height)
        
        #drawing the dice in board
        if app.isRolling: 
            drawLabel("Rolling..", app.height/2, app.height/2 + 275, size = 25)
        elif app.playerRolled:
            drawLabel(f'You rolled a {app.diceNumber}', app.height/2, 
                      app.height/2 + 275, size = 25)
        app.board.getBoard(app)
        url = app.allDice[app.diceIndex]
        drawImage(url, app.height//2, app.height//2 + 225, align='center', 
                  width=app.diceWidth, height=app.diceHeight)
        
        #drawing the player in board
        characterInfo = app.chosenCharacters[app.currPlayer]
        charUrl = characterInfo['url']
        app.players[app.currPlayer].url = charUrl
        app.players[app.currPlayer].drawPlayer(app.board)

        #drawing instructions and score if the player hasn't rolled
        if app.cardLabel == None:
            drawLabel('Roll dice to begin turn!', app.height//2,
                      app.height/4 - 50,size=45,
                      bold=True, fill='white',border = 'black',
                      align = 'center')
        #once they roll, tell them where they landed and next instructions
        elif 'Landed' in app.cardLabel:
            rightDist = app.width - app.height
            drawLabel(app.cardLabel, app.height/2,app.height/4 - 70,
                      size=30,bold=True, fill='white',border = 'black')
            drawLabel('Click here to get your card!',app.height/2,
                      app.height/4 - 10,fill='white',border = 'black',
                      size=35,bold=True)
       
        if app.state == 'jail':
            app.jail.drawJailGame(app)
    

    #load question page - if landed on property
    if app.state == 'question':
        drawScreenAndQuestion(app)
        drawOptions(app)
        drawFeedbackAndClose(app)
    
    elif app.state == 'buy':
        drawBuyScreen(app)

    elif app.state == 'rent':
        drawCardPrompt(app)
        payRent(app)

    elif app.state == 'tax':
        drawCardPrompt(app)
        drawTaxPage(app)
   
    #load chest page - if landed on chest
    elif app.state == 'chest':
        drawCardPrompt(app)
        loadChestPage(app)

    elif app.state == 'chestPrompt':
        drawCardPrompt(app)
        loadChestPrompt(app)
    
    elif app.state == 'chance':
        app.chance.drawChance(app)
    
    elif app.state == 'go':
        drawGo(app)
    
    elif app.state == 'free parking':
        drawFreeParking(app)

    #drawing the home screen
    elif app.state == 'home':
        drawImage(app.homeUrl, 0, 0, width = app.width, height = app.height)
        
    
    #drawing the rules page
    elif app.state == 'rules':
        drawImage(app.rulesUrl,0,0,width=app.width,height=app.height)
        drawLabel('X',app.width - 50,50,size=50,fill='white',bold=True)

    #drawing the player count screen
    elif app.state == 'playerCountSelect':
        drawPlayerCountScreen(app)
    elif app.state == 'playerSelection':
        drawPlayerSelectionScreen(app)

    if app.state == 'endGame':
        drawImage(app.endUrl, 0,0, width = app.width, height = app.height)
        if len(app.winner) == 1:
            player = app.winner[0]
            drawLabel(f'Player {app.winner[0] + 1} won the game! Congrats!',
                      app.width//2 + 225, app.height//3, size=35, bold=True)
            drawLabel(f'Score: ${app.players[player].money}', 
                      app.width//2 + 225, app.height//3 + 50, 
                      size=35, bold=True)
    
        else:
            names = ', '.join(f'Player {i + 1}' for i in app.winner)
            player = app.winner[0]
            if len(names) >= 20:
                drawLabel("It's a tie between", 
                      app.width//2 + 225, app.height//3, size=35, bold=True)
                drawLabel(f"{names}", 
                      app.width//2 + 225, app.height//3 + 50, 
                      size=35, bold=True)
                drawLabel(f"with a score of {app.players[player].money}!", 
                      app.width//2 + 225, app.height//3 + 100, 
                      size=35, bold=True)
            else:
                drawLabel(f"It's a tie between {names}", 
                      app.width//2 + 225, app.height//3, size=35, bold=True)
                drawLabel(f"with a score of {app.players[player].money}!", 
                      app.width//2 + 225, app.height//3 + 50, 
                      size=35, bold=True)


def onStep(app):
    if app.state != 'endGame' and (app.state == 'board' or 
                                   app.state == 'question' or 
                                   app.state=='tax' or 
                                   app.state == 'rent' or 
                                   app.state == 'chest' 
                                   or app.state == 'go' or 
                                   app.state =='free parking'):
        app.timerSteps[app.currPlayer] += 1
        if app.timerSteps[app.currPlayer] >=20:
            app.players[app.currPlayer].timer -= 1
            app.gameTimeLeft -= 1
            if app.gameTimeLeft <= 0:
                app.state = 'endGame'
                app.winner = getWinner(app)
            app.timerSteps[app.currPlayer] = 0

        if app.players[app.currPlayer].timer == 0:
            app.players[app.currPlayer].timer = 60
            resetCards(app)
            nextTurn(app)
            

    # if the dice is rolling, move the player accordingly
    if app.isRolling == True:
        app.diceIndex = (app.diceIndex + 1) % 6
        app.stepCount += 1
        if app.stepCount >= 30: 
            app.isRolling = False
            app.players[app.currPlayer].moveNext(app.board,app.diceNumber)
            app.currentTile = app.players[app.currPlayer].tileIndex
            if app.currentTile in app.locations:  #check if tile is a property
                for i in range(len(app.chosenCharacters)):
                    player = app.players[i]
                    if app.currentTile in player.properties:
                        app.state = 'rent'
                if app.state != 'rent':
                    app.state = 'board'

                app.cardLabel = ('You Landed On ' + 
                                 app.board.tiles[app.currentTile].name)
            elif app.currentTile in app.taxIndicies:
                app.cardLabel = ('You Landed On Pay Tuition!')
            elif app.currentTile in app.chestIndicies:
                app.cardLabel = ('You Landed On Chest!')
            elif app.currentTile == 0 or app.currentTile == 20: 
                app.cardLabel = ('You Landed On ' +
                                 app.board.tiles[app.currentTile].name)
            elif app.currentTile in app.chanceIndicies:
                app.cardLabel = ('You Landed on Chance!')
            elif app.currentTile == 10:
                app.cardLabel = ('You Landed on Go!')
            elif app.currentTile == 30:
                app.cardLabel = ('You Landed on Free Parking!')
            else:
                app.state = 'board'
            app.playerRolled = True
    elif app.state == 'jail':
        app.jail.takeStep(app)
    elif app.state == 'chance':
        app.chance.takeChanceStep()
    else:
        app.diceIndex = app.diceNumber - 1
    
def drawCardPrompt(app):
    if 'Landed' in app.cardLabel:
        drawLabel(app.cardLabel, app.height/2, app.height/4 - 80, size=30, 
                  bold=True, fill='white', border='black')
        drawLabel('Click here to get your card!', app.height/2, app.height/4, 
                  fill='white', border='black', size=35, bold=True)

#Functions related to players begins here through
def timeDisplay(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    if seconds < 10: 
        return f'{minutes}:0{seconds}'
    else:
        return f'{minutes}:{seconds}'

def loadQuestionScreen(app):
    loadQuestion(app)

def splitText(text, maxLength):
    words = text.split(' ')
    lines = []
    currentLine = ""
    for word in words:
        # Check if adding this word would exceed the line length
        if len(currentLine) + len(word) + 1 > maxLength:
            lines.append(currentLine)
            currentLine = word
        else:
            if currentLine:
                currentLine += " " + word
            else:
                currentLine = word
    if currentLine:
        lines.append(currentLine)
    return lines

def drawScreenAndQuestion(app):
    #drawing the screen
    drawImage(app.questionUrl,0,0,width = app.height,height = app.height)
    #if it's a question card, load the question

    # Split the question into lines with a max length of 30 characters per line
    lines = splitText(app.currQuestion, 30)
    
    # Draw each line of text
    i = 0
    for line in lines:
        drawLabel(line, app.height/2, app.height/7 + i * 30, size=30, bold=True)
        i += 1
    
def drawOptions(app):
    #creating the multiple choice circles
    for i in range(len(app.optionCircles)):
        cy = app.optionCircles[i]
        color = 'blue' if app.selectedOptionIndex == i else None
        drawCircle(app.height/4 + 50, cy,15, fill=color, border='black')
    # creating the labels for each potential option
    for option, cy in app.optionLabels:
        lines = splitText(option,50)
        i = 0
        for line in lines:
            drawLabel(option,app.height/4 + 75,cy + i*22,align='left',size=20)
            i += 1

def drawFeedbackAndClose(app):
    #if its a question and they clicked an answer, we want them to be able to 
    # exit the screen, and we want to give them feedback
    if app.answered:
        drawImage(app.questionUrl,0,0,width = app.height,
                  height = app.height)
        drawLabel(app.feedback, app.height/2, app.height/2, size=25, 
                  fill='black', bold = True)
        drawLabel(f'The right answer was {app.answer}',app.height/2,
                  app.height/2+40, size=15, fill='black', 
                  bold = True)
        drawRect(app.height-75,25,50,50,fill='lightBlue')
        drawLabel('X',app.height - 50,50,size=30,fill='black',bold = True)

def clickedHere(app,mouseX,mouseY):
    #checking to see if they clicked 
    return ((100 <= mouseX <= app.height - 100) and 
            (app.height/4 - 25 <= mouseY <= app.height/4 + 25))

def clickedExitButton(app,mouseX,mouseY):
    return ((app.height - 75 <= mouseX <= app.height - 25) 
            and (0 <= mouseY <= 100))

def payRentReal(app):
    rent = app.board.tiles[app.currentTile].rent
    for i in range(len(app.chosenCharacters)):
        player = app.players[i]
        if app.currentTile in player.properties:
            owner = i
    app.players[app.currPlayer].money -= rent
    app.players[owner].money += rent


def payRent(app):
    rent = app.board.tiles[app.currentTile].rent
    for i in range(len(app.chosenCharacters)):
        player = app.players[i]
        if app.currentTile in player.properties:
            owner = i
    drawImage(app.questionUrl,0,0,width = app.height,height = app.height)
    drawLabel('You landed on a property',app.height/2,
              app.height/2 - 30,size=30,bold=True)
    drawLabel(f'owned by Player {owner + 1}. Pay ${rent}.',
              app.height/2,app.height/2 + 30 ,size=30,bold=True)

    drawRect(app.height/2 - 50,2*app.height/3 - 25,
             100,50,fill='lightGreen')
    drawLabel('Pay Now', app.height/2, 2*app.height/3, 
              fill = 'black', bold = True, size = 25)
    if app.paidRent == True:
        drawRect(app.height-75,25,50,50,fill='lightBlue')
        drawLabel('X',app.height - 50,50,size=30,fill='black',bold = True)

def clickedPayButton(app, mouseX, mouseY):
    left = app.height/2 - 50
    right = left + 100
    top = (2*app.height/3) - 25
    bottom = top + 50
    return (left <= mouseX <= right) and (top <= mouseY <= bottom)
    
    
def drawTaxPage(app):
    drawImage(app.questionUrl,0,0,width = app.height,height = app.height)
    drawLabel("It's time to pay tuition! Pay 10%",
              app.height/2,app.height/2,size=30,bold=True)
    drawLabel("- ${app.currTax}",app.height/2,app.height/2 + 50,
              size=30,bold=True)
    drawLabel('X',app.height - 50,50,size=30,fill='black',bold = True)

def buyProperty(app):
    player = app.players[app.currPlayer]
    property = app.board.tiles[app.currentTile]
    if player.money >= property.price:  #buy condition
        player.money -= property.price
        property.owner = player.name  
        player.properties.append(app.currentTile)
        resetCards(app)
        nextTurn(app)
        # app.state = 'board' 
    else:
        app.feedback = "You don't have enough money to buy this property."
        app.cardLabel = None
        resetCards(app)
        nextTurn(app)
        # app.state = 'board'

def drawFreeParking(app):
    drawImage(app.questionUrl,0,0,width = app.height,height = app.height)
    drawLabel("Free Parking!",app.height/2,app.height/2,size=30,bold=True)
    drawLabel('X',app.height - 50,50,size=30,fill='black',bold = True)

def drawGo(app):
    app.players[app.currPlayer].money += 200
    drawImage(app.questionUrl,0,0,width = app.height,height = app.height)
    drawLabel("Congrats on finishing a turn! Collect $200.!",app.height/2,
              app.height/2,size=30,bold=True)
    drawRect(app.height-75,25,50,50,fill='lightBlue')
    drawLabel('X',app.height - 50,50,size=30,fill='black',bold = True)

        
        
def drawBuyScreen(app):
    buttonWidth = app.width//2
    buttonHeight = app.height//12
    property = app.board.tiles[app.currentTile]
    drawImage(app.selectCharacterUrl,0,0,width = app.width, height = app.height)
    drawLabel('You have answered the question correctly!', 
              app.width // 2, app.height // 4, size=20, bold=True)
    drawLabel(f'Would you like to buy {property.name} for ${property.price}?',
               app.width // 2, app.height //3, size=18)

    drawRect(app.width//2-(buttonWidth//2), app.height//2 - (buttonHeight//2), 
             buttonWidth, buttonHeight, fill='darkGreen')
    drawLabel('Buy Property', app.width // 2, app.height //2, 
              fill='white', size=app.height//30)
    
    drawRect(app.width//2-(buttonWidth//2), app.height//1.5 - (buttonHeight//2), 
             buttonWidth, buttonHeight, fill='darkGreen')
    drawLabel('Return To Board', app.width // 2, app.height//1.5, 
              fill='white', size=app.height//30)

def clickedBuy(app,mouseX, mouseY):
    buyButtonWidth = app.width // 2
    buyButtonHeight = app.height // 12
    buyButtonLeft = app.width//2 - (buyButtonWidth//2)
    buyButtonTop = app.height//2 - (buyButtonHeight//2)
    if ((buyButtonLeft <= mouseX <= buyButtonLeft + buyButtonWidth) and 
        (buyButtonTop <= mouseY <= buyButtonTop + buyButtonHeight)):
        return True
    return False

def clickedBuyExit(app, mouseX, mouseY):
    exitButtonWidth = app.width//2
    exitButtonHeight = app.height//12
    exitButtonLeft = app.width//2 - (exitButtonWidth//2)
    exitButtonTop = app.height//1.5 - (exitButtonHeight//2)
    if ((exitButtonLeft <= mouseX <= exitButtonLeft + exitButtonWidth) and 
        (exitButtonTop <= mouseY <= exitButtonTop + exitButtonHeight)):
        return True
    return False

def nextTurn(app):
    app.currPlayer = (app.currPlayer + 1) % len(app.players)  
    # Reset to 0 when it's the last player
    app.players[app.currPlayer].timer = 60
    app.playerRolled = False
    app.players[app.currPlayer].timer = 60
    app.currentTile = app.players[app.currPlayer].tileIndex
    app.state = 'board'

def getWinner(app):
    highest = 0
    currWinner = []
    for i in range(len(app.players)):
        score = app.players[i].money
        if score > highest:
            highest = score
            currWinner = [i]
        elif score == highest:
            currWinner.append(i)
    return currWinner

def main():
    runApp(width=1440,height=796)
main()


