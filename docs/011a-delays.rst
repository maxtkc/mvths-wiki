Delays
================

Overview
--------

Delays are used to stop the progress of the code for a specified amount of time. As you should recall, lines of code inside a function are always executed in order from top to bottom. A delay stops this progress for the time specified in the delay. The delay function we are using is measured in milliseconds and has a range from 0 to 10,000 milliseconds and only in whole numbers. That means that fractional numbers such as 1.67 or numbers larger than 10,000 cannot be used in the function.

Below is an example of the delay command. In this example, the delay is set for 1500 milliseconds (or 1.5 seconds).

.. code-block:: c

   delay(1500);  //Produces a 1.5 second delay

Note that fractional delays do not work. For delays below 1ms you will need to use a different function, delayMicroseconds() which is covered in a later lesson.

.. code-block:: c

   delay(.25);  //THIS DOES NOT WORK
   
Code
----

Write a program to turn your LED on for two seconds and then off for one second and then back on indefinitely. This code should again be placed in your setup function.

IMPORTANT: Do not forget to make sure to set the pin the LED is using to an output.

TEACHER CHECK \_\_\_\_\_
