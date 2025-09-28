from cmu_graphics import *

#makes each tile on board 
class Tile: 
    def __init__(self, index, x, y, width, height, owner):
        self.index = index
        self.properties = self.getPropertyInfo()
        self.name = self.properties['name']
        self.color = self.properties['color']
        self.price = self.properties['price']
        self.rent = self.properties['rent']
        self.x = x
        self.y = y
        self.width = width 
        self.height = height
        self.owner = owner
    
    def __repr__(self):
        print(f'{self.name}')
    #initializes property info/attributes for each location
    def getPropertyInfo(self):
        properties = { 
        0: {"name": "Donner Dungeon", "color": "white", 
            "price": 0, "rent": 0, "index": 0},
        1: {"name": "Mr.Bulgogi", "color": "lightBlue",
            "price": 120, "rent": 100, "index": 1},
        2: {"name": "CFA", "color": "lightBlue", 
            "price": 100, "rent": 90, "index": 2},
        3: {"name": "Chance", "color": "white", 
            "price": 0, "rent": 0, "index": 3},  
        4: {"name": "The Hill", "color": "lightBlue",
            "price": 100, "rent": 90, "index": 4},
        5: {"name": "De Fer", "color": "white",
            "price": 200, "rent": 0, "index": 5},
        6: {"name": "Tax", "color": "white", 
            "price": 0, "rent": 0, "index": 6},
        7: {"name": "Hunan", "color": "brown", 
            "price": 60, "rent": 60, "index": 7},
        8: {"name": "Chest", "color": "white", 
            "price": 0, "rent": 0, "index": 8},  
        9: {"name": "Baker/Porter", "color": "brown", 
            "price": 60, "rent": 30, "index": 9},
        10: {"name": "Go", "color": "white", 
            "price": 0, "rent": 0, "index": 10},
        11: {"name": "Tepper", "color": "darkBlue", 
            "price": 400, "rent": 600, "index": 11},
        12: {"name": "Tax", "color": "white", 
            "price": 0, "rent": 0, "index": 12},
        13: {"name": "Residence on Fifth", "color": "darkBlue",
            "price": 500, "rent": 30, "index": 13},
        14: {"name": "Chance", "color": "white", 
            "price": 0, "rent": 0, "index": 14},
        15: {"name": "Redhawk", "color": "white",
            "price": 200, "rent": 0, "index": 15},
        16: {"name": "The Exchange", "color": "green", 
            "price": 320, "rent": 450, "index": 16},
        17: {"name": "Chest", "color": "white", 
            "price": 0, "rent": 0, "index": 17},
        18: {"name": "Gates", "color": "green", 
            "price": 300, "rent": 390, "index": 18},
        19: {"name": "Stever", "color": "green", 
            "price": 300, "rent": 390, "index": 19},
        20: {"name": "Go to Jail", "color": "white", 
            "price": 0, "rent": 0, "index": 20},
        21: {"name": "Morewood", "color": "yellow", 
            "price": 280, "rent": 53600, "index": 21},
        22: {"name": "Hunt", "color": "white", 
            "price": 200, "rent": 0, "index": 22},
        23: {"name": "Revolution Noodle", "color": "yellow", 
            "price": 260, "rent": 330, "index": 23},
        24: {"name": "University Center", "color": "yellow", 
            "price": 260, "rent": 330, "index": 24},
        25: {"name": "Millies", "color": "white", 
            "price": 200, "rent": 0, "index": 25},
        26: {"name": "Scotties", "color": "red",
            "price": 240, "rent": 300, "index": 26},
        27: {"name": "Stack'd", "color": "red", 
            "price": 220, "rent": 250, "index": 27},
        28: {"name": "Chance", "color": "white",
            "price": 0, "rent": 0, "index": 28},
        29: {"name": "Scaife", "color": "red", 
            "price": 220, "rent": 250, "index": 29},
        30: {"name": "Free Parking", "color": "white", 
            "price": 0, "rent": 0, "index": 30},
        31: {"name": "ABP", "color": "orange", 
            "price": 200, "rent": 220, "index": 31},
        32: {"name": "Doherty", "color": "orange", 
            "price": 180, "rent": 200, "index": 32},
        33: {"name": "Chest", "color": "white", 
            "price": 0, "rent": 0, "index": 33},
        34: {"name": "Mudge", "color": "orange",
            "price": 180, "rent": 200, "index": 34},
        35: {"name": "La Prima", "color": "white",
            "price": 200, "rent": 0, "index": 35},
        36: {"name": "Shatz", "color": "pink", 
            "price": 160, "rent": 180, "index": 36},
        37: {"name": "Wean", "color": "pink",
            "price": 140, "rent": 150, "index": 37},
        38: {"name": "Sorreils", "color": "pink",
            "price": 200, "rent": 0, "index": 38},
        39: {"name": "Clyde", "color": "pink",
            "price": 140, "rent": 150, "index": 39},
    }
        return properties[self.index]
    
    def containsPoint(self, x, y):
        return (self.x <= x <= self.x + self.width and 
                self.y <= y <= self.y + self.height)
    
    def calculateRent(self):
        return self.rent
