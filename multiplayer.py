def local_2_player_game():
	"""
	The method used is odd and even rounds to determine player turn. Even rounds is played by Player 2 and Odd rounds is 
	played by Player 1.
	"""
	# Clear screen and print a blank board at the start of the game
	clear_screen()
	round_number = 1
	print_board(board)

	# Odd rounds are played by player 1; Even rounds are played by player 2
	# Round number starts from 1, player 1 always starts first
	# Round number is updated only when a piece was dropped successfully
	while end_of_game(board) == 0: 
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