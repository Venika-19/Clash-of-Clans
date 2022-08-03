from colorama import Fore, Back, Style
from src.color import bg, fg
# class Village :




class TownHall:
    def __init__(self, x, y):
        self.points = [[x,y]]
        self.x = x
        self.under_attack =[0]
        self.y = y
        self.height = 4
        self.width = 3
        self.life = [1400]
        self.max_life = 1400
        self.pixel = [['/', '=', '\\'],
                      ['|', 'T', '|'],
                      ['|', 'T', '|'],
                      ['\\', '=', '/']]
        for i in range(4):
            for j in range(3):
                self.pixel[i][j] = fg.black(self.pixel[i][j])

class Wall:
    def __init__(self):
        self.height = 1
        self.width = 1
        self.pixel = [[Fore.BLACK + 'o' + Style.RESET_ALL]]
        self.max_life = 250
        arr = [[5,i] for i in range(19,60)]
        self.points = arr
        arr = [[i,19] for i in range(6,19)]
        for [i,j] in arr:
            self.points.append([i,j])
        arr = [[19,i] for i in range(19,60)]
        for [i,j] in arr:
            self.points.append([i,j])
        arr = [[i,60] for i in range(5,20)]
        for [i,j] in arr:
            self.points.append([i,j])
        
        arr = [[10,i] for i in range(38,45)]
        for [i,j] in arr:
            self.points.append([i,j])
        arr = [[i,38] for i in range(11,15)]
        for [i,j] in arr:
            self.points.append([i,j])
        arr = [[15,i] for i in range(38,45)]
        for [i,j] in arr:
            self.points.append([i,j])
        arr = [[i,44] for i in range(11,16)]
        for [i,j] in arr:
            self.points.append([i,j])
        
        self.life = [250 for i in range(len(self.points))]
        self.under_attack = [0 for i in range(len(self.points))]

class Cannon:
    def __init__(self, points):
        self.height = 3
        self.width = 3
        # self.points = [[12,30], [12,50],[7,40]]
        self.points = points
        self.max_life = 650
        self.life = [650 for i in range(len(self.points))]
        self.pixel = [['+', '+', '+'],
                      ['+', 'C', '+'],
                       ['+', '+', '+'], ]
        self.damage = 15
        self.check = None
        self.at_points = [[self.get_atpoints(k,i)for k in range(6) ]for i in range(len(self.points))]
        for i in range(3):
            for j in range(3):
                self.pixel[i][j] = fg.black(self.pixel[i][j])
        self.under_attack = [0 for i in range(len(self.points))]

    def war(self, obj, ind) :
    #    obj.under_attack[ind] = 1
       if obj.health[ind] < self.damage :
           obj.health[ind] = 0
           return 0
       else :        
           obj.health[ind] -= self.damage
       return 1

    def attacks(self,obj, points):
        for att in points:
           for ind in range(len(obj.points)):
                # self.check = [att, obj.points[ind]]
                if att == obj.points[ind] and obj.health[ind] > 0:
                    return ind   

    def get_atpoints(self, val, ind):
        x = self.points[ind][0] + 1
        y = self.points[ind][1] + 1
        points = []
        arr = [ [i*j, (val - i)*j ] for i in range(val + 1) for j in [1,-1] ]
        for i,j in arr :
            if i + x < 30 and i +x >= 0 and j + y < 80 and j + y >= 0 :
                points.append([i+x,j+y])
        return points

    def target(self,board):
        
        self.check = 1
        for i in range(len(self.points)) :
            if(self.life[i] > 0) : 
                for k in range(6):   
                    ind = self.attacks(board.bb, self.at_points[i][k])
                    if ind != None:
                        self.war(board.bb,ind)
                        board.bb.under_attack[ind] = 1
                        return i
                    ind = self.attacks(board.ruler, self.at_points[i][k])
                    if ind != None:
                        board.ruler.under_attack[ind] = 1
                        self.war(board.ruler,ind)
                        return i
                    ind = self.attacks(board.arch, self.at_points[i][k])
                    if ind != None:
                        board.arch.under_attack[ind] = 1
                        self.war(board.arch,ind)
                        return i

class Hut:
    def __init__(self, points):
        self.height = 3
        self.width = 3
        # self.points = [[16,40], [16,30],[16,50],[7,30],[7,50]]
        self.points = points
        self.life = [750 for i in range(len(self.points))]
        self.max_life = 750
        self.pixel = [['/', '-', '\\'],
                      ['|', 'H', '|'],
                      ['\\', '-', '/'], ]
        for i in range(3):
            for j in range(3):
                self.pixel[i][j] = fg.black(self.pixel[i][j])
        self.under_attack = [0 for i in range(len(self.points))]
        

