Neopixel Challenges
==============

Overview
--------

The following are a set of challenges using the neopixel stick.

Exercise:
~~~~~~~~~

1. Using a for loop, write a program to turn on each LED on the neopixel in order and then turn them all off. An example is shown in the gif below.
   Note that you can use the following command to turn off all the LEDs.
   
.. code-block:: C
   
   pixels.clear();

.. image:: images/ledup.gif


 TEACHER CHECK \_\_\_\_

2. Modify your code so that one LED lights as it moves up the Neopixel Stick. An example is shown below.
   
.. image:: images/updown2.gif

 TEACHER CHECK \_\_\_\_

3. Modify your code so that the one LED moves up AND down on the neopixel stick. Also increase the speed as shown in the example below.

.. image:: images/fastUD.gif

4. Rewrite your code so that a single LED changes from full red (255) to yellow (red + green). You will need to use a for loop to increase the
   value of green until it is the same as the value of the red.
   
.. image:: images/oneshift.gif

4. Modify your code so that all eight LEDs changes from full red (255) to yellow. To do this correctly, you will need place a for loop inside of
   your existing loop so that all LEDs are set instead of just one.
   
.. image:: images/eightshift.gif


 TEACHER CHECK \_\_\_
