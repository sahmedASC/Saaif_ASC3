from random import *
#Creates the Squares
def setup():
    size (600,600)
    fill(255,0,0)
    rect(0,0,100,100)
    fill(0,255,0)
    rect(100,0,100,100)
    fill(0,0,255)
    rect(200,0,100,100)
    fill(255,255,0)
    rect(300,0,100,100)

'''
def red():
    fill(255, 0, 0)
    ellipse(mouseX,mouseY,10,10)
def blue():
    fill(0, 0, 255)
    ellipse(mouseX,mouseY,10,10)
def green():
    fill(0, 255, 0)
    ellipse(mouseX,mouseY,10,10)
def yellow():
    fill(255, 255, 0)
    ellipse(mouseX,mouseY,10,10) 
def rainbow():
    fill (randrange(255), randrange(255),randrange(255))
    ellipse(mouseX,mouseY,10,10)'''
#Allows the user to pick color and drag
def draw():
    if mouseButton == LEFT and mouseX < 100 and mouseY < 100 :
        print ("You clicked the mouse here:",mouseX,mouseY)
        fill(255,0,0)    
    elif mouseButton == LEFT and mouseX < 200 and mouseX >100 and mouseY < 100 :
        print ("You clicked the mouse here:",mouseX,mouseY)
        fill(0,255,0)
    elif mouseButton == LEFT and mouseX< 300 and mouseX > 200 and mouseY < 100:
        fill(0,0,255)
    elif mouseButton == LEFT and mouseX < 400 and mouseX>300 and mouseY<100:
        fill(255,255,0)
    if mouseButton == LEFT:
        ellipse(mouseX,mouseY,10,10)