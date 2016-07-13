#Made by Saaif Ahmed and Jason Zhagui
#Song used- Spider Dance (Undertale) by Toby Fox
#We plan to create the loops once we have the movements down for the parts
from Myro import *

#verse
x=0
while x<4:
    i=0
    while i<6:
        turnRight(1,.1)
        turnLeft(1,.2)
        turnRight(1,.2)
        turnLeft(1,.1)
        i=i+1

    forward(1,.5)
    backward(1,.5)
    forward(1,.5)
    backward(1,.5)
    turnBy(60)
    x=x+1
#chorus

#bridge