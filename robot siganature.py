'''CODE signature
Written by Saaif Ahmed and Jason Zhagui
7/13/16
'''
from Myro import *
#used to position the robot
init("sim")
turnBy(180)
forward(1,2)
forward(1,2)
turnBy(-135)
penDown()
#defines commonly used functions
def x():
    forward(1,1)
def y():
    turnBy(45)
def z():
    turnBy(-45)  
def b():
    backward(1,1)
def n():
    turnBy(90)
def m():
    turnBy(-90) 
def square():
    i=0
    while i<4:
        forward(1,1)
        turnBy(-90)
        i=i+1
#makes the letter c
x()
y()
x()
z()
x()
b()
y()
b()
turnBy(-135)
x()
y()
x()
n()
x()
m()
x()
#makes the letter o
square()
x()
x()
x()
#makes the letter d
def squares():
    i=0
    while i<4:
        turnBy(-90)
        forward(1,1)
        i= i+1
squares()
turnBy(90)
forward(1,2)
turnBy(180)
x()
x()
x()
#makes the letter e
n()
x()
n()
x()
m()
x()
m()
forward(1,.5)
m()
forward(1,1)
n()
forward(1,.5)
n()
x()
x()
n()
#makes the big line
forward(1,.5)
n()
i=0
while i<10:
    x()
    i=i+1