class Spawning_points:
    def __init__(self):
        self.pts = [[25,70],[2,40],[10,10]]
        self.pixel = Fore.BLACK + Back.CYAN + 'S' + Style.RESET_ALL

        

class Wizard_tower:
    def __init__(self, points):
        self.height = 3
        self.width = 3
        self.points = points
        self.max_life = 650
        self.life = [650 for i in range(len(self.points))]
        self.pixel = [['W', 'w', 'W'],
                      ['w', 'W', 'w'],
                      ['W', 'w', 'W'], ]
        self.damage = 15
        self.check = None
        self.at_points = [[self.get_atpoints(k,i)for k in range(6) ]for i in range(len(self.points))]
        for i in range(3):
            for j in range(3):
                self.pixel[i][j] = fg.black(self.pixel[i][j])
        self.under_attack = [0 for i in range(len(self.points))]

    def war(self, obj, ind) :
    #    obj.under_attack[ind] = 1
       if obj.health[ind] < self.damage :
           obj.health[ind] = 0
           return 0
       else :        
           obj.health[ind] -= self.damage
       return 1

    def attacks(self,obj, points):
        for att in points:
           for ind in range(len(obj.points)):
                self.check = [att, obj.points[ind]]
                if att == obj.points[ind] and obj.health[ind] > 0:
                    return [ind ,att]  

    def get_atpoints(self, val, ind):
        x = self.points[ind][0] + 1
        y = self.points[ind][1] + 1
        points = []
        arr = [ [i*j, (val - i)*j ] for i in range(val + 1) for j in [1,-1] ]
        for i,j in arr :
            if i + x < 30 and i +x >= 0 and j + y < 80 and j + y >= 0 :
                points.append([i+x,j+y])
        return points

    def aoe(self,board, pt, num):
        points = self.get_atpoints(1,num)
        ind = self.attacks(board.bb, points)
        if ind != None:
            self.war(board.bb,ind[0])
            board.bb.under_attack[ind[0]] = 1
        ind = self.attacks(board.ruler, points)
        if ind != None:
            board.ruler.under_attack[ind[0]] = 1
            self.war(board.ruler,ind[0])
        ind = self.attacks(board.bal, points)
        if ind != None:
            board.bal.under_attack[ind[0]] = 1
            self.war(board.bal,ind[0])
        ind = self.attacks(board.arch,points)
        if ind != None:
            board.arch.under_attack[ind[0]] = 1
            self.war(board.arch,ind[0])

    def target(self,board):
        
        for i in range(len(self.points)) :
            if(self.life[i] > 0) : 
                for k in range(6):   
                    ind = self.attacks(board.bb, self.at_points[i][k])
                    if ind != None:
                        self.war(board.bb,ind[0])
                        board.bb.under_attack[ind[0]] = 1
                        self.aoe(board,ind[1],i)
                        return i
                    ind = self.attacks(board.ruler, self.at_points[i][k])
                    if ind != None:
                        board.ruler.under_attack[ind[0]] = 1
                        self.war(board.ruler,ind[0])
                        self.aoe(board,ind[1],i)
                        return i
                    ind = self.attacks(board.bal, self.at_points[i][k])
                    if ind != None:
                        board.bal.under_attack[ind[0]] = 1
                        self.war(board.bal,ind[0])
                        self.aoe(board,ind[1],i)
                        return i
                    ind = self.attacks(board.arch, self.at_points[i][k])
                    if ind != None:
                        board.arch.under_attack[ind[0]] = 1
                        self.war(board.arch,ind[0])
                        self.aoe(board,ind[1],i)
                        return i

def heal_spell(board):
        board.ruler.health[0] = min(board.ruler.max_health, int(board.ruler.health[0] * 1.5))
        board.bb.health = [min(board.bb.max_health, int(i * 1.5)) for i in board.bb.health]
        board.arch.health = [min(board.arch.max_health, int(i * 1.5)) for i in board.arch.health]
        board.bal.health = [min(board.bal.max_health, int(i * 1.5)) for i in board.bal.health]
def rage_spell(board) :
        initial_time = board.tim
        board.ruler.speed*=2
        board.ruler.damage*=2
        board.bb.speed*=2
        board.bb.damage*=2
        board.arch.damage*=2
        board.bal.damage*=2
                        