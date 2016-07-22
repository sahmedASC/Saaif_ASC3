SpaceX = 580
bullet = False
bulletY = 625
bulletX = SpaceX + 25
xChange = 1
invaders = []

for i in range(5):
    invaders.append(["0"] * 11)

for m in range(len(invaders)):
    print(invaders[m])
    
def setup():
    size(1280, 720)
    frameRate(120)
    background(0, 0, 0)

def initial_invaders():
    global bulletX
    global bulletY    
    global bullet
    global SpaceX
    global xChange
    x = 250 
    x += xChange
    if 30 >= x >= 500:
        xChange*=-1
        
     
          
    for j in range(11):
        y = 30
        for k in range(5):
            if invaders[k][j] == "0":
                fill(0, 255, 0)
                rect(x, y, 50, 50)
                if bullet == True and y < bulletY < y + 50 and x < bulletX < x + 50:
                    invaders[k][j] = "X"
                    bullet = False
                    bulletY = 625
                    bulletX = SpaceX + 25 
            
            y += 60
        x += 70
        
    '''while 30 < x < 1200:
        x += xChange
        print("ih")
        if 30 > x > 1200:
            xChange *= -1
            y -= 10'''
    
def keyPressed():
    global SpaceX
    global bullet
    if key == "a":
        SpaceX = SpaceX - 10
        if SpaceX <= 30:
            SpaceX = 30
            
    if key == "d":
        SpaceX = SpaceX + 10
        if SpaceX >= 1190:
            SpaceX = 1190
            
    if keyCode == 32:
        bullet = True
     
def spaceShip():
    #Spaceship Body
    fill(255, 255, 255)
    rect(SpaceX, 660, 60, 15, 40, 40, 0, 0)
    
    #Spaceship Cockpit
    fill(0, 255, 255)
    rect(SpaceX + 23.25, 640, 15, 20, 20, 20, 0, 0)
    
    #Spaceship Engines
    fill(255, 0, 0)
    rect(SpaceX + 10, 670, 8, 15)
    rect(SpaceX + 40, 670, 8, 15)
        
    
def draw():
    global SpaceX
    global bulletY
    global bulletX
    global bullet

    
    background(0, 0, 0)
    initial_invaders()
    spaceShip()
     
    
    if bullet == True:
        fill(255, 255, 255)
        rect(bulletX, bulletY, 10, 15)
        bulletY -= 15
        bulletX = SpaceX + 25
        if bulletY < 30:
            bullet = False
            bulletY = 625
            bulletX = SpaceX + 25