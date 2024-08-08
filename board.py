def __init__ (rows:int, cols: int):
	self.rows = rows
	self.cols = cols
	self.board = None
	if not self.board:
		create()

def create() -> list:
	"""
	Returns a 2D list of 6 rows and 7 columns to represent
	the game board. Default cell value is 0.

	:return: A 2D list of 6x7 dimensions.
	"""
	# Prints a 2D array of 7 for 6 times
	for i in range (self.rows):
		row = []
		for k in range (self.cols):
			row.append(0)
		self.board.append(row)
	# return self.board

def print(board) -> str:
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
	for row in range (0, self.rows, 1):
		# The first 'wall' to print for each row
		print("|", end='') 

		# For loop prints the columns and updates each cell of the column with the correct value corresponding to the player 
		for cells in range (0, self.cols, 1):
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
		print(" ---" * self.cols)

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

def end_of_game(winner: int) -> int:
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
	if winner == (1,True): 	# Check winning returns 1 and True when player 1 wins
		print("Player 1 wins!")
		return 1
	elif winner == (2,True): # Check winning returns 2 and True when player 2 wins
		print("Player 2 wins!")
		return 2
	elif all([cell != 0 for row in self.board for cell in row]): # Board is full if every row and column has a player piece 
		print("The game is a draw!")
		return 3
	else:
		return 0 # Continue game