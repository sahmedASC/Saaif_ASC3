#Made by Saaif Ahmed and Jason Zhagui
#Song used- Spider Dance (Undertale) by Toby Fox
#We plan to create the loops once we have the movements down for the parts
from Myro import *

#verse
x=0
s=1
while x<4:
    i=0
    while i<3:
        turnRight(s,.1)
        turnLeft(s,.2)
        turnRight(s,.2)
        turnLeft(s,.1)
        i=i+1

    forward(s,.4)
    backward(s,.4)
    forward(s,.4)
    backward(s,.4)
    turnBy(90)
    x=x+1
#chorus

#bridge