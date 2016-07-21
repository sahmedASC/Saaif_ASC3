from random import *
import re
import sys
import time

board = [["0","0","0","0","0"],
         ["0","0","0","0","0"],
         ["0","0","0","0","0"],
         ["0","0","0","0","0"],
         ["0","0","0","0","0"]]

board[(int(randrange(5)))][(int(randrange(5)))] = "S"
def setup():
    size(500, 500)
    for i in range(len(board)):
        for j in range(len(board)):
            rect(i*100, j*100, 100, 100)
print (board)    
turn=0
def mousePressed():
    global board, turn
    xPos = int(mouseX/100)
    yPos = int(mouseY/100)
    if board[xPos][yPos] == "S":
        fill(0,255,0)
        rect(xPos*100,yPos*100,100,100)
        print("You won!")
    
    else:
        fill (255,10, 30) 
        rect(xPos*100, yPos*100, 100, 100) 
        print("You missed")
        turn+=1
        print(turn)
    if turn > 5:
        print("You missed too many times. Everyone has died.")
        time.sleep(3)
        sys.exit()

def draw(): 
    global board
        