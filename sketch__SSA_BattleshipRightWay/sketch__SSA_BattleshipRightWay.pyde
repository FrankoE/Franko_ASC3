from random import *

board = [["0","0","0","0","0"],
         ["0","0","0","0","0"],
         ["0","0","0","0","0"],
         ["0","0","0","0","0"],
         ["0","0","0","0","0"]]
#"s" stands for ship
board[(randrange(5))][randrange(5)]="ship"

def setup():
    size(500,500)
    fill(255,0,0)
def draw():
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]=="clicked":
               fill(0,0,0)
               rect(i*100,j*100,100,100)
            elif board[i][j]=="SC":
               fill(0,200,0)
               rect(i*100,j*100,100,100)
            else:
                fill(255,0,0)
                rect(i*100,j*100,100,100)
     
          
        

    
def mousePressed():
    mX=mouseX/100
    mY=mouseY/100
    if board[mX][mY]=="ship":
        board[mX][mY]="SC"
        print("s")
    else:
        board[mX][mY]="clicked"   
        print("c") 