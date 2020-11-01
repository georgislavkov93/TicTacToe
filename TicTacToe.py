from random import randint
from time import sleep
def checkForWin(gameboard):
	for eachRow in range(0,3):
		if gameboard[eachRow][0] == 'X' and gameboard[eachRow][1] == 'X' and gameboard[eachRow][2] == 'X':
			print("Computer wins!")
			return 2
		if gameboard[eachRow][0] == 'O' and gameboard[eachRow][1] == 'O' and gameboard[eachRow][2] == 'O':
			print("You win!")
			return 1
	for eachCol in range(0,3):
		if gameboard[0][eachCol] == 'X' and gameboard[1][eachCol] == 'X' and gameboard[2][eachCol] == 'X':
			print("Computer wins!")
			return 2
		if gameboard[0][eachCol] == 'O' and gameboard[1][eachCol] == 'O' and gameboard[2][eachCol] == 'O':
			print("You win!")
			return 1
	if (gameboard[0][0] == 'X' and gameboard[1][1] == 'X' and gameboard[2][2] == 'X') or (gameboard[0][2] == 'X' and gameboard[1][1] == 'X' and gameboard[2][0] == 'X'):
		print("Computer wins!")
		return 2
	if (gameboard[0][0] == 'O' and gameboard[1][1] == 'O' and gameboard[2][2] == 'O') or (gameboard[0][2] == 'O' and gameboard[1][1] == 'O' and gameboard[2][0] == 'O'):
		print("You win!")
		return 1
	counter = 0
	for i in range(0,3):
		for j in range(0,3):
			if gameboard[i][j] != '':
				counter += 1
	if counter == 9:
		print("It's a tie!")
		return 3
	return 0
def checkInput(userInput,gameboard):
	while(len(userInput)!=3 or userInput[1]!="," or int(userInput[0]) not in range(0,3) or int(userInput[2]) not in range(0,3)):
		print("Incorrect input, please try again: ")
		userInput = input("Enter the row and then the column in the following format: i,j:")
	row = int(userInput.split(",")[0])
	col = int(userInput.split(",")[1])
	while(gameboard[row][col] != ''):
		print("This field has already been used, please play on an empty cell ")
		userInput = input("Enter the row and then the column in the following format: i,j:")
		row = int(userInput.split(",")[0])
		col = int(userInput.split(",")[1])
	return userInput


gameBoard = [['','',''],['','',''],['','','']]

keepGoing = 1

while keepGoing != 0:

	for i in range(0,3):
		for j in range(0,3):
			print(gameBoard[i][j], end=' ')
		print("\n")

	userInput = input("Enter the row and then the column in the following format: i,j  : ")
	validUserInput = checkInput(userInput,gameBoard)
	gameBoard[int(validUserInput.split(",")[0])][int(validUserInput.split(",")[1])] = 'O'
	if checkForWin(gameBoard) in range(1,4):
		keepGoing = 0
		break
	pcRow = randint(0,2)
	pcCol = randint(0,2)
	while(gameBoard[pcRow][pcCol] != ''):
		pcRow = randint(0,2)
		pcCol = randint(0,2)
	gameBoard[pcRow][pcCol] = 'X'
	if checkForWin(gameBoard) in range(1,4):
		keepGoing = 0
		break


input("Thanks for playing! Press Enter to exit.")