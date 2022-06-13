import random 
import turtle
import time 
import os 

def battleship():
    battleship_win = False 
    
    def init_player_board():
        player_board = []
        for i in range(10):
            column = []
            for x in range(10):
                column.append("0")
            player_board.append(column)
        return player_board 
    
    def init_enemy_board():
        enemy_board = []
        for i in range(5):
            column = []
            for x in range(5):
                column.append("0")
            enemy_board.append(column)
        return enemy_board 
    
    def draw_grid():
        """""
        turtle will create 5x5 grid 
        """
        pass
    
    def draw_battleship():
        "Turtle will draw 4x1 battleship"
        pass
        
    def draw_cruiser():
        "Turtle will draw 3x1 cruiser"
        pass
    
    def draw_submarine():
        "Turtle will draw 2x1 submarine"
        pass 
    
    player_health = 9
    enemy_health = 9
    turns = 0
    
    player_board = init_player_board()
    enemy_board = init_enemy_board()
    
    for i in range(5):
        counter = 0
        enemy_board[9][2 + counter] = "1"
        counter = counter + 1
    
    for i in range(4):
        counter = 0
        enemy_board[1 + counter][1] = "2"
        counter = counter + 1
    
    for i in range(3):
        counter = 0
        enemy_board[4][4 + counter] = "3"
        counter = counter + 1
        
    for i in range(2):
        counter = 0
        enemy_board[9 + counter][3] = "4"
        counter = counter + 1
        
    print("Rules of the game \n\
1. You must destroy every single boat in order to win the game \n\
2. You must choose a location on the grid in order to call a hit \n\
3. Each space of the grid has a number associated with it \n\
the numbers start at the bottom left of the board and go up until 25 \n\
which is the top right of the board. \n\
")
    time.sleep(3)
    os.system('cls')
    
    carrier_orientation = input("What orientation would you like the ba to be? (v/h): ")
    carrier_orientation = carrier_orientation.lower()
    place_carrier_x = int(input("Please enter the X coordinate you want to position \n\
your carrier on: "))
    place_carrier_y = int(input("Please enter the Y coordinate you want to position \n\
your carrier on: "))
    
    if carrier_orientation == "h":
        for i in range(4):
            player_board[place_carrier_x - 1][place_carrier_y - 1] = "1"
            place_carrier_x = place_carrier_x + 1
            
    if carrier_orientation == "v":
        for i in range(4):
            player_board[place_carrier_x - 1][place_carrier_y - 1] = "1"
            place_carrier_y = place_carrier_y + 1
    
    battleship_orientation = input("What orientation would you like the battleship to be? (v/h): ")
    battleship_orientation = battleship_orientation.lower()
    place_battleship_x = int(input("Please enter the X coordinate you want to position \n\
your battleship on: "))
    place_battleship_y = int(input("Please enter the Y coordinate you want to position \n\
your battleship on: "))
    
    if battleship_orientation == "h":
        for i in range(4):
            player_board[place_battleship_x - 1][place_battleship_y - 1] = "1"
            place_battleship_x = place_battleship_x + 1
            
    if battleship_orientation == "v":
        for i in range(4):
            player_board[place_battleship_x - 1][place_battleship_y - 1] = "1"
            place_battleship_y = place_battleship_y + 1
            
    cruiser_orientation = input("What orientation would you like the cruiser to be? (v/h): ")
    cruiser_orientation = cruiser_orientation.lower()
    place_cruiser_x = int(input("Please enter the X coordinate you want to position \n\
your cruiser on: "))
    place_cruiser_y = int(input("Please enter the Y coordinate you want to position \n\
your cruiser on: "))
    
    if cruiser_orientation == "h":
        for i in range(4):
            player_board[place_cruiser_x - 1][place_cruiser_y - 1] = "2"
            place_cruiser_x = place_cruiser_x + 1
            
    if cruiser_orientation == "v":
        for i in range(4):
            player_board[place_cruiser_x - 1][place_cruiser_y - 1] = "2"
            place_cruiser_y = place_cruiser_y + 1
    
    submarine_orientation = input("What orientation would you like the submarine to be? (v/h): ")
    submarine_orientation = cruiser_orientation.lower()
    place_submarine_x = int(input("Please enter the X coordinate you want to position \n\
your submarine on: "))
    place_submarine_y = int(input("Please enter the Y coordinate you want to position \n\
your submarine on: "))
    
    if submarine_orientation == "h":
        for i in range(4):
            player_board[place_submarine_x - 1][place_submarine_y - 1] = "3"
            place_submarine_x = place_submarine_x + 1
            
    if submarine_orientation == "v":
        for i in range(4):
            player_board[place_submarine_x - 1][place_submarine_y - 1] = "3"
            place_submarine_y = place_submarine_y + 1
            
    return battleship_win

battleship_win = battleship()

if battleship_win == True:
    print("You won!")

if battleship_win == False:
    print("You lost!")
