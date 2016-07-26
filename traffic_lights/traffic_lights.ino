//#include <string>
int val = 0;
void setup() {
  pinMode(12, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(2, OUTPUT);
  pinMode(6, INPUT);
}
int lights()
{ 
  digitalWrite(12, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(3000);              // wait for a second
  digitalWrite(12, LOW);    // turn the LED off by making the voltage LOW
  delay(10);              // wait for a second 
  digitalWrite(10, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(1000);              // wait for a second
  digitalWrite(10, LOW);    // turn the LED off by making the voltage LOW
  delay(10);              // wait for a second*/
  digitalWrite(8, HIGH);    // turn the LED off by making the voltage LOW
  delay(3000);              // wait for a second*/
  digitalWrite(8, LOW);    // turn the LED off by making the voltage LOW
  delay(10);
  digitalWrite(12, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(3000);              // wait for a second
  digitalWrite(12, LOW);    // turn the LED off by making the voltage LOW
  
  return 0;
}

int pedestrian()
{
  digitalWrite(2,HIGH);
  digitalWrite(12, LOW);
  digitalWrite(4, LOW);
  digitalWrite(8, HIGH);
  delay(3000);
  digitalWrite(2, LOW);
  delay(800);
  digitalWrite(2, HIGH);
  delay(800);
  digitalWrite(2, LOW);
  delay(800);
  digitalWrite(2, HIGH);
  delay(800);
  digitalWrite(2, LOW);
  delay(800);
  digitalWrite(2, HIGH);
  digitalWrite(8, LOW);
}
int no_pedestrian()
{
  digitalWrite(4,HIGH);
  digitalWrite(12,HIGH);
  digitalWrite(2,LOW);
  return 0;
}

void loop() 
{
  val = digitalRead(6); 
  digitalWrite(2,val);
  if (val == LOW)
  {
    no_pedestrian();
    
  }
  if (val == HIGH)
  {
    pedestrian();
    //lights();
  }  
}
