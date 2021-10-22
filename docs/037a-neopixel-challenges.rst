Neopixel Challenges
==============

Overview
--------

The neopixel st

2. Add three potentiometers to your board and modify your code so that
   each potentiometer controls one of the three colors (red, green,
   blue).

 TEACHER CHECK \_\_\_\_

3. Modify your code so that a potentiometer can be used to control the
   number of LEDs that are lit on the neopixel strip. The more you turn
   the dial, the more LEDs are lit. Note that your analog input ranges
   from 0 to 1023 but you only have 8 leds (numbered 0 to 7) so you will
   need to convert the range. The `mapping
   function <https://www.google.com/url?q=https://docs.google.com/document/d/1BmZbXzxnD2j17QToSZ9jeZmnP7burwfksfQq2v4zu-Y/edit%23heading%3Dh.w4r79820c3cs&sa=D&ust=1587613173999000>`__ can
   be helpful here. Also note that initially, you may not have a way to
   turn the LEDs off.

 TEACHER CHECK \_\_\_

4. Modify your code so that when the potentiometer is set all the way to
   the left no neopixels should be lit, and when it is set all the way
   to the right, all the neopixels should be lit. You will need to a one
   line that turns off the previous LED.

 TEACHER CHECK \_\_\_\_
