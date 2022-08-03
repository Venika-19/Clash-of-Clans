from numpy import broadcast_arrays, true_divide
from src.getinput import get_input
from colorama import Fore, Back, Style


class Queen():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.points = [[x, y]]
        self.pixel = Fore.BLUE + Back.WHITE + 'Q' + Style.RESET_ALL
        self.damage = 12
        self.max_health = 250
        self.health = [250]
        self.speed = 1
        self.direction = [0,1]
        self.under_attack = [0]
        self.attack_points = []
        self.name = "Queen"
        # self.check = 0
    def update_position(self):
        self.points = [[self.x, self.y]]

    # def attack(self):
        # self.pixel = Back.RED + Fore.BLUE + '8' + Style.RESET_ALL

    def get_pts(self, val):
        x = self.x - self.direction[1]*4
        y = self.y - self.direction[0]*4
        points = []
        arr = [[i*j, (val - i)*j] for i in range(val + 1) for j in [1, -1]]
        for i, j in arr:
            if i + x < 30 and i + x >= 0 and j + y < 80 and j + y >= 0:
                points.append([i+x, j+y])
        return points

    def get_attackpts(self):
        self.attack_points = [self.get_pts(k) for k in range(3)]


    def attacks_aoe(self, obj):

        for x in self.attack_points:
            for att in x :
                for ind in range(len(obj.points)):
                    for i in range(obj.points[ind][0], obj.points[ind][0] + obj.height):
                        for j in range(obj.points[ind][1], obj.points[ind][1] + obj.width):
                            # self.check = 1
                            if att == [i, j] and obj.life[ind] > 0:
                                obj.under_attack[ind] = 1
                                if obj.life[ind] < self.damage:
                                    obj.life[ind] = 0
                                else:
                                    obj.life[ind] -= self.damage
                                # self.check = 1

                                
    def target(self, board):
        self.get_attackpts()
        self.attacks_aoe(board.wall)
        self.attacks_aoe(board.townhall)
        self.attacks_aoe(board.hut)
        self.attacks_aoe(board.cannon)
        self.attacks_aoe(board.wizard)

