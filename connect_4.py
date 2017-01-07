class Board(object):
	def __init__(self, rows, columns):
		self.board = []
		self.rows = rows
		self.columns = columns
		for x in range (rows):
			row = []
			for y in range (columns):
				row.append("O")
			self.board.append(row)
	
	### Displays the current board
	def display_board(self):
		for each_row in self.board:
			print(" ".join(each_row))

	# Takes in a board position and tells you
	# what colour is in that position
	def check_tile(self, row, col):
		if (row >= 0 and 
			row < self.rows and 
			col >= 0 and 
			col < self.columns):
			return self.board[row][col]
		else:
			return "out of range"

	def update_tile(self, row, col, colour):
		if self.check_tile(row, col) != "out of range":
			self.board[row][col] = colour

class Connect_4(object):

	def __init__(self):
		self.board = Board(6, 7)
		self.turn = 1
		self.player = 1
		self.colour = "R"

	### Takes in a column, makes the move
	def make_move(self):

		# Check that the game is not over
		if self.turn == 43:
			print("Game over!")
			return

		# Update the colour chosen
		if self.player == 1:
			self.colour = "R"
		else:
			self.colour = "B"

		# Show the player the board
		self.board.display_board()

		# Code to get the player's input
		entry = input("Which column?")
		while not (entry in ['1', '2', '3', '4', '5', '6', '7']):
			entry = input("Sorry, that wasn't a column. Pick again: ")
		move = int(entry) - 1

		open = self.check_column(move)

		if open == -1:
			print("That column is full! Pick another column.")
			self.make_move()
		else:
			self.board.update_tile(open, move, self.colour)
			if self.win_condition():
				self.board.display_board()
				print("Player %s has won! Congratulations!" % (self.player))
				return
			else:
				self.player = 3 - self.player
				self.make_move()

	# Finds the row (counting up from the bottom) that is open
	# and returns -1 if it's full
	def check_column(self, column):
		open = 5
		while self.board.check_tile(open, column) != "O":
			open -= 1
			if open == -1:
				break
		return open

	# Takes in a board and checks if the game is over
	def win_condition(self):
		win = False
		for x in range(self.board.rows):
			for y in range(self.board.columns):
				win = self.check_win_here(x, y)
				if win:
					break
			if win:
				break
		return win


	# Checks in every direction, whether you're the start of a run of 4
	def check_win_here(self, row, col):
		win = False
		directions = [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)]
		for d in directions:
			for r in range(4):
				# Checks if the tile is the wrong colour
				if self.board.check_tile(row + r*d[0], col + r*d[1]) != self.colour:
					break
				# Checks if we've had three in a row
				if r == 3:
					win = True
			if win:
				break
		return win

game = Connect_4()
game.make_move()

