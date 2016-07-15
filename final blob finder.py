#Setup
from Myro import *
from Graphics import *
from random import *
import re
import sys

global user=""

def setup_graphics():
    user = input("What color do you want? Red, Yellow, Green, Blue")
    
    #Even More Setup
    width = 500
    height = 500
    sim = Simulation("Maze World", width, height, Color("gray"))

    #outside walls
    sim.addWall((10, 10), (490, 20), Color("black"))
    sim.addWall((10, 10), (20, 490), Color("black"))
    sim.addWall((480, 10), (490, 490), Color("black"))
    sim.addWall((10, 480), (490, 490), Color("black"))

    #blue spot
    poly = Circle((50, 50), 45)
    poly.bodyType = "static"
    poly.color = Color("blue")
    poly.outline = Color("black")
    sim.addShape(poly)

    #red spot
    poly = Circle((450, 50), 45)
    poly.bodyType = "static"
    poly.color = Color("red")
    poly.outline = Color("black")
    sim.addShape(poly)

    #green spot
    poly = Circle((50, 450), 45)
    poly.bodyType = "static"
    poly.color = Color("green")
    poly.outline = Color("black")
    sim.addShape(poly)

    #yellow spot
    poly = Circle((450, 450), 45)
    poly.bodyType = "static"
    poly.color = Color("yellow")
    poly.outline = Color("black")
    sim.addShape(poly)

    #begin simulation and sets robot's position
    makeRobot("SimScribbler", sim)
    sim.setPose(0, width/2, height/2, 0)

    sim.setup()

# 1-RED
# 2-GREEN
# 3-BLUE
# 4-YELLOW

#The following is a helper function 
#Inputs: A picture and a color represented by the list above
#Returns the average x location of the color in the picture or -1 if the robot has found the color spot

def findColorSpot(picture, color):
    xPixelSum = 0
    totalPixelNum = 0
    averageXPixel = 0

    show(picture)

    for pixel in getPixels(picture):
        if(color == 1 and getRed(pixel) > 200 and getGreen(pixel) == 0 and getBlue(pixel) == 0):
            xPixelSum += getX(pixel)
            totalPixelNum += 1
        elif(color == 2 and getRed(pixel)== 0 and getGreen(pixel) > 90 and getBlue(pixel) == 0):
            xPixelSum += getX(pixel)
            totalPixelNum += 1
        elif(color == 3 and getRed(pixel) == 0 and getGreen(pixel) == 0 and getBlue(pixel) > 200):
          
            xPixelSum += getX(pixel)
            totalPixelNum += 1
        elif(color == 4 and getRed(pixel) > 180 and getGreen(pixel) > 180 and getBlue(pixel) == 0):
            
            xPixelSum += getX(pixel)
            totalPixelNum += 1
    if(totalPixelNum != 0):
        averageXPixel = xPixelSum/totalPixelNum

    #Handles the case where robot has found the spot if it is near it
    #If necessary adjust the value
    if(totalPixelNum/(getWidth(picture)*getHeight(picture)) > 0.21):
        averageXPixel = -1

    return averageXPixel


# Use the following integers for colors:
# 1-RED
# 2-GREEN
# 3-BLUE
# 4-YELLOW

######################Code Starts Here##################################
#Function defining
def find_the_blob_red():
    pic = takePicture()
    color = findColorSpot(pic, 1)

    takePicture()
    print(pic)
    while findColorSpot(pic, 1)<100:
        turnBy(10)
        pic=takePicture()
        print(color)
        takePicture()

    while findColorSpot(pic, 1)<200:
        forward(1,1)

def find_the_blob_blue():
    pic = takePicture()
    color = findColorSpot(pic, 3)

    takePicture()
    print(pic)
    while findColorSpot(pic, 3)<100:
        turnBy(10)
        pic=takePicture()
        print(color)
        takePicture()

    while findColorSpot(pic, 3)<200:
        forward(1,1)
   
def find_the_blob_green():
    pic = takePicture()
    color = findColorSpot(pic, 2)

    takePicture()
    print(pic)
    while findColorSpot(pic, 2)<100:
        turnBy(10)
        pic=takePicture()
        print(color)
        takePicture()

    while findColorSpot(pic, 2)<200:
        forward(1,1)
def find_the_blob_yellow():
    pic = takePicture()
    color = findColorSpot(pic, 4)

    takePicture()
    print(pic)
    while findColorSpot(pic, 4)<100:
        turnBy(10)
        pic=takePicture()
        print(color)
        takePicture()

    while findColorSpot(pic, 4)<200:
        forward(1,1)


#What runs depending on user input
#Asks the user a question
def main():
    
    setup_graphics()
    if user == "Red":
        find_the_blob_red()
    elif user == "Yellow":
        find_the_blob_yellow()
    elif user == "Green":
        find_the_blob_green()
    elif user == "Blue":
        find_the_blob_blue()
    else:
        print("wrong Input")
        sys.exit()
        
   
#^^^^^Forces the user to input a "color".
main()



    
    
    

      
    

