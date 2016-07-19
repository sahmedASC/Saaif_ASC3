from random import *
xcoor=randrange(600)
ycoor=randrange(600)
speedX=randrange(3)
speedY=randrange(3)
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
    
    xcoor+=speedX
    ycoor+=speedY
    if xcoor<50:
        speedX*=-1
        background(255,255,255)
        ellipse(xcoor,ycoor,100,100)
    if xcoor>550:
        speedX*=-1
        background(255,255,255)
        ellipse(xcoor,ycoor,100,100)
    if ycoor<50:
        speedY*=-1
        background(255,255,255)
        ellipse(xcoor,ycoor,100,100)
    if ycoor>550:
        speedY*=-1
        background(255,255,255)
        ellipse(xcoor,ycoor,100,100)
    print(xcoor,ycoor)
            
    
    
        

               
    