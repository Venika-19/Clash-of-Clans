from numpy import broadcast_arrays, true_divide
from src.getinput import get_input
from colorama import Fore, Back, Style
from src.village import TownHall, Cannon, Hut, Wall, Spawning_points
from src.color import bg
class Barbarian :
    def __init__(self):
        self.pixel = Fore.BLUE + Back.WHITE + 'b' + Style.RESET_ALL
        self.size = 0
        self.health = []
        self.damage = 10
        self.max_health = 75
        self.speed = 1
        self.points = []
        self.dest = []
        self.target = []
        self.targetobj = []
        self.indtar = []
        self.temp = []
        self.tempobj = []
        self.tempindtar = []
        self.limit = 10
        self.under_attack = []
    def war(self, obj, ind) :
        obj.under_attack[ind] = 1
        if obj.life[ind] < self.damage :
            obj.life[ind] = 0
            return 0
        else :        
            obj.life[ind] -= self.damage
        return 1

    def attacks(self,obj, points):

        for att in points:
           for ind in range(len(obj.points)):
               for i in range(obj.points[ind][0], obj.points[ind][0] +obj.height):
                   for j in range(obj.points[ind][1], obj.points[ind][1] + obj.width):
                       if att == [i,j] and obj.life[ind] > 0:
                        #    obj.under_attack[ind] = 1
                        #    if obj.life[ind] < self.damage :
                        #        obj.life[ind] = 0
                        #    else :        
                        #        obj.life[ind] -= self.damage
                           return [ind, [i,j]]

    def get_atpoints(self, val, ind):
        x = self.points[ind][0]
        y = self.points[ind][1]
        points = []
        arr = [ [i*j, (val - i)*j ] for i in range(val + 1) for j in [1,-1] ]
        for i,j in arr :
            if i + x < 30 and i +x >= 0 and j + y < 80 and j + y >= 0 :
                points.append([i+x,j+y])
        return points
    def get_target(self,board, ind):
        for k in range(80) :         
            points = self.get_atpoints(k,ind) 
            some = self.attacks(board.townhall, points)
            if some != None :
                self.target[ind] = some[1]
                self.targetobj[ind] = (board.townhall)
                self.indtar[ind] = some[0]
                return
            some = self.attacks(board.cannon, points)
            if some != None:
                self.target[ind] = (some[1])
                self.targetobj[ind] = (board.cannon)
                self.indtar[ind] = (some[0])
                return
            some = self.attacks(board.hut, points)
            if some != None:
                self.targetobj[ind] = (board.hut)
                self.indtar[ind] = some[0]
                self.target[ind] = (some[1])
                return
            some = self.attacks(board.wizard, points)
            if some != None:
               self.targetobj[ind] = (board.wizard)
               self.indtar[ind] = some[0]
               self.target[ind] = some[1]
               return
                # self.war(board.hut, self.indtar[ind])
            
    def fun(self, board, x):
        if(x == 0):
            return [25,70]
        elif x == 1 :
            return [2,40]
        else :
            return [10,10]
    def add_troop(self, x, board):
        if len(self.points) < self.limit :
            self.points.append(self.fun(board, x))
            self.target.append(None)
            self.targetobj.append(None)
            self.indtar.append(None)
            self.health.append(25)
            self.temp.append(None)
            self.tempobj.append(None)
            self.tempindtar.append(None)
            self.under_attack.append(0)
            self.get_target(board, len(board.bb.points) - 1)

    def move(self, board):
        for ind in range(len(self.points)) :
            # if self.targetobj[ind] != None:
            #     self.war(self.targetobj[ind], self.indtar[ind])
            if(self.health[ind] == 0) :
                continue
            x = self.points[ind][0]
            y = self.points[ind][1] 
            some = self.attacks(board.wall,self.get_atpoints(1,ind))           
            if x != self.target[ind][0]:
                if x - self.target[ind][0] > 0:
                    self.points[ind][0] = x - 1
                else :
                    self.points[ind][0] = x + 1 
            elif y != self.target[ind][1]:
                if y - self.target[ind][1] > 0 :
                    self.points[ind][1] = y - 1
                else :
                    self.points[ind][1] = y + 1 
            if some!= None and self.points[ind] == some[1] and board.wall.life[some[0]]!=0:
                self.points[ind][0] = x
                self.points[ind][1] = y
                self.temp[ind] = self.target[ind]
                self.target[ind] = [x,y]
                self.tempobj[ind] = self.targetobj[ind]
                self.targetobj[ind] = board.wall
                self.tempobj[ind] = board.wall
                self.tempindtar[ind] = self.indtar[ind]                    
                self.indtar[ind] = some[0]                     
            if x == self.points[ind][0] and y == self.points[ind][1] :
                set = self.war(self.targetobj[ind], self.indtar[ind])
                if set == 0:
                    if self.targetobj == board.wall :
                        self.target[ind] = self.temp[ind]
                        self.targetobj[ind] = self.tempobj[ind]
                        self.indtar[ind] = self.tempindtar[ind]
                        self.temp[ind] = None
                # set = self.war(board.wall, some[0])
                    self.get_target(board,ind)
                    



