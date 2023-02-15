Motor Direction Control Functions
=================================

Overview
--------

Writing good functions for motor control are critical to writing good sumo robotics code. The best motor control function can control both motor direction and speed. In this lesson, you will start with just controlling the direction of your motor. In your sumo code, you may find that controlling the direction of the motor is enough. If you need to review how to write a function click `here. <https://mvths-wiki.readthedocs.io/en/latest/031-functions.html?highlight=functions#functions>`_

As you learned in a previous lesson, you can drive one of your motors with the following sort of code. We can imagine that this code drives one of your motors clockwise.

.. code::

    digitalWrite(MOT1A, HIGH);
    digitalWrite(MOT1B, LOW);
    
There are two problems with this approach. One is that it hard to read. Two is that you might want run your motor clockwise multiple times in your code and so you would have to continue to write these two lines of code.

Imagine how much clearer your code would be if you could instead drive a motor with the following single line.

.. code::

   drive_motor(clockwise);
   
This is the power of funcitons. 

Exercise:
~~~~~~~~~

#. Write a function to control just the direction of one motor. The function can be called anything you like, but you should use a name that best indicates the purpose of the function. Your function should allow you to pass one argument to change the direction of the motor. Again, if you need a reminder about how to write functions, check the link above. NOTE: Make sure to use defines for your control pins.

   TEACHER CHECK ______

#. Write a second function to control a second motor. Make sure to use function names to accurately distinguish between the two motors. 

   TEACHER CHECK ______

#. Write a function to control both motors at the same time. Again, make sure to use function names and argument names that are appropriate to the purpose of the function.

   TEACHER CHECK ______
