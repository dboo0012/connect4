import random
import os
from board import Board
# from multiplayer import local_2_player_game

def clear_screen():
	"""
	Clears the terminal for Windows and Linux/MacOS.

	:return: None
	"""
	os.system('cls' if os.name == 'nt' else 'clear')


def print_rules():
	"""
	Prints the rules of the game.

	:return: None
	"""
	print("================= Rules =================")
	print("Connect 4 is a two-player game where the")
	print("objective is to get four of your pieces")
	print("in a row either horizontally, vertically")
	print("or diagonally. The game is played on a")
	print("6x7 grid. The first player to get four")
	print("pieces in a row wins the game. If the")
	print("grid is filled and no player has won,")
	print("the game is a draw.")
	print("=========================================")

def validate_input(prompt, valid_inputs):
	"""
	Repeatedly ask user for input until they enter an input
	within a set valid of options.

	:param prompt: The prompt to display to the user, string.
	:param valid_inputs: The range of values to accept, list
	:return: The user's input, string.
	"""
	# User input is set to global so it can be called in other functions
	global user_input
	# Prompt user to enter
	user_input = input(prompt)

	# Prompts for input until a valid input is entered
	while user_input not in valid_inputs:
		print("Invalid input, please try again.")
		user_input = input(prompt)
	return user_input

def execute_player_turn(player, board):
	"""
	Prompts user for a legal move given the current game board
	and executes the move.

	:return: Column that the piece was dropped into, int.
	"""
	result = False
	while result == False:
		# Player enters a column for a piece to be played in the range of 1-7.
		valid_inputs = ["1", "2", "3", "4", "5", "6", "7"]
		prompt = ("Player " + str(player) + " , please enter the column you would like to drop your piece into: ")
		validate_input(prompt, valid_inputs)
		column = int(user_input)

		# Update cell with player piece if a valid move is executed in drop_piece(); Column selected is returned to function along with True.
		if board.drop_piece(player, column) == True:
			result = True
		else:
			print("That column is full, please try again.") # Print error message and return False
			result = False
	return column

def local_2_player_game(board):
	"""
	The method used is odd and even rounds to determine player turn. Even rounds is played by Player 2 and Odd rounds is 
	played by Player 1.
	"""
	# Clear screen and print a blank board at the start of the game
	os.system('cls' if os.name == 'nt' else 'clear')
	round_number = 1
	board.print()

	# Odd rounds are played by player 1; Even rounds are played by player 2
	# Round number starts from 1, player 1 always starts first
	# Round number is updated only when a piece was dropped successfully
	while board.end_of_game() == 0: 
		# execute_player_turn is looped to prompt inputs from both players every round until there is a winner
		if round_number % 2 == 0:
			player = 2
			column =  execute_player_turn(player, board) # Set the column to be player 2's input
			clear_screen()
			board.print()
			print("Player 2 dropped a piece into column " + str(column))
			round_number += 1
		else:
			player = 1
			column =  execute_player_turn(player, board) # Set the column to be player 1's input
			clear_screen()
			board.print()
			print("Player 1 dropped a piece into column " + str(column))
			round_number += 1

	# board.end_of_game()

def main():
	"""
	Defines the main application loop.
    User chooses a type of game to play or to exit.

	:return: None
	"""
	clear_screen()
	print("=========== Welcome to connect4 ===========")
	print("1. View rules")
	print("2. Play a local 2 player game")
	print("4. Exit")
	print("===========================================")
	valid_options = [1, 2, 3, 4]
	selection = True
	# User is prompted until a valid selection is made
	while selection:
		options = int(input("Please select your options (1-4): "))
		if options in valid_options:
			# User is directed to the section they chose
			if options == 1: # View rules
				clear_screen()
				print_rules()
				selection = False
			elif options == 2: # Play local_2_player_game
				local_2_player_game(board)
				selection = False
			elif options == 4: # Exit game
				clear_screen()
				selection = False
				break
		else:
			print("Please try again.")

if __name__ == "__main__":
	board = Board(6,7)
	main()