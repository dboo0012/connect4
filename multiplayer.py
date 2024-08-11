import os


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
	while board.end_of_game(board.check_winning) == 0: 
		# execute_player_turn is looped to prompt inputs from both players every round until there is a winner
		if round_number % 2 == 0:
			player = 2
			column =  execute_player_turn(player, board) # Set the column to be player 2's input
			clear_screen()
			print_board(board)
			print("Player 2 dropped a piece into column " + str(column))
			round_number += 1
		else:
			player = 1
			column =  execute_player_turn(player, board) # Set the column to be player 1's input
			clear_screen()
			print_board(board)
			print("Player 1 dropped a piece into column " + str(column))
			round_number += 1