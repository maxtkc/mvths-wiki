Logical Operators
=================

Overview
--------

In this lesson, you will learn to use the logical operators **AND**, **OR** and **NOT**. 

.. list-table:: Logical Operators
   :widths: 25 25 50 50
   :header-rows: 1

   * - Operator
     - Name
     - Is true if...
     - Example
   * - &&
     - AND
     - both operands is true
     - if ((x==5) && (y< 7))
   * - ||
     - OR
     - either operand are true
     - if ((z < 2) || (a > 5))
   * - !
     - NOT
     - the operand is false
     - if (!(x < 5))
  
Exercise:
~~~~~~~~~

#. With a potentiometer and at least one LED on your board, write a program to turn on the LED when the value of the potentiometer is above 600 or below 400. This will require the use of the OR operator inside of your conditional statement.  Note: The LED (or LEDs) should be off between the values of 400 and 600. 

   
#. Modify your program so that LED is on when the value of potentiometer reads between 500 and 700. The LED should be off when the potentiomenter reads below 500 and above 700. 

#. Modify your program so that the LED is only on between the values of 123 and 200, and the values of 456 and 601. 

#. Add a button on your board. Write a program that turns on the LED when the value of the potentiometer is between 200 and 400 and the button is pressed.

   TEACHER CHECK \_\_\_\_\_

