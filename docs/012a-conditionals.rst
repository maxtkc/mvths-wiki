Conditionals
=============

Overview

--------

Conditionals offer a way for your code to make decisions. In the real world, an example of a conditional might be, if it is cold put on a sweater. A conditional in code looks like the following (see below). In this code the condition x == 5 is evaluated. If it true, the code inside the curly braces runds. **NOTE:** the double equals sign is used when comparing two values.

.. code-block:: c
   
   if (x == 5) {                //Checks if this condition is true (i.e. does x equal 5). Note double equals sign
       Serial.print("true");    //If the condition is true than any lines of code placed between the two curly braces are executed.
                  
   }

In addtion to checking if two values are equal, you came make a variety of comparisons using the relational operators shown below.
   
.. list-table:: 
   :widths: 25 25 50
   :header-rows: 1

   * - Relational Operator
     - Description
     - Example
   * - ==
     - is equal to
     - x == 5
   * - >
     - is greater than
     - x > 5
   * - <
     - is less than
     - x < 5
   * - >=
     - is greater than or equal to
     - x >= 5
 
   * - <= 
     - is less than or equal to
     - x <= 5
   * - != 
     - is not equal to
     - x != 5
   
Challenge
----------

#. Write a program that includes a variable slowly increasing in value. Print the value to your serial monitor. When then variable reaches a set value, you should print "true" in your serial monitor. 

#. Modify your program so that the monitor displays "true" when the value is below your set point and "false" when above your set point.

#. Connect pin 6 to ground via a long jump wire. Modify your program to print "true" if pin 6 is connected to power.

TEACHER CHECK ____

