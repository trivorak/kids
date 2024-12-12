from os import name, system
from random import randrange

numberToGuess = 0
correctAnswer = False
highSet = []
lowSet = []

def checkGuess(guess):
	global correctAnswer, highSet, lowSet

	if guess == numberToGuess:
		correctAnswer = True
		clearScreen()
	if guess > numberToGuess:
		clearScreen()
		if guess not in highSet:
			highSet.append(guess)
		highSet = sorted(highSet,reverse=False)
	if guess < numberToGuess:
		clearScreen()
		if guess not in lowSet:
			lowSet.append(guess)
		lowSet = sorted(lowSet,reverse=True)

def clearScreen():
	if name == 'nt':
		system('cls')
	else:
		system('clear')

def getNewNumber():
	return randrange(10)

def clearGuesses():
	highSet.clear()
	lowSet.clear()

def resetGame():
	clearGuesses()
	correctAnswer = False

# #Main Game Loop
while True:
	#Get a New Random Number
	clearScreen()
	numberToGuess = getNewNumber()
	resetGame()

	#Actual Game
	while correctAnswer == False:
		if len(highSet) > 0:
			print(f"Lower Than {highSet[0]}")
		if len(lowSet) > 0:
			print(f"Higher than {lowSet[0]}")

		guess = input("Guess the number between 0 - 9:\n")

		try:
			guess = int(guess)
		except:
			clearScreen()
			print(f"{guess} <- Well that's not right")
			clearScreen()
			continue

		checkGuess(guess)

	clearScreen()
	print(f"Congrats you picked the right answer: {numberToGuess}")
	input("Press Enter to Play Again")
	correctAnswer = False



