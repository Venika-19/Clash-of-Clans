from os import system
from time import time
from src.getinput import get_input
# from tkinter.tix import Balloon
from numpy import percentile
from progressbar import CurrentTime, Percentage
from src.king import King
from colorama import Fore, Back, Style
from src.village import *
from src.color import bg, fg
from src.troops import *


class Board():

    def __init__(self, array):
        self.cols = 80
        self.rows = 30
        # self.king = King(25, 30)
        self.ruler = None
        self.bb = Barbarian()
        self.bal = Balloon()
        self.arch = Archer()
        self.townhall = TownHall(self.rows//2 - 4, self.cols//2)
        self.cannon = Cannon(array[0])
        self.hut = Hut(array[1])
        self.wizard = Wizard_tower(array[2])
        self.wall = Wall()
        self.sp = Spawning_points()
        self.level = 1
        self.startTime = time()
        self.lastTime = 0
        self.sec = 0
        self.currentTime = time()
        grass = Back.WHITE + Style.DIM + " " + Style.RESET_ALL
        self.board = [[grass for i in range(self.cols)]
                      for j in range(self.rows)]
        dashb = Back.YELLOW + Style.DIM + " " + Style.RESET_ALL
        self.dash = [[dashb for i in range(self.cols)] for j in range(3)]
        self.title = []
        self.target = None
        self.tim = 0
        self.aoe = 0
        # self.render(-1)

    def attack_king(self):

        self.ruler.target(self)

    def troop(self, obj):
        for c_ind in range(len(obj.points)):
            i = obj.points[c_ind][0]            
            j = obj.points[c_ind][1]            
            percent = (obj.health[c_ind])/obj.max_health
            if percent <= 0:
                # self.board[i][j] = bg.clear(obj.pixel)
                pass
            else:
                self.board[i][j] = bg.white_b(obj.pixel)
            if obj.under_attack[c_ind] == 1 :
                if percent > 0.5:
                    self.board[i][j] = bg.green_b(obj.pixel)
                elif percent <= 0.5 and percent > 0.2:
                    self.board[i][j] = bg.yellow_b(obj.pixel)
                elif percent <= 0.2 and percent > 0:
                    self.board[i][j] = bg.red_b(obj.pixel)


    def percentage(self, obj):
        for c_ind in range(len(obj.points)):
            for i in range(obj.points[c_ind][0], obj.points[c_ind][0] + obj.height):
                for j in range(obj.points[c_ind][1], obj.points[c_ind][1] + obj.width):
                    percent = (obj.life[c_ind])/obj.max_life
                    if percent <= 0:
                        self.board[i][j] = bg.clear(obj.pixel[i -
                                                              obj.points[c_ind][0]][j - obj.points[c_ind][1]])
                    else:
                        self.board[i][j] = bg.white_b(obj.pixel[i -
                                                                obj.points[c_ind][0]][j - obj.points[c_ind][1]])
                    if obj.under_attack[c_ind] == 1 :
                        if percent > 0.5:
                            self.board[i][j] = bg.green_b(obj.pixel[i -
                                                                    obj.points[c_ind][0]][j - obj.points[c_ind][1]])
                        elif percent <= 0.5 and percent > 0.2:
                            self.board[i][j] = bg.yellow_b(obj.pixel[i -
                                                                     obj.points[c_ind][0]][j - obj.points[c_ind][1]])
                        elif percent <= 0.2 and percent > 0:
                            self.board[i][j] = bg.red_b(obj.pixel[i -
                                                                  obj.points[c_ind][0]][j - obj.points[c_ind][1]])

    def rage_off(self, given):
        if(self.tim - given == -2) :
            self.ruler.speed/=2
            self.ruler.damage/=2
            self.bb.speed/=2
            self.bb.damage/=2
    def render(self, end_percent):

        system('clear')
        return_var = None
        self.currentTime = time()
        ##############
        self.title = [[bg.yellow_b(' ')
                       for i in range(self.cols)] for j in range(2)]
        str = "CLASH OF CLANS LITE"
        for i in range(30, len(str)+30):
            self.title[0][i] = bg.yellow_b(fg.red(str[i - 30]))
        str = f"Level {self.level}"
        for i in range(36, len(str)+36):
            self.title[1][i] = bg.yellow_b(fg.red(str[i - 36]))
        grass = Back.WHITE + Style.DIM + " " + Style.RESET_ALL
        self.board = [[grass for i in range(self.cols)]
                      for j in range(self.rows)]
        dashb = Back.YELLOW + Style.DIM + " " + Style.RESET_ALL
        self.dash = [[dashb for i in range(self.cols)] for j in range(5)]
        #############




        ####timer
        self.tim = self.currentTime - self.startTime
        if self.tim - self.lastTime < 0.5 and self.tim - self.lastTime > 0 :
            # self.tim = 10*self.tim + 5
            self.tim = int(self.tim) + 0.5
        else :
            self.tim = int(self.tim)
        i_cannon = None
        i_wizard = None
        if(self.tim - self.sec == 1):
            i_cannon = self.cannon.target(self)
            i_wizard = self.wizard.target(self)
            self.bb.move(self) 
            self.sec = self.tim
            # self.bb.move(self)  
        if(self.tim - self.lastTime == 0.5):
            self.arch.move(self) 
            self.bal.move(self)
            # self.bb.move(self)  
            pass
            return_var = 1
            # self.tim -=1
        timer = "Timer : %d" % (120 - int(self.tim))
        self.lastTime = self.tim
        for i in range(len(timer)):
            self.dash[0][i] = bg.yellow_b(fg.red(timer[i]))

        ### timer



        ### debug
        # str = f'Points : {self.bb.health}'
        # for i in range(16, len(str)+16):
        #     self.dash[3][i] = bg.yellow_b(str[i - 16])

        # str = f'Points : {self.cannon.life}'
        # for i in range(16, len(str)+16):
        #     self.dash[2][i] = bg.yellow_b(str[i - 16])

        #### debug


        str = f"{self.ruler.name}'s Heath %d" % self.ruler.health[0]
        for i in range(16, len(str)+16):
            self.dash[1][i] = bg.yellow_b(str[i - 16])
        tiles = int((self.ruler.health[0]/self.ruler.max_health) * 15)
        for i in range(tiles):
            self.dash[1][i] = Back.GREEN + Style.DIM + " " + Style.RESET_ALL
        str = f'Number of barbarians : {len(self.bb.points)}/{self.bb.limit}'
        for i in range(len(str)):
            self.dash[2][i] = bg.yellow_b(str[i])
        str = f'Number of archers : {len(self.arch.points)}/{self.arch.limit}'
        for i in range(len(str)):
            self.dash[3][i] = bg.yellow_b(str[i])
        str = f'Number of balloons : {len(self.bal.points)}/{self.bal.limit}'
        for i in range(len(str)):
            self.dash[4][i] = bg.yellow_b(str[i])
        # print(self.townhall.pixel[3][0])
        # townhall
        self.percentage(self.townhall)
        self.percentage(self.hut)
        self.percentage(self.cannon)
        self.percentage(self.wall)
        self.percentage(self.wizard)
        # king attack
        self.troop(self.ruler)
        self.troop(self.bb)
        self.troop(self.bal)
        self.troop(self.arch)
        if i_cannon != None:
            self.board[self.cannon.points[i_cannon][0] + 1][self.cannon.points[i_cannon]
                                                            [1] + 1] = Back.CYAN + Style.BRIGHT + 'C' + Style.RESET_ALL
        if i_wizard != None:
            self.board[self.wizard.points[i_wizard][0] + 1][self.wizard.points[i_wizard]
                                                            [1] + 1] = Back.CYAN + Style.BRIGHT + 'C' + Style.RESET_ALL
        # self.board[self.ruler.x][self.ruler.y] = self.ruler.pixel
        for i_,j_ in self.sp.pts :
            self.board[i_][j_] = self.sp.pixel
            
        if end_percent  != -1:
            if(end_percent == 0):
                str = "WON THE GAME! BRAVO"
                # grass = Back.WHITE + Style.DIM + " " + Style.RESET_ALL
                # self.board = [[grass for i in range(self.cols)]
                #       for j in range(self.rows)]
            elif end_percent == -2 :
                str = "LOST THE GAME :("
                # grass = Back.WHITE + Style.DIM + " " + Style.RESET_ALL
                # self.board = [[grass for i in range(self.cols)]
                #       for j in range(self.rows)]
            else :
                # str = "Game Over with %d %% destruction"%(100 - end_percent)
                str = ""
            for i in range(46, len(str)+46):
                self.dash[1][i] = bg.yellow_b(str[i - 46])

        print("\n".join(["".join(row) for row in self.title]))
        print("\n".join(["".join(row) for row in self.board]))
        print("\n".join(["".join(row) for row in self.dash]))
        # time.sleep(1)
        self.target = None
        self.townhall.under_attack = [0]
        self.wall.under_attack = [
            0 for i in range(len(self.wall.under_attack))]
        self.hut.under_attack = [0 for i in range(len(self.hut.under_attack))]
        self.cannon.under_attack = [
            0 for i in range(len(self.hut.under_attack))]
        self.bb.under_attack = [0 for i in range(len(self.bb.under_attack))]
        self.bal.under_attack = [0 for i in range(len(self.bal.under_attack))]
        self.wizard.under_attack = [0 for i in range(len(self.wizard.under_attack))]
        self.ruler.under_attack = [0]
        self.ruler.update_position()
    def move(self): 
        char = get_input()

        def check_wall(x):
            ind = 0
            for i in self.wall.points:
                if x == i and self.wall.life[ind] != 0:
                    return False
                ind += 1
            return True
        if(char == 'd'):
            if((self.ruler.y) < (self.cols- self.ruler.speed) and check_wall([self.ruler.x, self.ruler.y + self.ruler.speed]) and check_wall([self.ruler.x, self.ruler.y + self.ruler.speed - 1])):
                self.ruler.y = self.ruler.y+ self.ruler.speed
                self.ruler.direction = [1,0]
        elif(char == 'a'):
            if((self.ruler.y > 0) and check_wall([self.ruler.x, self.ruler.y - 1])and check_wall([self.ruler.x, self.ruler.y + self.ruler.speed - 1])):
                self.ruler.y = self.ruler.y-self.ruler.speed
                self.ruler.direction = [-1,0]
        elif(char == 's'):
            if((self.ruler.x) < (self.rows-1) and check_wall([self.ruler.x + 1, self.ruler.y])and check_wall([self.ruler.x, self.ruler.y + self.ruler.speed - 1])):
                self.ruler.x = self.ruler.x+self.ruler.speed
                self.ruler.direction = [0,-1]
        elif(char == 'w'):
            if(self.ruler.x > 0 and check_wall([self.ruler.x - 1, self.ruler.y])and check_wall([self.ruler.x, self.ruler.y + self.ruler.speed - 1])):
                self.ruler.x = self.ruler.x- self.ruler.speed
                self.ruler.direction = [0,1]
        elif (char == ' '):
            self.attack_king()
        elif(char == '1'):
            self.bb.add_troop(0, self)
        elif(char == '2'):
            self.bb.add_troop(1, self)
        elif(char == '3'):
            self.bb.add_troop(2, self)
        elif(char == '4'):
            self.bal.add_troop(0, self)
        elif(char == '5'):
            self.bal.add_troop(1, self)
        elif(char == '6'):
            self.bal.add_troop(2, self)
        elif(char == '7'):
            self.arch.add_troop(0, self)
        elif(char == '8'):
            self.arch.add_troop(1, self)
        elif(char == '9'):
            self.arch.add_troop(2, self)
        elif(char == 'h') :
            heal_spell(self)
        elif char == 'r' :
            rage_spell(self)
            self.rage_off(self.tim)
        elif char == 'k' :
            self.aoe = 1
        return char
    def end_game(self):
        total_life = 0
        max_life =0
        total_life = self.townhall.life[0]
        max_life += self.townhall.max_life
        for i in self.hut.life :
            total_life += i
            max_life += self.hut.max_life
        for i in self.cannon.life :
            total_life+=i
            max_life += self.cannon.max_life
        for i in self.wizard.life :
            total_life+=i
            max_life += self.wizard.max_life

        percent = (100 * total_life)//max_life 

        total_health = 0
        max_health = 0
        total_health = self.ruler.health[0] 
        max_health = self.ruler.max_health
        for i in self.bb.health :
           total_health += i
        for i in self.bal.health :
          total_health += i
        for i in self.arch.health :
          total_health += i
        total_limit = self.bb.limit + self.bal.limit + self.arch.limit
        total_troops = len(self.bb.points) + len(self.bal.points) + len(self.arch.points)
        if total_health == 0 and total_troops == total_limit :
            percent = -2
        return percent
  

