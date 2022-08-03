
from src.board import Board
import json
from time import time
from src.king import King
from src.getinput import get_input
from src.queen import Queen
from src.level import *
from os import system 
curtime = time()
lasttime = time()
board = Board(level(1))
# filename = "replay.json"
# file = open(filename,'r+')
# file_data = json.load(file)
# d = {"data" : []}
# file_data["replay"].append(d)


# def write_data(data):
#     file_data["replay"][len(file_data["replay"]) - 1]["data"].append(data)


# def store(timestamp):
#     y = {
#         "dash" : board.dash,
#         "title" : board.title,
#         "board" : board.board,# board.dash
#         "time" : timestamp
# }
# write_data(y)

# print("Choose the character(K or Q): ")
# check = None
def choose_ruler() :
    check = input("Choose the character(K or Q): ")
    if check[0] == 'K':
        board.ruler = King(25, 30)
        # print("ho")
    elif check[0] == 'Q':
        board.ruler = Queen(25, 30)
    else :
        print('Invalid input')
        choose_ruler()
choose_ruler()
# time.sleep(2)
while(True):
    check = board.move()
    percent = board.end_game()
    if check == 'q' or percent == -2 or percent == 0 or board.tim == 120:
        # file.seek(0)
        board.render(percent)
        if check == 'q':
            break
        if percent == 0 and board.level < 3:
            board.sec = 0
            board.lastTime = 0
            board.tim = 0
            lvl = board.level
            system('clear')
            board  = Board(level(lvl+1))
            choose_ruler()
            board.level = lvl + 1
            continue
        curtime = time()
        timestamp = curtime - lasttime
        lasttime = curtime
        # store(timestamp)
        # json.dump(file_data, file, indent = 4)
        break
        # store(timestamp)
        # file.seek(0)
        # json.dump(file_data, file, indent = 4)
        break
    o = board.render(percent)
    if(check != '' or o == 1):
        curtime = time()
        timestamp = curtime - lasttime
        lasttime = curtime
    # print(board.arch.targetobj)   
    # print(board.ruler.attack_points)     

        # store(timestamp)
