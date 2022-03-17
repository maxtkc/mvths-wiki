Seven Segment Display
===============

Overview
--------

The four-digit seven segment display provides an easy and quick way to display numbers. It is also highly visible from a distance. Each segment can display the digits 0-9 as well as the characters A-F. It can also be used as clock display since it contains a colon between the two pairs of digits.

.. figure:: images/sevenseg.jpg
   :width: 400px

Exercise:
~~~~~~~~~

Remove power and wire up the four digit display to your Microcontroller board. Note that there are only four required connections. Two of the pins are for 
power and ground. The other two pins allow the display to communicate with your microcontroller.
**IMPORTANT: This display is easily damaged. Make sure to get these first two connections correct or the board will be 
damaged.**

#. The + is connected to the power bus of your breadboard
#. The - is connected to the ground bus of your breadboard.
#. The D (data) should be connected to A4 (SDA) of your microcontroller.
#. The C (clock) should be connected to A5 (SCL) of your microcontroller.

 TEACHER CHECK \_\_\_\_


1. Open and download the example code Examples/Adafruit LED Backpack
   Library/sevenseg. If you cannot find this file, you can install the
   library Adafruit LED Backpack using the manage libraries function.

TEACHER CHECK \_\_\_\_

2. Make a copy of the code. Modify the copy so that it only displays
   a single number. You can do this by commenting out one line of code at a time and testing. 
   
3. Now modify your new code file so that your displays counts from 0 to 120
   and repeats with a 10ms delay. You can do this using a for loop.
   


 TEACHER CHECK \_\_\_\_
