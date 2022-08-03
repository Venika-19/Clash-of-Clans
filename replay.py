import json
from os import system
from time import time 
def printer(x):
    print("\n".join(["".join(row) for row in x]))
filename = 'replay.json'
entry = int(input("Please enter the replay you want to play (1 for the last one, 2 for second last) : "))
system('clear')
with open('replay.json','r+') as file :
    file_data = json.load(file)
    entry = len(file_data["replay"]) - entry
    i = file_data["replay"][entry]
    for j in range(len(i["data"])):
        start = time() 
        printer(i["data"][j]["title"])
        printer(i["data"][j]["board"])
        printer(i["data"][j]["dash"])
        while(True) :
            if (time() - start) > i["data"][j]["time"] :
                system('clear')
                break