#creates the board
class Board: 
    #initializes list of tiles to make the board
    def __init__(self):
        self.tiles = []
    
    def addTile(self, i, x, y, w, h): #add all tiles to board
        tile = Tile(i, x, y, w, h,owner = None)
        self.tiles.append(tile)
    #adds all the tiles to the "board"
    def getTiles(self, app):
        self.tiles = []
        s = min(app.width, app.height)
        edge = s / 12
        corner = s / 8
        #bottom row
        self.addTile(0, 0, s - corner, corner, corner) #bottom left corner
        for i in range(1, 10):
            self.addTile(i, corner + (i - 1) * edge,
                s - corner, edge, corner)
        self.addTile(10, corner + 9 * edge,
            s - corner, corner, corner) #bottom right corner
        #right column 
        for i in range(1, 10):
            index = 10 + i
            self.addTile(index, s-corner, s-corner-i*edge, corner, edge)
        #top row
        self.addTile(20, s - corner, 0 , corner, corner) #top right corner
        for i in range(1, 10):
            index = 20 + i
            self.addTile(index, s - corner - i * edge, 0, edge, corner)
        self.addTile(30, 0, 0, corner, corner) #top left corner
        #left column 
        for i in range(1, 10): 
            index = 30 + i
            self.addTile(index, 0, corner + (i - 1) * edge, corner, edge)
    #builds board
    def getBoard(self, app):
        self.getTiles(app)
#creates player 
class Player: 
    def __init__(self, number, url, tileIndex = 10,
            money = 1500, timer = 60):
        self.tileIndex = tileIndex
        self.name = f'Player {number}'
        self.characterName = None
        self.money = money
        self.properties = []
        self.url = url
        self.timer = timer
    #draws each player on the board 
    def drawPlayer(self, board):
        if self.tileIndex < len(board.tiles):
            playerUrl =  self.url
            tile = board.tiles[self.tileIndex]
            left = tile.x + (tile.width / 4) - 30
            top = tile.y + (tile.height / 4) - 20
            drawImage(playerUrl, left, top, 
                      width = 100,height = 100)
    #moves the player based on dice
    def moveNext(self, board, steps):
        self.tileIndex = (self.tileIndex - steps) % len(board.tiles)
    #updates money based on what they land on
    def updateMoney(self, amount):
        self.money += amount
#dict of locations and their tile index
def makeLocations():
    return {
    34: 'Mudge Courtyard',
    19: 'Stever House',
    13: 'Residence on Fifth',
    21: 'Morewood',
    4: 'The Hill',
    39: 'Clyde House',
    11: 'Tepper School of Business',
    37: 'Wean Hall',
    18: 'Gates Center',
    7: 'Hunan',
    32: 'Doherty',
    24: 'Cohon University Center (CUC)',
    29: 'Scaife',
    2: 'College of Fine Arts (CFA)',
    9: 'Baker-Porter',
    23: 'Revolution Noodle',
    36: 'Schatz Dining Room',
    27: "Stack'd (Morewood basement)",
    26: "Scotty's Market",
    31: 'Au Bon Pain (ABP)',
    16: 'Exchange',
    1: 'Mr. Bulgogi (CFA side campus dining)',
    5: 'De Fer Coffee & Tea',
    15: 'Redhawk',
    25: "Millie's (CUC)",
    35: 'La Prima (multiple locations on campus)',
    38: 'Sorrells Library',
    22: 'Hunt Library'
}
