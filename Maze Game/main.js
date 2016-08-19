//Movement and Speed
var x, y, squareSize, xSpeed, ySpeed;
//win and lose booleans
var lost = false, won = false;
//level count and increment system
var level = 1;
//the winning color integer value
var winColor = 1;
//the lsing color integer value
var loseColor = 0;
//Win or lose the game entirely
var game = false;

//setup function: creates levels and character
function setup() {
    createCanvas(600, 600);
    noStroke();
    x = 20;
    y = 35;
    squareSize = 50;
    xSpeed  = 2.5;
    ySpeed = 2.5;
}

// reset to the first level and reset player position
function reset() {
    x = 20;
    y = 35;
    level = 1;
    lost = false;
    won =false;
    game = false;
    loseColor =0;
    winColor=1;
}

//the player itself
function drawPlayer(){
    fill(255, 0, 0);
    rect(x, y, squareSize, squareSize);
}

//All level paths
function drawPath(){
    if (level==1)
    {
       fill(255);
        rect(10,10, 400,100);
        rect(390,10,100,400);
        rect(10,400,480,100);
        fill(1, 155, 155);
        rect(20, 425, 50, 50); 
    }
    else if (level==2)
    {
        fill(255);
        rect(10,400,300,100);
        rect(235,325,75,75);
        rect(100,250,210,75);
        rect(25,35,75,290);
        rect(25,35,400,80);
        rect(425,35,60,550);
        fill(1,155,155);
        rect(425,530,60,55);
    }    
    else if (level ==3)
    {
        fill(3,255,0);
        rect(420,430,80,130);
        fill(255);
        rect(420,80,55,350);
        rect(50,80,450,60);
        rect(50,140,75,250);
        rect(125,325,230,100);
        rect(125,425,60,60);
        fill(1,155,155);
        rect(125,485,100,100);
    }
}

//Collision detection. In short: everytime a key is pressed we get the pixel value
//of all the corners of the square character. If the pixel value is black(a.k.a the borders,)
//the players loses. If the pixel value is 1 (first parameter of the color of the blue square
// the players advances into the next level.
function checkCollision(key) {
    //if user presses a directional key.
    if (key == LEFT_ARROW){
        //get the value of the corners and check if it is black(0)
        if (get(x - xSpeed, y)[0] == loseColor || get(x - xSpeed, y + squareSize)[0] == loseColor)
        {
            //player loses
            lost=true;
        //get the value of the corners and checks if it is blue (1)
        }else if(get(x - xSpeed, y)[0] == winColor || get(x - xSpeed, y + squareSize)[0] == winColor){
            //player wins
            won = true;
        }
    }else if(key == RIGHT_ARROW){
        if (get(x + xSpeed + squareSize, y)[0] == loseColor || get(x + xSpeed + squareSize, y + squareSize)[0] == loseColor)
        {
            lost=true;
        }else if (get(x + xSpeed + squareSize, y)[0] == winColor || get(x + xSpeed + squareSize, y + squareSize)[0] == winColor)
        {
            won = true;
        }
    }else if(key == UP_ARROW){
        if (get(x, y - ySpeed)[0] == loseColor || get(x + squareSize, y - ySpeed)[0] == loseColor)
        {
            lost=true;
        }else if (get(x, y - ySpeed)[0] == winColor || get(x + squareSize, y - ySpeed)[0] == winColor)
        {
            won = true;
        }
    }else if(key == DOWN_ARROW){
        if (get(x, y + squareSize + ySpeed)[0] == loseColor || get(x + sq, y + squareSize + ySpeed)[0] == loseColor)
        {
            lost=true;
        }else if (get(x, y + squareSize + ySpeed)[0] == winColor || get(x + sq, y + squareSize + ySpeed)[0] == winColor)
        {
            won = true;
        }
    }
}
//draws the background and the player. Movement is created here. Does collision detection
//everytime a key is pressed.
function draw() {
    background(0);
    drawPath();
    drawPlayer();

    if(!lost){
        if (keyIsDown(LEFT_ARROW)){
            checkCollision(LEFT_ARROW);
            x -= xSpeed;

        }
        if (keyIsDown(RIGHT_ARROW)){
            checkCollision(RIGHT_ARROW);
            x += xSpeed;
        }
        if (keyIsDown(UP_ARROW)){
            checkCollision(UP_ARROW);
            y -= ySpeed;
        }
        if (keyIsDown(DOWN_ARROW)){
            checkCollision(DOWN_ARROW);
            y += ySpeed;
        }
    }

    //tells the user what happened
    if (lost){
        reset();
    }else if (won == true){
        level++;
        if(level == 3){
            loseColor = 255;
        }else{
            loseColor = 0;
        }
        won = false;
        if (level == 4){
            game = true;
        }
    }

    if(game){
        fill(100, 55, 222);
        textSize(30);
        var t = "You won the game! Good job!";
        text(t, width/2 - textWidth(t)/2, height/2);
    }
}