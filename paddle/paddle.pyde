from random import *
x=randrange(480)
y=randrange(480)

xspeed=3
yspeed=5
def setup():
    size(500,500)
    background(0,0,0)
    
def draw ():
   global x
   global y
   global xspeed
   global yspeed
   background(0,0,0)
   ellipse(x,y,20,20)
   x+=xspeed
   y+=yspeed
   fill(255,0,0)
   rect(mouseX,480,100,20)
   t=mouseX+100

   if x > 490 or x < 10:
     xspeed*=-1
   if y >490 or y<10:
      yspeed*=-1
   if x>mouseX and x<t and y>460:
       yspeed*=-1
   if y >480:
        fill (0,0,0)
        x=-10
        y=-10

      