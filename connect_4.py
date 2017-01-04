# Variable stores the board
board = []

# Code to initialise the board
for x in range (6):
	row = []
	for y in range (7):
		row.append("O")
	board.append(row)

# Variable keeps track of whose turn, 0 or 1
player = 0
turn = 1
	
### Displays the current board
def display_board(input):
	for each_row in input:
		print(" ".join(each_row))

### Takes in a column, makes the move
def make_move():

	colour = ''
	if player == 0:
		colour = "R"
	else:
		colour = "B"

	move = int(raw_input("Which column? "))

	open = check_column(move)

	if open == 7:
		print("That column is full! Pick another column.")
		return make_move()
	else:
		board[open][column] = colour
		if win_condition(board, open, column):
			print("Player %s has won! Congratulations!" % (player + 1))
		else:
			player = 1 - player
			turn += 1
			return make_move()

# Finds the row (counting up from the bottom) that is open
# and returns 7 if it's full
def check_column(column):
	open = 0
	while board[open][column] != "O":
		open += 1
	return open

# Takes in a board, and also the position of the most recent move
# Then checks if the game is over
def win_condition(board, p1, p2):
	colour = board[p1][p2]
	up_down = check_direction(board, colour, 1, 0, p1, p2)
	right_left = check_direction(board, colour, 0, 1, p1, p2) 
	up_right = check_direction(board, colour, 1, 1, p1, p2)
	up_left = check_direction(board, colour, 1, -1, p1, p2)
	if up_down >= 3 or right_left >= 3 or up_right >= 3 or up_left >= 3:
		return True
	else:
		return False

# Takes in the board, the colour to check,
# and then whether to go up/down, and left/right
# and outputs the number of consecutives of that colour
# in the specified directions
def check_direction(board, colour, up_down, right_left, p1, p2):
	out = 0
	for x in range(3):
		if board[p1 + up_down*x][p2 + right_left*x] == player:
			out += 1
		else:
			break
	for x in range(3):
		if board[p1 - up_down*x][p2 - right_left*x] == player:
			out += 1
		else:
			break
	return out
