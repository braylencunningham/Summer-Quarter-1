import pgzrun
from pgzero.actor import Actor
# Define width and height of the game grid & size of each grid tile
GRID_WIDTH = 16 # defines How many squares wide the game board is
GRID_HEIGHT = 12 # defines How many squares tall the game board is
GRID_SIZE = 50
# Define the size of the game window
WIDTH = GRID_WIDTH * GRID_SIZE
HEIGHT = GRID_HEIGHT * GRID_SIZE
#########################
########## 1.5 ##########
MAP = ["WWWWWWWWWWWWWWWW",
       "W              W",
       "W              W",
       "W  W  KG       W",
       "W  WWWW WWWWWW  W",
       "W              W",
       "W      P       W",
       "W  WWWWWWWWWW  W",
       "W      GK   W  W",
       "W              W",
       "W              D",
       "WWWWWWWWWWWWWWWW"]
#########################
########## 1.4 ##########
# This function converts a grid position to screen coordinates
def GetScreenCoords(x, y):
    return (x * GRID_SIZE, y * GRID_SIZE)
# This function draws the dungeon floor as a background on screen
def DrawBackground():
    for y in range (GRID_HEIGHT): # loop over each grid row
        for x in range (GRID_WIDTH): # loop over each grid column
            screen.blit("floor1", GetScreenCoords(x, y)) # Draws the named imaged at the given screen position
#########################
########## 2.1 ##########
# This function takes in an actor as an argument &
# returns the postion of the actor on the grid
def GetActorGridPos(actor):
    return(round(actor.x / GRID_SIZE), round(actor.y / GRID_SIZE))
#########################
########## 1.7, 3.0 ##########
# This function creates an actor object from the Actor class to reperesent the player & keys
def SetupGame():
    global player # Define player as a global var that be accessed anywhere in your code
    global keysToCollect # A var to store all the keys the player needs to collect
    global gameOver
    global guards # A var to store all the guards in the game
    player = Actor("player", anchor=("left", "top")) # Create a new Actor & set its anchor
    keysToCollect = []
    guards = [] # Create an empty list to store the guards
    gameOver = False
    for y in range(GRID_HEIGHT): # Loop over each grid position
        for x in range(GRID_WIDTH):
            square = MAP[y][x] # Extracts the character from the MAP variable
            if square == "P": # Checks if the grid position is the player
                player.pos = GetScreenCoords(x, y) # Set the position of the player
            elif square == "K":
                # Create an actor for that key
                key = Actor("key", anchor=("left", "top"))
                # Set the key's pos to this grid location
                key.pos = GetScreenCoords(x, y)
                # Add this key to our list of keys
                keysToCollect.append(key)
#########################
########## 1.6 ##########
def DrawScenery():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            square = MAP[y][x]
            if square == "W":
                screen.blit("wall", GetScreenCoords(x, y))
            elif square == "D":
                screen.blit("door", GetScreenCoords(x, y))
########## 1.8, 3.1 ##########
def DrawActors():
    player.draw()
    for key in keysToCollect:
        key.draw()
#########################
# draw() is
def DrawGameOver():
    screenMiddle = (WIDTH / 2, HEIGHT / 2)
    # Draw "Game Over" on the screen
    screen.draw.text("GAME OVER", midbottom = screenMiddle,
                     fontsize = GRID_SIZE, color="cyan", owidth=1)
def draw():
    screen.clear()
    DrawBackground()
    DrawScenery()
    DrawActors()
    if gameOver:
        DrawGameOver()
#########################
########## 2.2, 3.2 ##########
def MovePlayer(dx, dy):
    global gameOver
    if gameOver: # If the game is over, do not let the player move
        return
    (x, y) = GetActorGridPos(player)
    x += dx
    y += dy
    square = MAP[y][x]
    if square == "W": # If the player tries to move into a wall
        return # stop the function, dont let the player move
    elif square == "D":
        if len(keysToCollect) > 0: # If there are keys left to collect
            return  # do no let the player exit the door if there are keys left
        else:
            gameOver = True
    for key in keysToCollect:
        # Get the grid pos of the current key
        (keyX, keyY) = GetActorGridPos(key)
        # Check if the new player pos mathces the pos of one of the keys
        if x == keyX and y == keyY:
            keysToCollect.remove(key)
            break # Stop checking keys once one is found
    player.pos = GetScreenCoords(x,y)
#########################
########## 2.3 ##########
# This Function gets a key from the user and moves the player based on the input
def on_key_down(key):
    if key == key.LEFT:
        MovePlayer(-1, 0) # Player moves left one on the grid
    elif key == key.UP:
        MovePlayer(0, -1) # Player moves up one on the grid
    elif key == key.RIGHT:
        MovePlayer(1, 0) # Player moves right one on the grid
    elif key == key.DOWN:
        MovePlayer(0, 1) # Player moves down one on the grid
#########################
# Start the Pygame
#3.6
def SetupGame():
    global player
    global keysToCollect
    global gameOver
    global guards
    player = Actor("player", anchor=("left", "top"))
    keysToCollect = []
    gameOver = False
    guards = []
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            square = MAP[y][x]
            if square == "P":
                player.pos = GetScreenCoords(x, y)
            elif square == "K":
                key = Actor("key", anchor=("left", "top"))
                key.pos = GetScreenCoords(x, y)
                keysToCollect.append(key)
            elif square == "G":
                guard = Actor("guard", anchor=("left", "top"))
                guard.pos = GetScreenCoords(x, y)
                guards.append(guard)
####1.8, 3.1
def DrawActors():
    player.draw()
    for key in keysToCollect:
        key.draw()
    for guard in guards:
        guard.draw()
#####4.1
def MoveGuard(guard):
    global gameOver
    if gameOver:
        return
    (playerX, playerY) = GetActorGridPos(player)
    (guardX, guardY) = GetActorGridPos(guard)  # Assuming one guard for simplicity
    if playerX > guardX and MAP[guardY][guardX + 1] != "W":
        guardX += 1
    elif playerX < guardX and MAP[guardY][guardX - 1] != "W":
        guardX -= 1
    elif playerY > guardY and MAP[guardY + 1][guardX] != "W":
        guardY += 1
    elif playerY < guardY and MAP[guardY - 1][guardX] != "W":
        guardY -= 1
    guard.pos = GetScreenCoords(guardX, guardY)
    if (playerX, playerY) == (guardX, guardY):
        gameOver = True
#4.2
def MoveGuards():
    for guard in guards:
        MoveGuard(guard)
4.3
import pgzrun
GRID_WIDTH = 16
GRID_HEIGHT = 12
GRID_SIZE = 50
GUARDMOVEINTERVAL = 0.5
# Define the size of the game window
WIDTH = GRID_WIDTH * GRID_SIZE
HEIGHT = GRID_HEIGHT * GRID_SIZE
SetupGame()
clock.schedule_interval(MoveGuards, GUARDMOVEINTERVAL)
pgzrun.go()






