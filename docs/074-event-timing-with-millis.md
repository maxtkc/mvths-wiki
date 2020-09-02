# Event Timing With Millis

## Overview

A common task for a microcontroller is to run an event at a regular and precise interval. A simple example is flashing an LED. In some cases the event timing interval is very short as in moving a character in a game or controlling the frequency of a stepper motor. In some cases the interval is very long as in feeding fish every eight hours.

One approach for establishing an interval is using a delay in your code. The main problem with delays though is that they are blocking in that they prevent any other code from running while in the delay. In some cases this is not a problem, as in a short delay after a button is pressed, but for regular events it is generally best to avoid this approach.

A better approach for timing regular events is to use the internal timers of the microcontroller. In this lesson, you will learn to use the built-in function millis() for this purpose. In the next lesson you will learn to use timer interrupts.

The millis function returns the number of milliseconds passed since your Arduino began running its current program i.e. when power was applied to the controller or the program was reset or uploaded. The value of millis is stored as an unsigned long which is four bytes or a top value of 4,294,967,296. Yes, that is over 4 billion milliseconds or almost 50 days. When the count reaches this top value it returns to zero and continues counting.

# Read Millis

You can read the value of millis() by simply calling the function. Remember that millis returns an unsigned long so it is generally useful to store the result of the call in an unsigned long. For short timing intervals though this is not absolutely necessary.

#### unsigned long x = millis();

## Challenge

Use the delay function to display the value of millis roughly every 500 milliseconds in your terminal window. Generally, you would not use a delay and millis together this way, but this challenge is just for demonstrations purposes. In your loop function, you should include both a 500 ms delay and Serial.print function to display the value of millis. Since delay stops the loop function every 500 ms, the value of millis displayed in your terminal window should increase by 500 each time it is printed.

# Time Interval

Below is sample code for using millis to create a timed interval in the loop function. The function is designed to print “count” exactly every 1000 ms. It does this without using a delay and without blocking the code (sitting in a state where no other code can be executed).

The first step is to grab the value of millis each time through the function loop. This value is stored in the variable thisTime which is initialized as a long. Since not much happens in this loop, thisTime gets updated very frequently. In fact the remainder of the code requires so little processing time to execute, that it might even get updated many times before 1 ms has passed.

For example, every time the conditional is false (not executed) the loop completes and returns back to the line including millis. If it were possible to print the value of millis fast enough, you would likely see the same value printed many times (number of times through the loop) before printing the next value, i.e. before a single millisecond had elapsed.

####   timeThis = millis();

Next the program checks if the present time (timeThis) minus the previous time (timeLast) is greater than 1000. This is key to how the program works and a bit confusing.

#### if (timeThis - timeLast \>= 1000)

Note that timeThis is being updated almost constantly or every time the loop completes which as noted above is very frequently. timeLast on the other hand is only updated when the conditional is true, when 1000ms has passed.

A good way to understand difficult code is to walk through it with some example numbers. Starting at the beginning, both thisTime and lastTime are initialized to zero. As the program begins the first value of thisTime is probably something greater than zero since some code is executed before the loop even begins running. Let’s say the first value of thisTime is 13. At this point the value of lastTime is still zero. thisTime minusLast time (13 - 0) is zero so the conditional if false and not executed. Each time through the loop millis is called and over time, the value of thisTime increases until it reaches 1000 (1000 - 0) is greater than or equal to 1000 so the conditional is true. The print statement is executed and the lastTime now has the value of 1000.

The next time through the loop thisTime is set at 1000 or 1001. Either way thisTime minus lastTime is far less than 1000 so the loop continues to execute until thisTime equals 2000 and so on.

To be precise, you should note that the first time the conditional is true, the exact interval might be slightly less than 1000 since, as noted above, 13 ms elapsed before the loop even started, but from this point on, we should get an exact 1000 ms interval.

#### Unsigned long timeThis, timeLast;

#### 

#### void setup() {

####   Serial.begin(9600);

#### }

#### 

#### void loop() {

####   //Store the present count of millis

####   timeThis = millis();

####   //Check if 1000ms has passed between the last check of millis

####   if (timeThis - timeLast \>= 1000) {

####     Serial.println("count\!");

#### //Update the variable timeLast so it now contains the present value of       //millis

####     timeLast = timeThis;

####   }

## Challenge

Write a program to flash an LED on and off with a total period of 700ms (350ms on and 350ms off) without using a delay.
