"""
FIT1045: Sem 1 2023 Assignment 1 
Applied 06_July
"""
import random
import os

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

def create_board(rows:int, cols: int):
	"""
	Returns a 2D list of 6 rows and 7 columns to represent
	the game board. Default cell value is 0.

	:return: A 2D list of 6x7 dimensions.
	"""
	board = []
	
	# Prints a 2D array of 7 for 6 times
	for i in range (rows):
		row = []
		for k in range (cols):
			row.append(0)
		board.append(row)
	return board

def print_board(board):
	"""
	Prints the game board to the console.

	:param board: The game board, 2D list of 6x7 dimensions.
	:return: None
	"""
	
	# Print the 'header' section for the board
	print("========== Connect4 =========")
	print("Player 1: X",'     ',"Player 2: O\n")
	print("  1   2   3   4   5   6   7")
	print(" ---" * 7)

	# For loop prints the row dividers
	for row in range (0, 6, 1):
		# The first 'wall' to print for each row
		print("|", end='') 

		# For loop prints the columns and updates each cell of the column with the correct value corresponding to the player 
		for cells in range (0, 7, 1):
			# Print 'blank' if the cell is equal to zero
			if board[row][cells] == 0:
				print("   |", end='') 
			# Print 'X' if the cell is filled with 1
			elif board[row][cells] == 1: 
				print(" X |", end='')
			elif board[row][cells] == 2: # Print 'O' if the cell is filled with 2
				print(" O |", end='') 

		# The base for each row
		print('')
		print(" ---" * 7)

	# 'Footer' section for the board
	print("=============================")

def drop_piece(board, player, column):
	"""
	Drops a piece into the game board in the given column.
	
	Looping of counter is used to check for empty cells for a piece to be played.

	:param board: The game board, 2D list of 6x7 dimensions.
	:param player: The player who is dropping the piece, int.
	:param column: The index of column to drop the piece into, int.
	:return: True if piece was successfully dropped, False if not.
	"""
	# For loop returns true if successfully dropped; False if the column is full and drop unsuccesssful
	# Check rows from bottom to top for the column selected
	for i in range (6):
		if board[5-i][column-1] == 0: # Check if the provided column is empty (starting from the bottom row)
			board[5-i][column-1] = player # Drop player piece
			return True
	return False

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
		if drop_piece(board, player, column) == True:
			result = True
		else:
			print("That column is full, please try again.") # Print error message and return False
			result = False
	return column

def end_of_game(board):
	"""
	Checks if the game has ended with a winner
	or a draw.

	1: Player 1 is winner
	2: Player 2 is winner
	3: The game is a draw
	0: Continue to next round

	:param board: The game board, 2D list of 6 rows x 7 columns.
	:return: 0 if game is not over, 1 if player 1 wins, 2 if player 2 wins, 3 if draw.
	"""
	
	# Conditions to determine the state of the game
	if check_winning(board) == (1,True): 	# Check winning returns 1 and True when player 1 wins
		print("Player 1 wins!")
		return 1
	elif check_winning(board) == (2,True): # Check winning returns 2 and True when player 2 wins
		print("Player 2 wins!")
		return 2
	elif all([cell != 0 for row in board for cell in row]): # Board is full if every row and column has a player piece 
		print("The game is a draw!")
		return 3
	else:
		return 0 # Continue game

