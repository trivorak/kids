import os
from time import sleep
from secrets import randbelow

def clearscreen():
    os.system('clear')

def multiRoll(num):
    clearscreen()
    for i in range(num):
        clearscreen()
        for i in range(len(pArray)):
            print(f'{pArray[i]}: {parts[randbelow(len(parts))]}')
        sleep(0.015)

# Variables
pArray = []
parts = ['Eye','Horn','Pokey Hair','Leg','Arm','Mouth','Nose','Ear']
mainLoop = True

clearscreen()
print("Hello Little Monsters!")
players = input("Type All Players (Seperated by Spaces)\n")
players = players.split(' ')

for i in players:
    if i == '':
        continue
    else:
        pArray.append(i.strip())

clearscreen()
print(f'Number of players: {len(pArray)}')
sleep(1)
clearscreen()

# Main Loop
while mainLoop:
    clearscreen()
    multiRoll(20)
    input("Press ENTER for next round")
