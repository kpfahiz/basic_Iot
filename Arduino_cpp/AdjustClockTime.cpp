/*
AdjustClockTime sketch
buttons on pins 2 and 3 adjust the time
*/
#include <Time.h>
const int btnForward = 2; // button to move time forward
const int btnBack = 3;    // button to move time back
unsigned long prevtime;   // when the clock was last displayed
void setup()
{
    digitalWrite(btnForward, HIGH); // enable internal pull-up resistors
    digitalWrite(btnBack, HIGH);
    setTime(12, 0, 0, 1, 1, 11); // start with the time set to noon Jan 1 2011
    Serial.begin(9600);
    Serial.println("ready");
}
void loop()
{
    prevtime = now();         // note the time
    while (prevtime == now()) // stay in this loop till the second changes
    {
        // check if the set button pressed while waiting for second to roll over
        if (checkSetTime())
            prevtime = now(); // time changed so reset start time
    }
    digitalClockDisplay();
}