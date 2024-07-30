#!/usr/bin/env python3

import os
from time import sleep
from secrets import randbelow

def clearscreen():
    os.system('clear')

def fakeRolls(num):
    clearscreen()
    for i in range(num):
        for i in range(len(pArray)):
            print(f'{pArray[i]}: {parts[randbelow(len(parts))]}')
        sleep(0.015)
        clearscreen()

def printResults():
    pass

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

while mainLoop:
    clearscreen()

    fakeRolls(20)
    for i in range(len(pArray)):
        randSelection = randbelow(len(parts))
        print(f'{pArray[i]}: {parts[randSelection]}')

    input("Press ENTER for next round")
