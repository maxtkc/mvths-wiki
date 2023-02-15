Motor Direction Control Functions
=================================

Overview
--------

Writing good functions for motor control are critical to writing good sumo robotics code. The best motor control function can control both motor direction and speed. In this lesson, you will start with just controlling the direction of your motor. In your sumo code, you may find that controlling the direction of the motor is enough. If you need to review how to write a function click `here. <https://mvths-wiki.readthedocs.io/en/latest/031-functions.html?highlight=functions#functions>`_

As you learned in a previous lesson, you can drive one of your motors with the following sort of codel. 

.. code::

    digitalWrite(MOT1A, HIGH);
    digitalWrite(MOT1B, LOW);
    
    

Exercise:
~~~~~~~~~

Write a function to control just the direction of one motor. The function can be called anything you like, but you should use a name that best indicates the purpose of the function. The following is just one example.

.. code::

   void motor(int direction) {

      //write your motor drive commands here
      //Make sure to use the defines you used for your control pins

   }

Write your motor code (within the motor function)  so that passing an argument of 1 will drive the motor forward and passing an argument of 2 will drive the motor in reverse. This way the following example commands can be used to call the function.

motor(1);  //to drive the motor forward

motor(2); //to drive the motors reverse

Using these examples as a starting point, write a complete program
including a function to drive your motor. You program should drive the
motor forward for 3 seconds and reverse for 3 seconds repeatedly.

TEACHER CHECK \_\_\_\_

Exercise:
~~~~~~~~~

Modify your function so that instead of using the numbers 1 and 2 for
forward and reverse, use the text forward and reverse. In order to do
this, you will simply need to create defines for forward and reverse at
the top of your code file.

TEACHER CHECK \_\_\_\_
