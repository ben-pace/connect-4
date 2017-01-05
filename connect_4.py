# Variable stores the board
board = []

# Code to initialise the board
for x in range (6):
	row = []
	for y in range (7):
		row.append("O")
	board.append(row)
	
### Displays the current board
def display_board(input):
	for each_row in input:
		print(" ".join(each_row))

### Takes in a column, makes the move
def make_move(player, current_board):

	display_board(current_board)

	colour = ''
	if player == 0:
		colour = "R"
	else:
		colour = "B"

	move = int(input("Which column? "))

	open = check_column(move)

	if open == -1:
		print("That column is full! Pick another column.")
		make_move(player, current_board)
	else:
		current_board[open][move] = colour
		if win_condition(current_board):
			display_board(current_board)
			print("Player %s has won! Congratulations!" % (player + 1))
		else:
			make_move(1 - player, current_board)

# Finds the row (counting up from the bottom) that is open
# and returns -1 if it's full
def check_column(column):
	open = 5
	while board[open][column] != "O":
		open -= 1
		if open == -1:
			break
	return open

# Takes in a board and checks if the game is over
def win_condition(board):
	win = False
	for x in range(6):
		for y in range(7):
			win = check_win_here(board, x, y)
			if win:
				break
		if win:
			break
	return win


# Checks in every direction, whether you're the start of a run of 4
def check_win_here(board, row, col):
	win = False
	directions = [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)]
	tile = board[row][col]
	for direction in directions:
		for y in range(3):
			# Checks to make sure you're in range
			if (row + (y+1)*direction[0] >= 0 and 
				row + (y+1)*direction[0] <= 5 and 
				col + (y+1)*direction[1] >= 0 and 
				col + (y+1)*direction[1] <= 6):
				# Checks if the tile is the wrong colour
				if board[row + y*direction[0]][col + y*direction[1]] != tile:
					win = False
					break
				if y == 3:
					win = True
			else:
				win = False
				break
		if win:
			break
	return win



make_move(0, board)

