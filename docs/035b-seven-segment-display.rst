Seven Segment Display
===============

Overview
--------

The four digit seven segment display provides an easy and quick way to
display numbers. It is also highly visible from a distance. The display
can display numbers in both decimal and
`hexadecimal <https://www.google.com/url?q=https://docs.google.com/document/d/1BmZbXzxnD2j17QToSZ9jeZmnP7burwfksfQq2v4zu-Y/edit%23heading%3Dh.r9xkk2b3evb&sa=D&ust=1587613173990000>`__ since
it can display the characters A-F. It can be used as clock display since
it contains a colon between the two pairs of digits.

Exercise:
~~~~~~~~~

Remove power and wire up the four digit display to your breadboard. Note
that there are only four required connections. The device communicates
with your microcontroller over
`I2C <https://www.google.com/url?q=https://docs.google.com/document/d/1BmZbXzxnD2j17QToSZ9jeZmnP7burwfksfQq2v4zu-Y/edit%23heading%3Dh.zbv2l6wpi6ec&sa=D&ust=1587613173990000>`__.
The pin marked D (data) should be connected to SDA on your
microcontroller. The pin marked C (clock) should be connected to SCL on
your microcontroller. You can locate the I2C pins (SDA, SCL) on your
Metro Mini from this
`diagram <https://www.google.com/url?q=https://docs.google.com/document/d/1BmZbXzxnD2j17QToSZ9jeZmnP7burwfksfQq2v4zu-Y/edit%23heading%3Dh.bk51dfzckrxr&sa=D&ust=1587613173991000>`__.

 TEACHER CHECK \_\_\_\_

Exercise:
~~~~~~~~~

1. Open and download the example code Examples/Adafruit LED Backpack
   Library/sevenseg. If you cannot find this file, you can install the
   library Adafruit LED Backpack. You can find more information about
   managing libraries
   `here <https://www.google.com/url?q=https://docs.google.com/document/d/1BmZbXzxnD2j17QToSZ9jeZmnP7burwfksfQq2v4zu-Y/edit%23heading%3Dh.5ie0wlz76yki&sa=D&ust=1587613173992000>`__.
   If the code does not compile, you may need to install the Arduino GFX
   library as well.

TEACHER CHECK \_\_\_\_

2. Make a copy of the code and modify the copy so that it only displays
   a single number. Make sure you remove all of the code you do not
   need.
3. Modify your new code file so that your displays counts from 0 to 120
   and repeats with a 10ms delay. You will need to use a `for
   loop <https://www.google.com/url?q=https://docs.google.com/document/d/1BmZbXzxnD2j17QToSZ9jeZmnP7burwfksfQq2v4zu-Y/edit%23heading%3Dh.2u7q6orum403&sa=D&ust=1587613173992000>`__ to
   do this.
4. Using the MCP9808 temperature sensor, display the temperature on the
   LED display. In order to do this, you will need to combine minimal
   code for the temperature sensor with minimal code for the LED
   display.

 TEACHER CHECK \_\_\_\_
