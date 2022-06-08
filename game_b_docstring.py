import random 

def battleship():
    
    grid_locations_player = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    grid_locations_opponent = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    
    player_battleship_location = []
    player_cruiser_location = []
    player_submarine_location = []
    
    enemy_battleship_location = []
    enemy_cruiser_location = []
    enemy_submarine_location = []
    
    player_health = 9
    enemy_health = 9
    turns = 0
    
    def draw_grid():
        """""
        turtle will create 5x5 grid 
        """
    
    def draw_battleship():
        "Turtle will draw 4x1 battleship"
        
    def draw_cruiser():
        "Turtle will draw 3x1 cruiser"
    
    def draw_submarine():
        "Turtle will draw 2x1 submarine"
    

    
    print("Rules of the game \n\
1. You must destroy every single boat in order to win the game \n\
2. You must choose a location on the grid in order to call a hit \n\
3. Each space of the grid has a number associated with it \n\
the numbers start at the bottom left of the board and go up until 25 \n\
which is the top right of the board.")
    
    battleship_orientation = input("What orientation would you like the battleship to be? (vert/hor): ")
    battleship_orientation = battleship_orientation.lower()
    place_battleship = int(input("Please enter the location you want to position \n\
your battleship on: "))
    
    if battleship_orientation == "vert":
        for i in range(4):
            player_battleship_location = place_battleship
            place_battleship = place_battleship + 3
        grid_locations_player.remove(player_battleship_location)   
    
    if battleship_orientation == "hor":
        for i in range(4):
            player_battleship_location = place_battleship
            place_battleship = place_battleship + 1
        grid_locations_player.remove(player_battleship_location)
    
    cruiser_orientation = input("What orientation would you like the submarine to be? (vert/hor): ")
    cruiser_orientation = cruiser_orientation.lower()  
    place_cruiser = int(input("Please enter the location you want to position \n\
your cruiser on: "))
    
    if cruiser_orientation == "vert":
        for i in range(4):
            player_cruiser_location = place_cruiser
            place_cruiser = place_cruiser + 3
        grid_locations_player.remove(player_cruiser_location)
        
    if cruiser_orientation == "hor":
        for i in range(4):
            player_cruiser_location = place_cruiser
            place_cruiser = place_cruiser + 1
        grid_locations_player.remove(player_cruiser_location)
        
    submarine_orientation = input("WHat orientation would you like the submarine to be? (vert/hor): ")
    submarine_orientation = submarine_orientation.lower()
    place_submarine = int(input("Please enter the location you want to position \n\
your submarine on: "))

    if submarine_orientation == "vert":
        for i in range(4):
            player_submarine_location = place_submarine
            place_submarine = place_submarine + 3
        grid_locations_player.remove(player_submarine_location)    
        
    if submarine_orientation == "hor":
        for i in range(4):
            player_submarine_location = place_submarine
            place_submarine = place_submarine + 1
        grid_locations_player.remove(player_submarine_location)
    
    #places the 
    enemy_place_battleship = random.choice(grid_locations_opponent)
    for i in range(4):
        enemy_battleship_location = enemy_place_battleship
        enemy_place_battleship = enemy_place_battleship + 1
        
    
    
    #Start of main game 
    draw_grid()
    
    #draw the ships in the position they are supposed to be in 
    #draw_battleship()
    #draw_cruiser()
    #draw_submarine()
    
    while player_health > 0 and enemy_health > 9 and turns > 25:
        player_choice = int(input("Where do you want to hit?: "))
