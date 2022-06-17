import random 
from turtle import *
import time 
import os 
import numpy
setup(500,500)
speed(100000000000000)

bgcolor("black")

penup()
setpos(-250,-250)
pendown()

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
        for i in range(10):
            column = []
            for x in range(10):
                column.append("0")
            enemy_board.append(column)
        return enemy_board 
    
    def make_grid():
        pencolor("white")
        for i in range(10):
            for i in range(10):
                for i in range(4):
                    forward(50)
                    left(90)
                forward(50)
            backward(500)
            left(90)
            forward(50)
            right(90)
    
            penup()
            setpos(-250,-250)
            pendown()
    
    def miss(x_coord, y_coord):
        pencolor("white")
        penup()
        forward((50 * x_coord) - 50)
        left(90)
        forward((50 * y_coord) - 50)
        pendown()
        
        pensize(4)
        right(45)
        forward(70)
        backward(70)
        
        penup()
        right(45)
        forward(50)
        left(135)
        pendown()
        
        forward(70)
        backward(70)
        
        penup()
        right(135)
        setpos(-250,-250)
        pendown()
    
        
    def hit(x_coord, y_coord):
        pencolor("green")
        penup()
        forward((50 * x_coord) - 50)
        left(90)
        forward((50 * y_coord) - 50)
        pendown()
        
        pensize(4)
        right(45)
        forward(70)
        backward(70)
        
        penup()
        right(45)
        forward(50)
        left(135)
        pendown()
        
        forward(70)
        backward(70)
        
        penup()
        right(135)
        setpos(-250,-250)
        pendown()
    
    player_health = 9
    enemy_health = 9
    
    def player_choice():
        player_choice_x = int(input("What X Coordinate would you like to place your hit on?: "))
        player_choice_y = int(input("What Y coordinate would you like to place your hit on ?: "))
        
        if enemy_board[player_choice_x - 1][player_choice_y - 1] == "1":
            print("HIT! \n\
You hit their Carrier!")
            enemy_board[player_choice_x - 1][player_choice_y - 1] = "X"
            enemy_health = enemy_health - 1
            
        if enemy_board[player_choice_x - 1][player_choice_y - 1] == "2":
            print("HIT! \n\
You hit their Battleship!")
            enemy_board[player_choice_x - 1][player_choice_y - 1] = "X"
            enemy_health = enemy_health - 1
            
        if enemy_board[player_choice_x - 1][player_choice_y - 1] == "3":
            print("HIT! \n\
You hit their Cruiser!")
            enemy_board[player_choice_x - 1][player_choice_y - 1] = "X"
            enemy_health = enemy_health - 1
            
        if enemy_board[player_choice_x - 1][player_choice_y - 1] == "4":
            print("HIT! \n\
You hit their Submarine!")
            enemy_board[player_choice_x - 1][player_choice_y - 1] = "X"
            enemy_health = enemy_health - 1
        
        if enemy_board[player_choice_x - 1][player_choice_y - 1] == "0":
            print("MISS! \n\
You hit nothing!")
            enemy_board[player_choice_x - 1][player_choice_y - 1] = "X"
            miss()
        
        if enemy_board[player_choice_x - 1][player_choice_y - 1] == "X":
            print("You already hit that location!")
        
        else:
            print("Error")

    def enemy_choice():
        enemy_choice_x = random.randint(1,10)
        enemy_choice_y = random.randint(1,10)
        
        if player_board[enemy_choice_x - 1][enemy_choice_y - 1] == "1":
            print("HIT! \n\
They hit your Carrier!")
            time.sleep(2)
            os.system('cls')
            player_board[enemy_choice_x - 1][enemy_choice_y - 1] = "X"
            player_health = player_health - 1
            
        if player_board[enemy_choice_x - 1][enemy_choice_y - 1] == "2":
            print("HIT! \n\
They hit your Battleship!")
            time.sleep(2)
            os.system('cls')
            player_board[enemy_choice_x - 1][enemy_choice_y - 1] = "X"
            player_health = player_health - 1
            
        if player_board[enemy_choice_x - 1][enemy_choice_y - 1] == "3":
            print("HIT! \n\
They hit your Cruiser!")
            time.sleep(2)
            os.system('cls')
            player_board[enemy_choice_x - 1][enemy_choice_y - 1] = "X"
            player_health = player_health - 1
            
        if player_board[enemy_choice_x - 1][enemy_choice_y - 1] == "4":
            print("HIT! \n\
They hit your Submarine!")
            time.sleep(2)
            os.system('cls')
            player_board[enemy_choice_x - 1][enemy_choice_y - 1] = "X"
            player_health = player_health - 1
        
        if player_board[enemy_choice_x - 1][enemy_choice_y - 1] == "0":
            print("MISS! \n\
You hit nothing!")
            time.sleep(2)
            os.system('cls')
            player_board[enemy_choice_x - 1][enemy_choice_y - 1] = "X"
        
        if player_board[enemy_choice_x - 1][enemy_choice_y - 1] == "X":
            print("You already hit that location!")
            time.sleep(2)
            os.system('cls')
        
        else:
            print("Error")
    
    player_board = init_player_board()
    enemy_board = init_enemy_board()
    
    for i in range(5):
        enemy_board[0][0 + i] = "1"
        
    for i in range(4):
        enemy_board[1 + i][1] = "2"
    
    for i in range(3):
        enemy_board[4][2 + i] = "3"
        
    for i in range(2):
        enemy_board[2 + i][3] = "4"
    
    print("Rules of the game \n\
1. You must destroy every single boat in order to win the game \n\
2. You must choose a location on the grid in order to call a hit \n\
3. The board starts at the top left of the grid and ends at the bottom right \n\
")
    time.sleep(3)
    os.system('cls')
    
    carrier_orientation = input("What orientation would you like the carrier to be? (v/h): ")
    carrier_orientation = carrier_orientation.lower()
    place_carrier_x = int(input("Please enter the X coordinate you want to position \n\
your carrier on: "))
    place_carrier_y = int(input("Please enter the Y coordinate you want to position \n\
your carrier on: "))
    
    if carrier_orientation == "h":
        for i in range(5):
            player_board[place_carrier_y - 1][place_carrier_x - 1] = "1"
            place_carrier_x = place_carrier_x + 1
            
    if carrier_orientation == "v":
        for i in range(5):
            player_board[place_carrier_y - 1][place_carrier_x - 1] = "1"
            place_carrier_y = place_carrier_y + 1
    
    battleship_orientation = input("What orientation would you like the battleship to be? (v/h): ")
    battleship_orientation = battleship_orientation.lower()
    place_battleship_x = int(input("Please enter the X coordinate you want to position \n\
your battleship on: "))
    place_battleship_y = int(input("Please enter the Y coordinate you want to position \n\
your battleship on: "))
    
    if battleship_orientation == "h":
        for i in range(4):
            player_board[place_battleship_y - 1][place_battleship_x - 1] = "2"
            place_battleship_x = place_battleship_x + 1
            
    if battleship_orientation == "v":
        for i in range(4):
            player_board[place_battleship_y - 1][place_battleship_x - 1] = "2"
            place_battleship_y = place_battleship_y + 1
            
    cruiser_orientation = input("What orientation would you like the cruiser to be? (v/h): ")
    cruiser_orientation = cruiser_orientation.lower()
    place_cruiser_x = int(input("Please enter the X coordinate you want to position \n\
your cruiser on: "))
    place_cruiser_y = int(input("Please enter the Y coordinate you want to position \n\
your cruiser on: "))
    
    if cruiser_orientation == "h":
        for i in range(3):
            player_board[place_cruiser_y - 1][place_cruiser_x - 1] = "3"
            place_cruiser_x = place_cruiser_x + 1
            
    if cruiser_orientation == "v":
        for i in range(3):
            player_board[place_cruiser_y - 1][place_cruiser_x - 1] = "3"
            place_cruiser_y = place_cruiser_y + 1
    
    submarine_orientation = input("What orientation would you like the submarine to be? (v/h): ")
    submarine_orientation = cruiser_orientation.lower()
    place_submarine_x = int(input("Please enter the X coordinate you want to position \n\
your submarine on: "))
    place_submarine_y = int(input("Please enter the Y coordinate you want to position \n\
your submarine on: "))
    
    if submarine_orientation == "h":
        for i in range(2):
            player_board[place_submarine_y - 1][place_submarine_x - 1] = "4"
            place_submarine_x = place_submarine_x + 1
            
    if submarine_orientation == "v":
        for i in range(2):
            player_board[place_submarine_y - 1][place_submarine_x - 1] = "4"
            place_submarine_y = place_submarine_y + 1
    
    numpy.array(player_board)
    print(numpy.reshape(player_board, (10,10)))
    time.sleep(5)
    print(" ")
    numpy.array(enemy_board)
    print(numpy.reshape(enemy_board,(10,10)))
    
    while player_health > 0 and enemy_health > 0:
        player_choice()
        enemy_choice()
    
    if player_health <= 0:
        print("You lost!")
        battleship_win = False 
    
    if player_health > 0 and enemy_health <=0:
        print("You won!")
        battleship_win = True
        
    return battleship_win

battleship_win = battleship()