class Balloon :
    def __init__(self):
        self.pixel = Fore.RED + Back.WHITE + 'B' + Style.RESET_ALL
        self.size = 0
        self.health = []
        self.damage = 20
        self.max_health = 75
        self.speed = 1
        self.points = []
        self.dest = []
        self.target = []
        self.targetobj = []
        self.indtar = []
        self.limit = 10
        self.under_attack = []
    def war(self, obj, ind) :
        obj.under_attack[ind] = 1
        if obj.life[ind] < self.damage :
            obj.life[ind] = 0
            return 0
        else :        
            obj.life[ind] -= self.damage
        return 1

    def attacks(self,obj, points):

        for att in points:
           for ind in range(len(obj.points)):
               for i in range(obj.points[ind][0], obj.points[ind][0] +obj.height):
                   for j in range(obj.points[ind][1], obj.points[ind][1] + obj.width):
                       if att == [i,j] and obj.life[ind] > 0:
                           return [ind, [i,j]]

    def get_atpoints(self, val, ind):
        x = self.points[ind][0]
        y = self.points[ind][1]
        points = []
        arr = [ [i*j, (val - i)*j ] for i in range(val + 1) for j in [1,-1] ]
        for i,j in arr :
            if i + x < 30 and i +x >= 0 and j + y < 80 and j + y >= 0 :
                points.append([i+x,j+y])
        return points
    def get_target(self,board, ind):
        for k in range(100) :         
            points = self.get_atpoints(k,ind) 
            some = self.attacks(board.cannon, points)
            if some != None:
                self.target[ind] = (some[1])
                self.targetobj[ind] = (board.cannon)
                self.indtar[ind] = (some[0])
                return
        for k in range(100) :         
            points = self.get_atpoints(k,ind) 
            some = self.attacks(board.townhall, points)
            if some != None :
                self.target[ind] = some[1]
                self.targetobj[ind] = (board.townhall)
                self.indtar[ind] = some[0]
                return
            some = self.attacks(board.hut, points)
            if some != None:
                self.targetobj[ind] = (board.hut)
                self.indtar[ind] = some[0]
                self.target[ind] = (some[1])
                return
            some = self.attacks(board.wizard , points)
            if some != None:
                self.targetobj[ind] = (board.wizard)
                self.indtar[ind] = some[0]
                self.target[ind] = some[1]
                # self.war(board.hut, self.indtar[ind])
                return
    def fun(self, x):
        if(x == 0):
            return [25,70]
        # return board.sp.pts[x]
        elif x == 1 :
            return [2,40]
        else :
            return [10,10]
    def add_troop(self, x, board):
        if len(self.points) < self.limit :
            self.points.append(self.fun(x))
            self.target.append(None)
            self.targetobj.append(None)
            self.indtar.append(None)
            self.health.append(25)
            self.under_attack.append(0)
            self.get_target(board, len(board.bal.points) - 1)

    def move(self, board):
        for ind in range(len(self.points)) :
            # if self.targetobj[ind] != None:
            #     self.war(self.targetobj[ind], self.indtar[ind])
            if(self.health[ind] == 0) :
                continue
            x = self.points[ind][0]
            y = self.points[ind][1] 
            some = self.attacks(board.wall,self.get_atpoints(1,ind))          
            if self.target[ind] != None and x != self.target[ind][0]:
                if x - self.target[ind][0] > 0:
                    self.points[ind][0] = x - 1
                else :
                    self.points[ind][0] = x + 1 
            elif self.target[ind] != None and y != self.target[ind][1]:
                if y - self.target[ind][1] > 0 :
                    self.points[ind][1] = y - 1
                else :
                    self.points[ind][1] = y + 1              
            if x == self.points[ind][0] and y == self.points[ind][1] :
                if self.target[ind] != None :
                    set = self.war(self.targetobj[ind], self.indtar[ind])
                    if set == 0:
                        self.get_target(board,ind)
