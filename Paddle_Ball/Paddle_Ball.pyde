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
    top=horiz
    top2=horiz+10
    top3=horiz+20
    top4=horiz+30
    top4=horiz+40
    top5=horiz+50
    top6=horiz+60
    top7=horiz+70
    top8=horiz+80
    top9=horiz+90
    top10=horiz+10
    
    if xcoor<50 or xcoor>475:
        speedX*=-1
    if ycoor<50 or ycoor> 600:
        speedY*=-1
        background(255,255,255)
        ellipse(xcoor,ycoor,100,100)
    if ycoor> 475 and xcoor==top or ycoor> 475 and xcoor==top2 or ycoor> 475 and xcoor==top3 or ycoor> 475 and xcoor==top4 or ycoor> 475 and xcoor==top5 or ycoor> 475 and xcoor==top6 or ycoor> 475 and xcoor==top7 or ycoor> 475 and xcoor==top8 or ycoor> 475 and xcoor==top9 or ycoor> 475 and xcoor==top10:
        speedY*=-1
        i=i+1

    xcoor+=speedX
    ycoor+=speedY   
    print(xcoor,ycoor)
    print(i)