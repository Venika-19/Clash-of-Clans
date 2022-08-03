from numpy import broadcast_arrays, true_divide
from src.getinput import get_input
from colorama import Fore, Back, Style
from src.village import TownHall, Cannon, Hut, Wall
# from matplotlib import
from src.troops import Barbarian

class King():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.points = [[x,y]]
        self.pixel = Fore.BLUE + 'K' + Style.RESET_ALL
        self.damage = 12
        self.max_health = 250
        self.health = [250]
        self.speed = 1
        self.direction = None
        self.under_attack = [0]
        self.attack_points = []
        self.name = "King"

    def update_position(self):
        self.points = [[self.x,self.y]]

    # def attack(self):
        # self.pixel = Back.RED + Fore.BLUE + '8' + Style.RESET_ALL

    def get_attackpts(self):
        arr = [[0, 0], [0, 1], [0, -1], [1, 0], [-1, 0]]
        self.attack_points = [[i + self.x, j + self.y]
                              for i, j in arr]
    
    def attacks(self, obj):

        for att in self.attack_points:
            for ind in range(len(obj.points)):
                for i in range(obj.points[ind][0], obj.points[ind][0] + obj.height):
                    for j in range(obj.points[ind][1], obj.points[ind][1] + obj.width):
                        if att == [i, j] and obj.life[ind] > 0:
                            obj.under_attack[ind] = 1
                            if obj.life[ind] < self.damage:
                                obj.life[ind] = 0
                            else:
                                obj.life[ind] -= self.damage
                            return ind
    def attacks_aoe(self, obj):

        for att in self.attack_points:
            for ind in range(len(obj.points)):
                for i in range(obj.points[ind][0], obj.points[ind][0] + obj.height):
                    for j in range(obj.points[ind][1], obj.points[ind][1] + obj.width):
                        if att == [i, j] and obj.life[ind] > 0:
                            obj.under_attack[ind] = 1
                            if obj.life[ind] < self.damage:
                                obj.life[ind] = 0
                            else:
                                obj.life[ind] -= self.damage
                            
    def aoe_pts(self) :
        points = []
        x = self.x
        y = self.y
        for val in range(6) :
            arr = [ [i*j, (val - i)*j ] for i in range(val + 1) for j in [1,-1] ]
            for i,j in arr :
                if i + x < 30 and i +x >= 0 and j + y < 80 and j + y >= 0 :
                    points.append([i+x,j+y])

    def aoe(self, board) :
        points = self.aoe_pts
        self.attacks_aoe(board.townhall)
        self.attacks_aoe(board.hut)
        self.attacks_aoe(board.cannon)
        self.attacks_aoe(board.wizard)
    def target(self, board):
        if self.aoe == 1 :
            self.aoe(board)
            self.damage = 2
            return
        self.get_attackpts()
        if self.attacks(board.townhall) != None:
            return
        if(self.attacks(board.hut) != None):
            return
        if(self.attacks(board.cannon) != None):
            return
        if(self.attacks(board.wizard) != None):
            return
        if(self.attacks(board.wall) != None):
            return

# class Spells : 
  
            