import random 
import time

def tic_tac_toe():
    
    turns_left = 5
    win = False
    
    def draw_grid():
        """""
        Turtle will draw grid 
        """
    
    def player_X_and_O():
        row_input = int(input("What row do you choose?: "))
        column_input = int(input("What column do you want to choose?: "))
        """""
        turtle will go to row and column and draw X 
        """
        turns_left = turns_left - 1
    
    def easyAI_X_and_O():
        random_row = random.randint(1,3)
        random_column = random.randint(1,3)
        
        """""
        turtle will go to row and column using random_row and random_column
        """
    
    def mediumAI_X_and_O():
        """""
        """
        
    def hardAI_X_and_O():
        """""
        """
        
    computer_difficulty = int(input("What difficulty do you want to play against?: \n\
1. Easy \n\
2. Medium \n\
3. Hard \n\
Choose your option (1/2/3): "))
    
    if computer_difficulty == 1:
        
        print("Rules of the game \n\
1. You must get 3 in a row in order to win the game \n\
2. If no player has 3 in a row by the end of the game it is a tie")
        time.sleep(3)
        
        while win != True and turns_left != 0:
            player_X_and_O()
            easyAI_X_and_O()
            
        if win == True:
            print("You won")
            """""
            turtle will draw "YOU WON!" on canvas
            """
        
        elif win != True and turns_left == 0:
            print("You lost")
            """""
            turtle will draw sad face 
            """
        
        else:
            print("TIE!")
            """""
            turtle will draw "TIE!" on canvas
            """
    
    if computer_difficulty == 2:
        
        print("Rules of the game \n\
1. You must get 3 in a row in order to win the game \n\
2. If no player has 3 in a row by the end of the game it is a tie")
        time.sleep(3)
        
        while win != True and turns_left != 0:
            player_X_and_O()
            mediumAI_X_and_O()
            
        if win == True:
            print("You won")
            """""
            turtle will draw "YOU WON!" on canvas
            """
        
        elif win != True and turns_left == 0:
            print("You lost")
            """""
            turtle will draw sad face 
            """
        
        else:
            print("TIE!")
            """""
            turtle will draw "TIE!" on canvas
            """
            
    if computer_difficulty == 3:
        
        print("Rules of the game \n\
1. You must get 3 in a row in order to win the game \n\
2. If no player has 3 in a row by the end of the game it is a tie")
        time.sleep(3)
        
        while win != True and turns_left != 0:
            player_X_and_O()
            mediumAI_X_and_O()
        
        if win == True:
            print("You won")
            """""
            turtle will draw "YOU WON!" on canvas
            """
        
        elif win != True and turns_left == 0:
            print("You lost")
            """""
            turtle will draw sad face 
            """
        
        else:
            print("TIE!")
            """""
            turtle will draw "TIE!" on canvas
            """
        

tic_tac_toe()
