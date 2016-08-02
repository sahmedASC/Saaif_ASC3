var floor;
var player;

function preload()
{
    floor = createSprite(0, 550, 2048, 30);
    floor.shapeColor = color(139,69,19);

    //var obstacle1 = 
    player = createSprite(20, 410, 20, 40);
    player.shapeColor = color(0, 255, 255); 
}

function setup()
{
    createCanvas(1024, 600);
}


function keyPressed()
{
    

    if (key === 'd')
    {
         player.velocity.x += 2;
    }

    if (key === 'a')
    {
        player.velocity.x -= 2;
    }

    if (keyCode === '32')
    {
        player.velocity.y -= 4;
    }
}

function draw()
{
    background(120, 0, 120);
    
    player.velocity.y += 2;
    
    if (player.collide(floor))
        {
            player.velocity.y = 0;
        }
    /*else
    {
        player.velocity.x = 0;
    }*/

    //gravity();
    drawSprites();
}