def check_winning(board):
	"""
	Conditions to check for four winning methods. Win produced by row, column, descending diagonal 
	and ascending diagonal for both players 1 and 2. 
	
	Returns winner as player and True if conditions are fulfilled.
	"""
	# Checks for both players
	for player in [1,2]:
		columns = 7
		rows = 6
		# Horizontal win conditions
		# Starts from top-left (board[0][0]) and checks until the 4th column to the right
		# Only 4 columns is checked; Past column[4], 4 in a row is impossible for row
		for c in range (columns - 3):
			for r in range (rows): # Checks every row
				if board[r][c] == player and board[r][c+1] == player and board[r][c+2] == player and board[r][c+3] == player:
					return player, True
						
		# Vertical win conditions
		# Starts from top-left (board[0][0]) and checks 3 rows from the top
		# Only 3 rows is checked; Past row[3], 4 in a row is impossible for column
		for c in range (columns): # Checks every column
			for r in range (rows - 3):
				if board[r][c] == player and board[r+1][c] == player and board[r+2][c] == player and board[r+3][c] == player:
					return player, True

		# Descending diagonal win conditions
		# Starts from board[0][0] and checks for diagonal 4 in a row going in the negative direction.
		# Only values in 4 columns and 3 rows is checked; Past that range, negative diagonal win is impossible.
		for c in range (columns - 3): # Check columns[0, 1, 2, 3]
			for r in range (rows - 3): # Check rows[0, 1, 2]
				if board[r][c] == player and board[r+1][c+1] == player and board[r+2][c+2] == player and board[r+3][c+3] == player:
					return player, True

		# Ascending diagonal win conditions
		# Starts from board[0][3] and checks for diagonal 4 in a row going in the negative direction.
		# Only values in 4 columns and 3 rows is checked; Past that range, positive diagonal win is impossible.
		for c in range (3, columns): # Check columns[3, 4, 5, 6]
			for r in range (rows - 3): # Check rows[0, 1, 2]
				if board[r][c] == player and board[r+1][c-1] == player and board[r+2][c-2] == player and board[r+3][c-3] == player:
					return player, True
	return False

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
	print("3. Play a game against the computer")
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
				local_2_player_game()
				selection = False
			elif options == 3: # Play against cpu
				game_against_cpu()
				selection = False
			elif options == 4: # Exit game
				clear_screen()
				selection = False
				break
		else:
			print("Please try again.")

def cpu_player_easy(board, player):
	"""
	Executes a move for the CPU on easy difficulty. This function 
	plays a randomly selected column.

	:param board: The game board, 2D list of 6x7 dimensions.
	:param player: The player whose turn it is, integer value of 1 or 2.
	:return: Column that the piece was dropped into, int.
	"""
	# A while loop is used to generate a random column between 1 - 7
	# The random column is played if the play is a valid move
	while True:
		cpu_random_drop = random.randint(1, 7)
		if drop_piece(board, player, cpu_random_drop) == True: #if you can drop
			return cpu_random_drop


def cpu_player_medium(board, player):
    """
    Executes a move for the CPU on medium difficulty. 
    It first checks for an immediate win and plays that move if possible. 
    If no immediate win is possible, it checks for an immediate win 
    for the opponent and blocks that move. If neither of these are 
    possible, it plays a random move.

    :param board: The game board, 2D list of 6x7 dimensions.
    :param player: The player whose turn it is, integer value of 1 or 2.
    :return: Column that the piece was dropped into, int.
    """
    columns = 7
    # Assuming CPU is always player 2
    if player == 1:
        opponent = 2
    else:
        opponent = 1

    # Duplicate a board to play a piece in trial and error method to see if opponent has a winnning pattern that can be produced
    for c in range(columns):
		# A cpu piece is dropped into columns 1 - 7 consecutively, if the duplicate board returns a winning move for cpu,
		# Play the move to win and return the column
        duplicate_board = [row[:] for row in board]  # Creates a temporary board identical to the game board
        if drop_piece(duplicate_board, player, c + 1) == True: # Drop a piece staring from column 1 - 7
            if end_of_game(duplicate_board) == (player): # If a win is determined in the duplicate board, play the move to win in the actual board
                drop_piece(board, player, c + 1)
                return c + 1

    # The same concept applies but checks for opponent pieces that has a winning pattern and cpu play a piece to block it
    for c in range(columns):
		# An opponent piece is dropped into columns 1 - 7 consecutively, if the duplicate board returns a winning move for opponent,
		# Play the move to block opponent from winning and return the column 
        duplicate_board2 = [row[:] for row in board]
        if drop_piece(duplicate_board2, opponent, c + 1) == True:
			# If opponent wins in the duplicate board, play the move in the same column to block the win in the actual board
            if end_of_game(duplicate_board2) == (opponent): 
                drop_piece(board, player, c + 1)
                return c + 1

    # Plays a random move if neither a win move or block move is valid
    return cpu_player_easy(board, player)

