import random

#creating the board for tic tac toe
def board_display():
  print(board['7'] + '|' + board['8'] + '|' + board['9'])
  print('-+-+-')
  print(board['4'] + '|' + board['5'] + '|' + board['6'])
  print('-+-+-')
  print(board['1'] + '|' + board['2'] + '|' + board['3'])

def pwin(boardc):
  if boardc['7'] == boardc['8'] == boardc['9'] != ' ':
    return True
  elif boardc['4'] == board['5'] == boardc['6'] != ' ':
    return True
  elif boardc['1'] == boardc['2'] == boardc['3'] != ' ':
    return True
  elif boardc['1'] == boardc['4'] == boardc['7'] != ' ':
    return True
  elif boardc['3'] == boardc['6'] == boardc['9'] != ' ':
    return True
  elif boardc['2'] == boardc['5'] == boardc['8'] != ' ':
    return True
  elif boardc['1'] == boardc['5'] == boardc['9'] != ' ':
    return True
  elif boardc['3'] == boardc['5'] == boardc['7'] != ' ':
    return True

def comp_move(board,pd):

  possibleMoves = []
  for i in board:
    if board[i] == " ":
      possibleMoves.append(i)

  move = ""
  boardcopy = {}
  for i in ['X','O']:
    for j in possibleMoves:
      boardcopy = board.copy()
      boardcopy[str(j)] = i
      if pwin(boardcopy) == True:
        move = str(j)
        return move
  
  corner = []
  for i in possibleMoves:
    if i in ['1','3','7','9']:
      corner.append(i)
  
  if corner!=[]:
    move = random.choice(corner)
    return move

  if '5' in possibleMoves:
    move = '5'
    return move

  edge = []
  for i in possibleMoves:
    if i in ['2','4','6','8']:
      edge.append(i)
  
  if edge!=[]:
    move = random.choice(edge)
  return move

while True:
  
  print("READY TO START THE TIC TAC TOE GAME?? :] \n")
  print()
  answer_1=input("Type 'y' for YES and 'n' for NO : \n")
  print()

  if answer_1=='n' or answer_1=='N':
    break

  elif answer_1=='y' or answer_1=='Y':
    print("Enter the your preference : \n")
    print("1 for Computer vs Player \n2 for Player vs Player ")
    print()
    answer_2=input()
    print()

    # if the user's choice is to play the game with his/her friend
    if answer_2=="2":

      player1=input("enter the name of the player 1 : ")
      player2=input("enter the name of the player 2 : ")

      print(player1," will be using the character 'X'.")
      print(player2," will be using the character 'O'.")

      pd={"X":player1,"O":player2}

      board = {'7': ' ' , '8': ' ' , '9': ' ' ,'4': ' ' , '5': ' ', '6': ' ' ,'1': ' ' , '2': ' ' , '3': ' ' }

      board_keys = []
      turn = pd['X']
      count = 0
      turn_1='X'

      while True:
        board_display()
        print()
        print("It's your turn," + turn + ".Move to which place?")
        print()
        move = input()
        if board[move] == ' ':
          board[move] = turn_1
          count += 1
        else:
          print("That place is already filled.\nMove to which place?")
          continue

        if count >= 5: # We need atleast 3 'X'/'O' for winning the game therefore after 'X' this block is executed to check for the winner
        # all the possible cases for winning the game is checked
          if pwin(board):
            board_display()
            print("\nGame Over.\n")
            print(f"------------- {turn} won. -------------\n")
            break

        # since there are 9 empty slots in a tic tac toe game - so if the count is equal to 9 and none of the above cases are satisfied then its is draw match
        if count == 9:
          print("\nGame Over.\n")
          print()
          print("It's a Tie!!")
          print()
          break
        if turn == pd['X']:
          turn = pd['O']
          turn_1='O'
        else:
          turn = pd['X']
          turn_1='X'

    else:# if the user's choice is to play with the computer
      player=input("enter the your name : ")
      ask=input("Which character would you like to use? ['X' or 'O'] : ")
      print()
      computer='computer'

      if ask=='x' or ask=='X':
        pd={'X':player,'O':computer}
        print(player," will be using the character 'X'.")
        print(computer," will be using the character 'O'.")
        print()
      else:
        pd={'O':player,'X':computer}
        print(computer," will be using the character 'X'.")
        print(player," will be using the character 'O'.")
        print()

      board = {'7': ' ' , '8': ' ' , '9': ' ' ,'4': ' ' , '5': ' ', '6': ' ' ,'1': ' ' , '2': ' ' , '3': ' ' }
      board_keys = []
      turn = pd['X']
      count = 0
      turn_1='X'

      while True:
        board_display()
        if turn=="computer":
          print("It's computer's turn.")
          print()
          move = comp_move(board,pd)
        else:
          print("It's your turn," + turn + ".Move to which place?")
          move=input()
          print()
        if board[move] == ' ':
          board[move] = turn_1
          count += 1
        else:
          print("That place is already filled.\nMove to which place?")
          print()
          continue
        if count >= 5:
          if pwin(board):
            board_display()
            print("\nGame Over.\n")
            print(f"------------- {turn} won. -------------\n")
            break
        
        if count == 9:
          print("\nGame Over.\n")
          print()
          print("It's a Tie!!")
          print()
          break
        if turn == pd['X']:
          turn = pd['O']
          turn_1='O'
        else:
          turn = pd['X']
          turn_1='X'

  else:# if the user enters a character other than (y,n,Y,N)
    print("Please Enter 'y' or 'n'")
    print()
    continue
