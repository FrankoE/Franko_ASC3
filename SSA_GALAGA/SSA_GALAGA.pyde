x=45
z=0
xspeed= 1.15
yspeed=10


def setup ():
    size(800,600)
    
def draw():
    background (0,0,0)
    global x
    global xspeed
    global yspeed
    y=40
    fill((z*3),(x*9),155)
    rect(z,400,100,20)

    for i in range(4):
        x+=xspeed
        for j in range(7):
            fillx=45
z=0
xspeed= 1.15
yspeed=10
board = [["0","0","0","0","0","0","0"],
         ["0","0","0","0","0","0","0"],
         ["0","0","0","0","0","0","0"],
         ["0","0","0","0","0","0","0"],
         ["0","0","0","0","0","0","0"]]
    

def setup ():
    size(800,600)
    
def draw():
    background (0,0,0)
    global x
    global xspeed
    global yspeed
    y=40
    fill((z*3),(x*5),155)
    rect(z,510,100,20)
    
    for i in range(len(board)):
            # x+=xspeed
        for j in range(len(board[1])):
            fill((z*3),(x*5),155)
            rect(j*70+x,i*60+y,60,40)
            
        y+=yspeed
    if x > 290 or x < 10:
        xspeed*=-1
    if y >490 or y<10:
      Yspeed*=-1





def keyPressed():
    global z
    if keyCode==39 and z<670:
     z+=20
    if keyCode==37 and z>30:
        z-=20
        

        rect(j*70+x,i*60+y,60,40)
            
        y+=yspeed
    if x > 290 or x < 10:
        xspeed*=-1
    if y >490 or y<10:
      yspeed*=-1





def keyPressed():
    global z
    if keyCode==39 and z<670:
     z+=20
    if keyCode==37 and z>30:
        z-=20
        