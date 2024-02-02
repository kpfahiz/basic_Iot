//Including Libraries
#include <Stepper.h>
#include "SR04.h"
//Setting pins
#define TRIG_PIN 4
#define ECHO_PIN 3
//Creates an instance of our ultrasonic sensor
SR04 sr04 = SR04(ECHO_PIN,TRIG_PIN);
//A variable to store the sensor's value
long a;

// Defines the number of steps per rotation
const int stepsPerRevolution = 2038;

// Creates an instance of stepper class
// Pins entered in sequence IN1-IN3-IN2-IN4 for proper step sequence
Stepper myStepper = Stepper(stepsPerRevolution, 8, 10, 9, 11);

void setup() {
    // Nothing to do (Stepper Library sets pins as outputs)
    Serial.begin(9600);
    myStepper.setSpeed(15);
}

void loop() {
  //Store the distance returned by the sensor
  a=sr04.Distance();
  //If the distance is less than 40
  if(a <= 40) 
  { 
    //Turn for 3 whole revolutions
    myStepper.step(-stepsPerRevolution * 3);
    //Print a message
    Serial.println("Opened");
    //Wait some time
    delay(6000);
    //Turn in the opposite direction.
    myStepper.step(stepsPerRevolution * 3); 
    Serial.println("Closed");
  }
 

}