class Archer :
    def __init__(self):
        self.pixel = Fore.BLUE + Back.WHITE + 'A' + Style.RESET_ALL
        self.size = 0
        self.health = []
        self.damage = 5
        self.max_health = 37
        self.speed = 1
        self.points = []
        self.dest = []
        self.target = []
        self.targetobj = []
        self.indtar = []
        self.temp = []
        self.tempobj = []
        self.tempindtar = []
        self.limit = 10
        self.under_attack = []
    def war(self, obj, ind) :
        obj.under_attack[ind] = 1
        if obj.life[ind] < self.damage :
            obj.life[ind] = 0
            return 0
        else :        
            obj.life[ind] -= self.damage
        return 1

    def attacks(self,obj, points):

        for att in points:
           for ind in range(len(obj.points)):
               for i in range(obj.points[ind][0] - 2, obj.points[ind][0] +obj.height + 2):
                   for j in range(obj.points[ind][1] - 2, obj.points[ind][1] + obj.width + 2):
                       if att == [i,j] and obj.life[ind] > 0:
                        #    obj.under_attack[ind] = 1
                        #    if obj.life[ind] < self.damage :
                        #        obj.life[ind] = 0
                        #    else :        
                        #        obj.life[ind] -= self.damage
                           return [ind, [i,j]]

    def get_atpoints(self, val, ind):
        x = self.points[ind][0]
        y = self.points[ind][1]
        points = []
        arr = [ [i*j, (val - i)*j ] for i in range(val + 1) for j in [1,-1] ]
        for i,j in arr :
            if i + x < 30 and i +x >= 0 and j + y < 80 and j + y >= 0 :
                points.append([i+x,j+y])
        return points
    def get_target(self,board, ind):
        for k in range(80) :         
            points = self.get_atpoints(k,ind) 
            some = self.attacks(board.townhall, points)
            if some != None :
                self.target[ind] = some[1]
                self.targetobj[ind] = (board.townhall)
                self.indtar[ind] = some[0]
                return
            some = self.attacks(board.cannon, points)
            if some != None:
                self.target[ind] = (some[1])
                self.targetobj[ind] = (board.cannon)
                self.indtar[ind] = (some[0])
                return
            some = self.attacks(board.hut, points)
            if some != None:
                self.targetobj[ind] = (board.hut)
                self.indtar[ind] = some[0]
                self.target[ind] = (some[1])
                return
            if some != None:
               self.targetobj[ind] = (board.wizard)
               self.indtar[ind] = some[0]
               self.target[ind] = some[1]
               return
                # self.war(board.hut, self.indtar[ind])
            
    def fun(self, board, x):
        if(x == 0):
            return [25,70]
        elif x == 1 :
            return [2,40]
        else :
            return [10,10]
    def add_troop(self, x, board):
        if len(self.points) < self.limit :
            self.points.append(self.fun(board, x))
            self.target.append(None)
            self.targetobj.append(None)
            self.indtar.append(None)
            self.health.append(25)
            self.temp.append(None)
            self.tempobj.append(None)
            self.tempindtar.append(None)
            self.under_attack.append(0)
            self.get_target(board, len(board.arch.points) - 1)

    def move(self, board):
        for ind in range(len(self.points)) :
            # if self.targetobj[ind] != None:
            #     self.war(self.targetobj[ind], self.indtar[ind])
            if(self.health[ind] == 0) :
                continue
            x = self.points[ind][0]
            y = self.points[ind][1] 
            some = board.bb.attacks(board.wall,self.get_atpoints(1,ind))           
            if x != self.target[ind][0]:
                if x - self.target[ind][0] > 0:
                    self.points[ind][0] = x - 1
                else :
                    self.points[ind][0] = x + 1 
            elif y != self.target[ind][1]:
                if y - self.target[ind][1] > 0 :
                    self.points[ind][1] = y - 1
                else :
                    self.points[ind][1] = y + 1 
            if some!= None and self.points[ind] == some[1] and board.wall.life[some[0]]!=0:
                self.points[ind][0] = x
                self.points[ind][1] = y
                self.temp[ind] = self.target[ind]
                self.target[ind] = [x,y]
                self.tempobj[ind] = self.targetobj[ind]
                self.targetobj[ind] = board.wall
                self.tempobj[ind] = board.wall
                self.tempindtar[ind] = self.indtar[ind]                    
                self.indtar[ind] = some[0]                     
            if x == self.points[ind][0] and y == self.points[ind][1] :
                set = self.war(self.targetobj[ind], self.indtar[ind])
                if set == 0:
                    if self.targetobj == board.wall :
                        self.target[ind] = self.temp[ind]
                        self.targetobj[ind] = self.tempobj[ind]
                        self.indtar[ind] = self.tempindtar[ind]
                        self.temp[ind] = None
                # set = self.war(board.wall, some[0])
                    self.get_target(board,ind)
                    


    