def cpu_player_hard(board, player):
    """
    Executes a move for the CPU on hard difficulty.
    This function creates a copy of the board to simulate moves.

	Middle column: The center-most column in the board
    Center columns: (middle column -1),(middle column),(middle column +1)

	cpu_player_hard is an improved version of cpu_player_medium, hence its top priority is to also 
	determine patterns to score a win followed by to prevent the win of the opponent if the former is 
	unavailable.

	Our implementation of cpu_player_hard lets the cpu to be the first player as it is part of our strategy
	of winning.

	The core strategy to our approach of cpu_player_hard is to take control of the center columns (as defined above).
	As our cpu always has the first move, this allows it to always start at the board[0][4]. This move prevents the opponent
	from scoring a horizontal win in the first few rounds since vertical win would be blocked in all scenarios.

	The control of the center columns allows more flexibility to The control of the center columns allows more flexibility to 
	execute a 4 in a row as horizontal and diagonal win cannot happen without the center columns allowing a higher winning rate.

	The last resort of cpu_player_hard is to call back cpu_player_medium that checks for any possbility of a win/block move,
	or else play a random piece in the available columns.

    :param board: The game board, 2D list of 6x7 dimensions.
    :param player: The player whose turn it is, integer value of 1 or 2.
    :return: Column that the piece was dropped into, int.
    """
	# Set the opponent to always be opposite of player
    if player == 1:
        opponent = 2
    else:
        opponent = 1
    columns = 7
    rows = 6

	# We set CPU is player 1 (in execute_cpu_player_hard) and always goes first, so opponent is always player 2
    # First turn, drop into middle column
    if sum(board[rows-1][:]) == 0:
        drop_piece(board, 1, 4)
        global middle_col
        middle_col = 4 # Will be used in latter rule to help initialise the pattern
        return 4

    # Checks for every cell and counts how many pieces have been played to determine the round number
    round_num = 0
    for r in range(6):
        for c in range(7):
            if board[r][c] != 0:
                round_num += 1

    # Determine where the opponent played at round 2 (left or right of middle column) which affects CPU hard's next move
	# CPU hard would play at the opposite side of opponent in the column closest to the center column
    if round_num == 2:
        if sum(board[rows-1][0:3]) == opponent: # Opponent played on the left
            drop_piece(board, 1, 5) 
            return 5
        elif sum(board[rows-1][4:7]) == opponent: # Opponent played on the right
            drop_piece(board, 1, 3)
            return 3
        else:
            drop_piece(board, 1, 4) # If opponent played on the center as well, CPU will drop on center too
            return 4

    # Similar method from cpu_player_medium
    # Duplicate a board to play a piece in trial and error method to see if opponent has a winnning pattern that can be produced
    for c in range(columns):
		# A cpu piece is dropped into columns 1 - 7 consecutively, if the duplicate board returns a winning move for cpu,
		# Play the move to win and return the column
        duplicate_board = [row[:] for row in board]  # creates a temporary board where pieces are dropped in every column
        if drop_piece(duplicate_board, player, c + 1) == True:
            if end_of_game(duplicate_board) == (player):
                drop_piece(board, player, c + 1)
                return c + 1

    # The same concept applies but checks for cpu pieces that blocks a winning move and play the move to block
    for c in range(columns):
		# An opponent piece is dropped into columns 1 - 7 consecutively, if the duplicate board returns a winning move for opponent,
		# Play the move to block opponent from winning and return the column 
        duplicate_board2 = [row[:] for row in board]
        if drop_piece(duplicate_board2, opponent, c + 1) == True:
			# If opponent wins in the duplicate board, play the move in the same column to block the win in the actual board
            if end_of_game(duplicate_board2) == (opponent):
                drop_piece(board, player, c + 1)
                return c + 1
	
    # Checks if the center columns (3,4,5) is full
	# Play an alternating pattern in the three center columns depending which column was played in last (The pattern is from column 4 to 3 to 5)
    if board[0][2] == 0 or board[0][3] == 0 or board[0][4] == 0:
        while drop_piece(board, player, middle_col) == False: # Conditional loop if one of the center column is full
            if middle_col == 4:
                middle_col = 3
            elif middle_col == 3:
                middle_col = 5
            elif middle_col == 5:
                middle_col = 4

        drop_now = middle_col # To save the the current value of middle_col before it is changed through the if conditions
        if middle_col == 4:
            middle_col = 3
        elif middle_col == 3:
            middle_col = 5
        elif middle_col == 5:
            middle_col = 4
        return drop_now 
		# middle_col cannot be returned because its value has already changed through the conditions
		# Instead return drop_now that saves the value of middle_col before it is changed

	# Plays a defensive move to win or block 4 in a row until the game ends if the center columns are all full
    return cpu_player_medium(board, player)

