Relational Operators
====================

Overview
--------

In this lesson you will learn to use the greater than and less than logical operators. The greater than operator ">" checks if the value of a variable is greater than a compared value and the less than operator "<" checks if the value of a variable is less than a compared value.::

   x > 23 //If x is greater than 23 this returns true

   x < 23 //If x is less than 23 this returns true
   
The following is an example of a logical operator used inside a conditional.
   
.. code:: C
   
   if (x > 200) {
        // run this code if the above condition is true
   else {
        //run this code if the above condition is false
   }

Exercise:
~~~~~~~~~

#. Set up your board with an LED as an output and a potentiometer as an input.

#. Write a program to read the value of the potentiometer on your serial monitor.

#. Modify your program to turn on your LED if the value from the potentiometer is greater than 400.
   
#. Modify your code to turn off the LED if value of the potentiometer is less than 400. The LED should still turn on if the value is greater than 400.

   TEACHER CHECK \_\_\_\_\_

#. Add two more LEDs to your board. Write a program that turns on the first LED when the value of the potentiometer is greater than 400, the second LED when the value of the potentiometer is greater than 600 and the third LED when the value of the potentiometer is greater than 800. Note that the order in which you check the value of the potentiometer in your code is important.
   
#. Modify your code so that the respective LEDs turn off when they are below the values given above. (i.e. the third LED turns on when the pot is greater than 800 and off when it is less than 800).

   TEACHER CHECK \_\_\_\_\_
