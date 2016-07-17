from Myro import *
from Graphics import *


obamaDarkBlue = makeColor(0,51,76)
obamaRed = makeColor(217, 26, 33)
obamaBlue = makeColor(112,150,158)
obamaYellow = makeColor(252, 227, 166)
pic = makePicture(pickAFile())
#obama(pic)


for pixel in getPixels(pic):
    gray = getBlue(pixel)
    red = getRed(pixel)
    black = getGreen(pixel)
   # gray = makeColor(255,0,0)
    if black < 60:
        setColor(pixel, obamaRed)
    
    elif gray < 120:
        setColor(pixel, obamaBlue)
    
    elif red <180:
        setColor(pixel, obamaYellow)
    else:
        setColor(pixel, obamaDarkBlue)
        
show(pic)
