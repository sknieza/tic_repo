import random

def main():

  # We will need to initialise and store the board state - information about 
  # where moves have been made
  board_state = get_new_board_state()

  # Since we will be using a loop to repeatedly make moves until the games end,
  # we will use a variable to track whether the game should continue.
  game_in_progress = True

  while game_in_progress:
    
    need_player_move = True
    while need_player_move:
      player_move = ask_for_user_input()
      x_coord = player_move[0]
      y_coord = player_move[1]
      if board_state[x_coord][y_coord] != " ":
        print("Invalid move, there's already a move made there!")
      else:
        need_player_move == False

    # We update the board state with the player's move
    board_state = update_board_state(board_state, player_move)

    # We check if the the player has made a winning move
    player_has_won = check_for_win(board_state)
    
    if player_has_won:
      # The player made a winning move, we need to end the game and announce it,
      # print the board state and ensure the loop ends, ending the program
      game_in_progress = False
      print("You have won!")
      print_board(board_state)

    else:
      # If the game hasn't ended, get the computer's move. The function will 
      # need to know the board state to choose a valid move
      computer_move = get_computer_move(board_state)

      # We update the board state and check if there was a win
      board_state = update_board_state(board_state, computer_move)
      computer_has_won = check_for_win(board_state)

      if computer_has_won:
        # The computer won. Do same things as when the player won
        game_in_progress = False
        print("You have won!")
        print_board(board_state)
      else: 
        print_board(board_state)


# Listing the functions we will need to implement:
def get_new_board_state():
  return [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def ask_for_user_input():
  user_input = input("Enter where to place an 'X' in the format 'x, y':")
  x = int(user_input[0])
  y = int(user_input[3])
  return [x, y, "X"]


def update_board_state(board_state, move):
  x_coordinate = move[0]
  y_coordinate = move[1]
  x_or_o = move[2]
  board_state[x_coordinate][y_coordinate] = x_or_o
  return board_state

def check_for_win(board_state):
  for checking_for in ["X", "O"]:
    for row in board_state:
    # horizontal wins
      if row[0] == row[1] == row[2] == checking_for:
        return True
    for column in [0, 1, 2]:
    # vertical wins
      if board_state[0][column] == board_state[1][column] \
      == board_state[2][column] == checking_for:
        return True
   # diagonal wins
    if board_state[0][0] == board_state[1][1] == \
    board_state[2][2] == checking_for:
      return True
    
    if board_state[0][2] == board_state[1][1] == \
    board_state[2][0] == checking_for:
      return True
  
  return False

def get_computer_move(board_state):
  # we will store the list of possible moves in this variable
  possible_moves = []

  # We get the list of available moves first
  for row in [0, 1, 2]:
    for column in [0, 1, 2]:
      if board_state[row][column] == " ":
        possible_moves.append([row, column, "O"])
  return random.choice(possible_moves)

def print_board(board_state):
  row_number = 0
  for row in board_state:
    print("   |   |   ")
    print(" ", row[0], " | ", row[1], " | ", row[2], sep="")
    if row_number != 2:
      print("___|___|___")
    row_number += 1
  print("\n")


main()