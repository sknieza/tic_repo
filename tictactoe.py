def main():

  # We will need to initialise and store the board state - information about 
  # where moves have been made
  board_state = get_new_board_state()

  # Since we will be using a loop to repeatedly make moves until the games end,
  # we will use a variable to track whether the game should continue.
  game_in_progress = True

  while game_in_progress:
    player_move = ask_for_user_input()

    # We update the board state with the player's move
    board_state = update_board_state(board_state, player_move)
    print(board_state)
    break

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
  user_input = input("Enter where to place an 'X' in the format 'x, y'")
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
  pass

def get_computer_move(board_state):
  pass

def print_board(board_state):
  pass