Analogwrite
===========

Overview
--------

In addition to creating a PWM signal using delays, you can create a PWM signal using the analogWrite command which works in the background. This essentially means that the pulse created by this command runs independently of your code. This allows you to create a PWM signal without using delays in your code.

The function takes two arguments. The first argument is the pin number on your device and the second is a value that corresponds to the duty cycle of the pulse. In the example below the pin being used is 9 and the duty cycle is 200.

.. code-block:: C
   
   analogWrite(9, 200);


The pin is the pin number that will produce the PWM signal. NOTE that this function **ONLY** works on pins 3, 5, 6, 9, 10, and 11. The value determines the duty cycle or width of the pulse. The range of values is 0 to 255. A value of 255 produces a 100% duty cycle (or full on) and a value of 0 produces 0% duty cycle (or is full off). A value of 128 produces a 50% duty cycle or half on and half off.

Exercise
~~~~~~~~

#. Calculate the value required to create a 75% duty cycle using the analogWrite command. Show your calculations in your notebook.

#. Write a program that produces a pulse with a 75% duty cycle. Place the analogWrite command in the set-up function and not in the loop function to demonstrate that you do not need to repeatedly call this command.

#. Using your oscilloscope measure the width of the HIGH and LOW portions of the pulse. Write your answers in your notebook and make sure to use the correct units.

TEACHER CHECK \_\_\_\_

Challenge
~~~~~~~~~

Design a circuit that can be used to control the brightness of an LED with a potentiometer.

TEACHER CHECK \_\_\_\_

 
