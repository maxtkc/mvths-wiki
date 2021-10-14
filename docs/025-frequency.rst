Frequency
====================

Overview
--------

In the previous lesson you made an LED blink by turning it on and off repeatedly. The faster you turned the LED on and off the faster it blinked which
in turn means a higher frequency. The slower you turned the LED off and on, the slower the frequency. Frequency is a measurement of the number of 
blinks over a period of time. Again, more blinks represents a higher frequency.

The unit of measurement for frequency is Hertz which is defined as cycles "blinks" per second. A fast CPU might have a frequency of 3Ghz. That is the processor can
run calculations at 3 billion cycles per second. By contrast the microcontroller that you are using runs at only 16Mhz, or 16 million cycles per second. 

Exercise
~~~~~~~~

In the following exercise you will create different frequencies with your microcontroller and measure them.

#. Write a program that blinks and LED on for 10 milliseconds and off for 10 milliseconds. Using a multimeter measure the frequency. Note 
that on the meter there is position labeled with Hz for frequency. Again, connect the black lead to ground and the red lead to the 
pin you are measuring. Write the value you see on your meter in your notebook. Remember to use the correct units
  
#. Modify your code so that frequency you read on your meter is about 166Hz. Record the delay values you used in your notebook. 

#. In order to get higher frequencies you can use a shorter delay function shown below. 

.. code-block:: c

    delayMicroseconds(400);
    
Use this delay to get a frequency of about 2000Hz or 2KHz. Record the delay values you used in your notebook. 
