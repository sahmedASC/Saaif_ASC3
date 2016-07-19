from random import *
xcoor=randrange(100,450)
ycoor=randrange(100,450)
speedX=randrange(1,5)
speedY=randrange(1,5)
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
    rect(mouseX,525,100,50)
    horiz=mouseX
    top=horiz
    i=0
    if xcoor<50 or xcoor>475:
        speedX*=-1
    if ycoor<50 or ycoor> top:
        speedY*=-1
        background(255,255,255)
        ellipse(xcoor,ycoor,100,100)
#    if top = ycoor and mouse:
#        i=i+1
    xcoor+=speedX
    ycoor+=speedY   
    print(xcoor,ycoor,i)