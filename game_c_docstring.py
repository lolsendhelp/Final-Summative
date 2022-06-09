from game_a_docstring import *
from game_b_docstring import *
import time 
import os 
import random 

main_menu = int(input("What game would you like to play?: \n\
1. Tic Tac Toe \n\
2. Battleship? \n\
3. Exit \n\
What is your choice? (1/2): "))

if main_menu == 1:
    tic_tac_toe()
    

elif main_menu == 2:
    battleship_win = battleship()
    
    if battleship_win == True: 
        print("You won!")
        #will ask if they want to play again or play tic tac toe 

elif main_menu == 3:
    exit

else:
    exit
