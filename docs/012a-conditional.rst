Conditionals
=============

Overview

--------

Conditionals offer a way for your code to make decisions. In the real world, an example of a conditional might be, if it is cold put on a sweater. A conditional in code looks like the following (see below). In the following code, the condition x == 5 is evaluated as either true or false. Note the double equals sign. The code x = 5 tells the program to set x to the value 5. The code x == 5 tells the program to compare the value of x and 5. If they are the same, the program returns true. If they are not the same, the program returns false.

.. code-block:: c
   
   if (x == 5) {                //Checks if this condition is true (i.e. does x equal 5). Note double equals sign
      Serial.println("true");  //If the condition is true than this line is executed.
   }
   
In addition to the single state  *if*, you can also have a second state represented by *else*. The following is an example of code that has two possible states based on the evaluation of the initial condition.

.. code-block:: c
   
   if (x == 5) {                //Checks if this condition is true (i.e. does x equal 5). Note double equals sign
      Serial.println("true");  //If the condition is true than this line is executed.
   } else {
     Serial.println("true");
   }
     
Challenge
----------

#. Write a program to test the value of a variable. Initialize a variable and set its initial value to 6. Using a conditional, check if the value is in fact 6. If the value is 6  then print "true" in your serial monitor.

#. Connect pin 6 to ground via a long jump wire. Modify your program to print "true" only if pin 6 is connected to power.

#. 

TEACHER CHECK \_\_\_\_\_

