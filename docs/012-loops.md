# Overview

Up until this point all of your code has been placed in your setup function. As you have probably noted, this function only runs once. The loop function is designed to run continuously. Any code place in this function will run continuously until power is removed from the Metro Mini.

# Code

1.  Using a delay and your loop function, write a program to make your LED blink (on for one second and off for one second) continuously.

TEACHER CHECK \_\_\_\_\_

2.  Set up two LEDs on your breadboard on different pins. Make the LEDs flash alternately (i.e. one is on while the other is off)

TEACHER CHECK \_\_\_\_\_

# 

INPUT PINS

# Overview

The digital pins on the Metro Mini can also be set as inputs. As an input, the Metro Mini can read the value of a pin, i.e. if the pin is externally driven as HIGH (5V) or LOW (0V). Generally inputs are used for receiving information from the outside world, such a reading the value of a sensor or getting data from a robotic device.

Setting up software and hardware to test an input is a little more complicated than setting up software and hardware to test an output.

# Schematic

Set up the following circuit on your breadboard. Make sure to use a long jump wire for the connection between pin 9 and ground. You will be moving this pin between power and ground so using a long jump wire will make this much easier. By moving the long jump wire between GND and power you will be setting the input of pin 9 as HIGH and LOW. This wire will essentially act as a crude switch.

![](images/image101.png)

# Code

1.  In your  setup function, insert the following two lines to ensure that that pin 6 is an OUTPUT and pin 9 is an INPUT.

pinMode(9, INPUT);        

pinMode(6, OUTPUT):

2.  Type the following code inside of the loop function. This code is set in the loop function because it needs to repeatedly check the value of pin 9. For more information about how this code works you can review [conditionals](https://www.google.com/url?q=https://docs.google.com/document/d/1BmZbXzxnD2j17QToSZ9jeZmnP7burwfksfQq2v4zu-Y/edit%23heading%3Dh.o11qq65yx4ek&sa=D&ust=1587613173872000) in concepts.

![](images/image52.png)

3.  Compile and download your code.
4.  Connect pin 9 to the power bus (HIGH). The LED should be lit.
5.  Connect pin 9 to the ground bus (LOW). The LED should be off.

TEACHER CHECK \_\_\_\_\_

6.  What happens when the pin is in neither ground or power? Move the pin around or touch it with your hand. A pin when not connected to power or ground is said to [float](https://www.google.com/url?q=https://docs.google.com/document/d/1BmZbXzxnD2j17QToSZ9jeZmnP7burwfksfQq2v4zu-Y/edit%23heading%3Dh.jcbntq8yv6k7&sa=D&ust=1587613173873000).
7.  Modify your code so that it reverses operation. The LED should be lit when pin 9 is connected to LOW and vise versa.

TEACHER CHECK \_\_\_\_\_
