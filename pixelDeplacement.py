from ion import * # Gestion d'événements du clavier
from time import * # Gestion du temps
from random import *
from kandinsky import * # Gestion des pixels

class newMap:
    
    def __init__(self, mapColor):
        self.mapColor = mapColor
        
    def generate(self):
        fill_rect(0,0,320,240,self.mapColor)
        
    def gameWinScreen():
        fill_rect(0,0,320,240,(255,255,255))
        while 1:
            draw_string("You Win", 116,100)
            
    def gameOverScreen():
        fill_rect(0,0,320,240,(255,255,255))
        while 1:
            draw_string("Game Over", 116,100)
    
class newAvatar:
    
    def __init__(self, position, size, avatarColor, speed, avatarState):
        self.position = position
        self.size = size
        self.avatarColor = avatarColor
        self.speed = speed
        self.avatarState = avatarState
        
    def invoke(self):
        fill_rect(self.position.get('x'),self.position.get('y'),self.size.get("width"),self.size.get("height"),self.avatarColor)
    
    def updatePosition(self, xORy, addORremove):
        avatarColor = mapColor
        fill_rect(self.position.get('x'),self.position.get('y'),self.size.get("width"),self.size.get("height"),avatarColor)
        if addORremove == "add":
            self.position[xORy] += 10
        elif addORremove == "remove":
            self.position[xORy] -= 10
        fill_rect(self.position.get('x'),self.position.get('y'),self.size.get("width"),self.size.get("height"),self.avatarColor)
        sleep(self.speed)
    
    def control(self):
        if self.avatarState == "active":
            if keydown(KEY_RIGHT):
                self.updatePosition('x', "add")
            if keydown(KEY_LEFT):
                self.updatePosition('x', "remove")
            if keydown(KEY_DOWN):
                self.updatePosition('y', "add")
            if keydown(KEY_UP):
                self.updatePosition('y', "remove")
                
    def processDead(self):
        newMap.gameOverScreen()
        self.positionProcessing("notactive")
        
    def positionProcessing(self, avatarState):        
        actualPosition = (self.position.get('x'),self.position.get('y'))
        if actualPosition[0] == 310:
            self.processDead()
        if actualPosition[0] == 0:
            self.processDead()
        if actualPosition[1] == 210:
            self.processDead()
        if actualPosition[1] == 0:
            self.processDead()
            
def launch():
  
    # Global variables:
    global mapColor
    
    
    
    # Config (editable):
    
    #------ Map ------
    mapColor = (0,0,0)
    #-----------------
    
    #---- Avatar -----
    position = {
    'x': 160,
    'y': 110
    }
    
    size = {
    "width": 10,
    "height": 10
    }
    
    avatarColor = (218,165,32) #rgb
    speed = 0.05
    #-------------------

    theMap = newMap(mapColor)
    theMap.generate()
    avatarState = "active"
    theAvatar = newAvatar(position, size, avatarColor, speed, avatarState)
    theAvatar.invoke()
    while 1:
        theAvatar.control()
        theAvatar.positionProcessing(avatarState)
        
launch()

