#!/usr/bin/python
from itertools import cycle
from time import sleep
from os import system
import os

win_lines = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'],
             ['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9'],
             ['1', '5', '9'], ['3', '5', '7']]
             

def main():
  print "main"
  lst = ["X", "O"]
  players = cycle(lst)
  board = create_board()
  winner = False
  while not winner:
    player = next(players)
    announce = "say player, " + player
    system(announce)
    get_move(player, board)
    winner = check_win(board)
  print(player)
  system(announce)
  print
  quit()

def check_win(board):
  for win in win_lines:
    if check_board_win(win, board):
      return True
    

def check_board_win(win, board):
  if board[win[0]] == board[win[1]] == board[win[2]]:
    os.system('clear')
    print_board(board)
    print("WINNER!!!")
    system('say we have a winner winner winner')
    return True
  else:
    return False

def print_board(board):
  print
  print(" %s | %s | %s" % (board['1'], board['2'], board['3']))
  print("-------------")
  print(" %s | %s | %s" % (board['4'], board['5'], board['6']))
  print("-------------")
  print(" %s | %s | %s" % (board['7'], board['8'], board['9']))
  print


'''
1234567890123
 1 |  2 |  3 
-------------
 4 |  5 |  6 
-------------
 7 |  8 |  9 
'''

def get_move(player, board):
  available_spaces = get_empty_spaces(board)
  if len(available_spaces) == 0:
    os.system('clear')
    print_board(board)
    print("WINNER CAT!!!\n\nLet's Try Again...\n")
    sleep(5)
    main()
  move = get_selection(player, available_spaces, board)
  board[move] = player

def get_selection(player, choices, board):
  print("get selection")
  choices.sort()
  valid_selection = None
  warning=''
  while valid_selection is None:
    os.system('clear')
    print_board(board)
    print(warning)
    selection = raw_input("Player %s choose an available space:\n %s  : " % (player, choices))
    if selection in choices:
      return selection
    else:
      warning = 'TRY AGAIN!!!'

def get_empty_spaces(board):
  empty_spaces = [] 
  for key, value in board.iteritems(): 
    if int(key) == value:
      empty_spaces.append(key)
  return empty_spaces

def create_board():
  # create dict board
  board = { '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9}
#  board = { '1' : 'X', '2' : 'X', '3' : 'X', '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9}
  return board

if __name__ == "__main__":
  main()
