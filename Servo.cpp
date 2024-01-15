#include <Servo.h>
Servo myservo; // create servo object to control a servo
int angle = 0; // variable to store the servo position
void setup()
{
myservo.attach(9); // attaches the servo on pin 10 to the servo object
}
void loop()
{
for(angle = 0; angle < 180; angle += 1) // goes from 0 degrees to 180 degrees
{ // in steps of 1 degree
myservo.write(angle); // tell servo to go to position in variable 'angle'
delay(20); // waits 20ms between servo commands
}
for(angle = 180; angle >= 1; angle -= 1) // goes from 180 degrees to 0 degrees
{
myservo.write(pos); // tell servo to go to position in variable 'pos'
delay(20); // waits 20ms between servo commands
}
}
