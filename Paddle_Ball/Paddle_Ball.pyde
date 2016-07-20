from random import *
xcoor=randrange(100,450)
ycoor=randrange(100,450)
speedX=randrange(1,10)
speedY=randrange(1,10)
i=0
def setup():
    size(600,600)
    fill(randrange(255), randrange(255), randrange(255))
def draw():
    global xcoor
    global ycoor
    background(255,255,255)
    ellipse(xcoor,ycoor,100,100)
    global speedX
    global speedY
    global i
    rect(mouseX,525,100,50)
    horiz=mouseX
    
    top0=horiz
    top=horiz+100
    
    
    if xcoor<50 or xcoor>475:
        speedX*=-1
    if ycoor<50 or ycoor> 600:
        speedY*=-1
        background(255,255,255)
        ellipse(xcoor,ycoor,100,100)
    if ycoor> 475 and xcoor >=top0 and xcoor<=top:
        speedY*=-1
        i=i+1

    xcoor+=speedX
    ycoor+=speedY   
    print("Score is:", i)