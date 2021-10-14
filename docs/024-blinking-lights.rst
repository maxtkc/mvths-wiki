Blinking Lights
======

Overview
--------

In your loop function it is possible to write code that will turn your LED on and then off repeatedly causing it to blink. In order for this to work
you must turn your LED on for a period of time and then off for a period of time. The loop function will repeat this action indefinitely. The longer the
time your LED is on and off the slower the blink rate. The shorter time your LED is off and on the faster the blink rate.


The following shows an example of how you can write code to create an infinite set of
pulses on a single digital pin on your microcontroller. The diagram shows how each line of code
corresponds to each part of the pulse.

.. figure:: images/image80.png
   :alt: 

Exercise:
~~~~~~~~~

1. Add an LED to your board if there is not already one on there. Write a
   program to flash the LED using code to create a pulse. Use a delay that is 
   large enough that you can see the LED flash on and off.

TEACHER CHECK \_\_\_\_

2. Reduce the delay in your code until you can no longer see that the LED is flashing. Essentially, it is flashing so quickly (on and off) that
   your eye can no longer perceive the individual pulses of the LED.
   
3. Write the value of this delay value in your notebook. Make sure to use the correct units. This is the rate of your critical flicker-fusion
   frequency (CFFF), the fastest flash you can perceive. This is very different for different animals. Read an article about CFFF `here <https://www.google.com/url?q=https://www.economist.com/news/science-and-technology/21586532-small-creatures-fast-metabolisms-see-world-action-replay-slo-mo&sa=D&ust=1587613173941000>`__.
   It is pretty cool.

TEACHER CHECK \_\_\_\_