def game_against_cpu():
	"""
	Runs a game of Connect 4 against the computer.

	:return: None
	"""
	clear_screen()
	print_cpu_rules()
	valid_options = [1, 2, 3]
	selection = True
	# Loops the input until a valid input is selected
	while selection:
		options = int(input("Please select your options (1-3): "))
		if options in valid_options:
			# User is directed to the cpu difficulty they chose
			if options == 1: # CPU difficulty: Easy
				execute_cpu_player_easy()
				break
			elif options == 2: # CPU difficulty: Medium
				execute_cpu_player_medium()
				break
			elif options == 3: # CPU difficulty: Hard
				execute_cpu_player_hard()
				break
		else:
			print("Please try again.")

def print_cpu_rules():
	"""
	Prints the rules of the game against cpu.

	:return: None
	"""
	print("============ Play against CPU ============")
	print("Please select the difficulty of cpu player")
	print("1. Easy ")
	print("2. Medium")
	print("3. Hard")
	print("==========================================")

def execute_cpu_player_easy():
	"""
	Runs a game of Connect4 against easy cpu.
	Odd rounds: Player
	Even rounds: CPU
	:return: None
	"""
	# Similar execution as local_2_player() except the second player is cpu_player_easy 
	clear_screen()
	print_board(board)
	round_number = 1
	while end_of_game(board) == 0:
		if round_number % 2 == 0:
			player = 2
			column = cpu_player_easy(board, player) # This line calls cpu_player_easy to drop a random piece
			clear_screen()
			print_board(board)
			print("Player 2 (CPU) dropped a piece into column " + str(column))
			round_number += 1
		elif round_number % 2 != 0:
			player = 1
			column = execute_player_turn(player, board) # This line prompts the user for column
			clear_screen()
			print_board(board)
			print("Player 1 dropped a piece into column " + str(column))		
			round_number += 1

def execute_cpu_player_medium():
	"""
	Runs a game of Connect4 against medium cpu.
	Odd rounds: Player
	Even rounds: CPU
	:return: None
	"""
	# Similar execution as execute_cpu_player_easy() except cpu_player_easy is replaced with cpu_player_medium
	clear_screen()
	print_board(board)
	round_number = 1
	while end_of_game(board) == 0:
		if round_number % 2 == 0:
			player = 2
			column = cpu_player_medium(board, player) # This line calls cpu_player_medium to detect 3 in a row to block/win
			clear_screen()
			print_board(board)
			print("Player 2 (CPU) dropped a piece into column " + str(column))
			round_number += 1
		elif round_number % 2 != 0:
			player = 1
			column = execute_player_turn(player, board) # This line prompts the user for column
			clear_screen()
			print_board(board)
			print("Player 1 dropped a piece into column " + str(column))				
			round_number += 1

def execute_cpu_player_hard():
	"""
	Runs a game of Connect4 against hard cpu.
	Odd rounds: Player
	Even rounds: CPU
	:return: None
	"""
	# Similar execution as execute_cpu_player_easy() except cpu_player_medium is replaced with cpu_player_hard
	clear_screen()
	print_board(board)
	round_number = 1
	while end_of_game(board) == 0:
		if round_number % 2 != 0:
			player = 1
			column = cpu_player_hard(board, player) # This line calls cpu_player_hard (refer to strategy in function docstring)
			clear_screen()
			print_board(board)
			print("Player 1 (CPU) dropped a piece into column " + str(column))
			round_number += 1
		elif round_number % 2 == 0:
			player = 2
			column = execute_player_turn(player, board) # This line prompts the user for column
			clear_screen()
			print_board(board)
			print("Player 2 dropped a piece into column " + str(column))				
			round_number += 1

if __name__ == "__main__":
	board = create_board(6,7)
	main()