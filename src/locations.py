from cmu_graphics import *

def makeLocations():
    return {
    34: 'Mudge Courtyard',
    19: 'Stever House',
    13: 'Residence on Fifth',
    21: 'Morewood',
    4: 'The Hill',
    39: 'Clyde House',
    11: 'Tepper School of Business',
    37: 'Donner Hall',
    18: 'Gates Center',
    7: 'Baker-Porter Hall',
    32: 'Highmark Center',
    24: 'Cohon University Center (CUC)',
    29: 'Schenley Park',
    2: 'College of Fine Arts (CFA)',
    9: 'Newell Simon Hall',
    23: 'Revolution Noodle',
    36: 'Schatz Dining Room',
    27: "Stack'd (Morewood basement)",
    26: "Scotty's Market",
    31: 'Au Bon Pain (ABP)',
    16: 'Posner Hall',
    1: 'Mr. Bulgogi (CFA side campus dining)',
    5: 'De Fer Coffee & Tea',
    15: 'Scaife Hall',
    25: "Millie's (CUC)",
    35: 'La Prima (multiple locations on campus)',
    38: 'Wean Hall (Sorrells Library)',
    22: 'Hunt Library',
}

def getLocation(app):
    return app.locations[app.currentTile]
    
def main():
   runApp()
main()

    