Neopixel Challenge One
==============

Overview
--------

The following are a set of challenges using the neopixel stick.

Exercise:
~~~~~~~~~

#. Using a for loop, write a program to turn on one neopixel at a time from bottom to top and then turn them all off. An example is shown in the gif below. Note that you can use the following command to turn off all the LEDs.
   
   .. code-block:: C
   
      pixels.clear();

   .. image:: images/ledup.gif


   TEACHER CHECK \_\_\_\_

#. Modify your code so that one neopixel appears to move up the Neopixel Stick. An example is shown below.
   
   .. image:: images/updown2.gif

   TEACHER CHECK \_\_\_\_

#. Modify your code so that the one neopixel appears to moves up AND down on the neopixel stick. Also increase the speed as shown in the example below.

   .. image:: images/fastUD.gif

#. Rewrite your code so that a single LED changes from full red (255) to yellow (full red + full green). You will need to use a *for loop* to increase the value of green until it is the same as the value of the red.
   
   .. image:: images/oneshift.gif

#. Modify your code so that all eight neopixels change from full red (255) to yellow. To do this correctly, you will need place a for loop inside of your existing loop so that all neopixels are set instead of just one.
   
   .. image:: images/eightshift.gif


 TEACHER CHECK \_\_\_
