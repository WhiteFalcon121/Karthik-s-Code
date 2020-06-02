import numpy as np
#import site as site

#VARIABLES
#game_board_row = [[' ',' ',' '],['0','0','0'],[' ',' ',' ']]

#game_board_column = [[' ','0',' '],[' ','0',' '],[' ','0',' ']]

#game_board_diagonal1 = [['O',' ',' '],[' ','O',' '],[' ',' ','O']]

#game_board_diagonal2 = [[' ',' ','O'],[' ','O',' '],['O',' ',' ']]

#game_board = game_board_column
#game_board = game_board_diagonal1
#game_board = game_board_diagonal2
#game_board = game_board_row
#game_board = game_board_column
#game_board = game_board_diagonal1
#game_board = game_board_diagonal2

playerx = True
times_iterated = 0
game_board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
game_over = False
symbol_count_X = 0
symbol_count_O = 0
winner = ""
new_game_board = np.array(game_board)

#WELCOME PAGE
print("Welcome to the Noughts & Crosses game! This game requires two players. \n")
player1username = input("Player1 Username:")
player2username = input("Player2 Username:")

#FUNCTIONS
def check_if_board_full(game_board):
    full = True
    counter1 = 0
    counter2 = 0
    for i in range(0,3):
      for row in game_board[counter2]:
          for cell in row:
              if cell != ' ':
                  #full = False
                  counter1 += 1
                  #print(counter1)
                  full = False
                  break
      counter2 += 1 
              
    if counter1 == 9:
      full = True
      #return full
      #print(full)

    return full

   
def show_game_board(board):
    print("    0    1    2")
    for row_num, row in enumerate(board):
        print(row_num, row)
    print('\n')

def check_diagonals(board):
  z = 0
  diagonal_list = []
  while z < 3:
    diagonal_list.append(game_board[z][z])
    z += 1
  if check_all_elements(diagonal_list) == True:
    return True
  else:
    z = 0
    y = 2
    diagonal_list = []
    while z < 3 and y > -1:
      diagonal_list.append(game_board[z][y])
      z += 1
      y -= 1 
    if check_all_elements(diagonal_list) == True:
      return True

def check_all_elements(list_to_check):
  #print(list_to_check)
  counter = 0 
  for i in list_to_check:
     if i == list_to_check[0] and i != ' ':
      counter += 1
  
  #print(counter)

  if counter == len(list_to_check):
    return True

def check_all_elements_row(game_board):
  y = 0
  while y < 3:
    if check_all_elements(game_board[y]) == True:
      return True
    else:
      y += 1 

def check_all_elements_column(game_board):
  y = 0
  while y < 3:
    if check_all_elements(list(game_board[:, y])) == True:
      return True
    else:
      y += 1 

def check_who_won(playerx):
  if playerx == False:
    winner = player1username
  else:
    winner = player2username

  return winner

def end_game(game_over, check_who_won, playerx):
  print(check_who_won(playerx), "won")

#DISPLAY GAMEBOARD FOR FIRST TIME
show_game_board(game_board)

#while not game_over:
while game_over == False:

    #TAKE INPUT FOR COORDINATES
    coordinates_input_x = int(input("x coordinate"))
    coordinates_input_y = int(input("y coordinate"))

    while coordinates_input_x not in range(0, 3) or coordinates_input_y not in range(0,3) or game_board[coordinates_input_x][coordinates_input_y] != ' ':
      print("Coordinates not possible or not available.")
      coordinates_input_x = int(input("x coordinate"))
      coordinates_input_y = int(input("y coordinate"))

    #INSERT X OR 0
    if playerx == True:
        game_board[coordinates_input_x][coordinates_input_y] = "X"
    else:
        game_board[coordinates_input_x][coordinates_input_y] = "O"

    #UPDATE GAMEBOARD AND DISPLAY IT
    show_game_board(game_board)
    new_game_board = np.array(game_board)
    
    #SWITCH PLAYER
    playerx = not playerx

    #CHECK WINNING
    #CHECK WINNING BY ROW
    if check_all_elements_column(new_game_board) == True:
      game_over = True
      print("Game Over by column")
      end_game(game_over, check_who_won, playerx)
    #check winning by column  
    elif check_all_elements_row(game_board) == True:
      game_over = True
      print("Game Over by row")
      end_game(game_over, check_who_won, playerx)
    elif check_diagonals(game_board) == True:
      game_over = True
      print("Game Over Diagonally")
      end_game(game_over, check_who_won, playerx)
    else:
      if check_if_board_full(game_board) == True:
        game_over = True
        print("It's a Draw!")
        end_game(game_over, check_who_won, playerx)
 
