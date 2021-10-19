Delays
================

Overview
--------

Delays are used in code to freeze the state of the controller for a
specified amount of time. The delay function we are using is measured in
milliseconds and has a
`range <https://www.google.com/url?q=https://docs.google.com/document/d/1BmZbXzxnD2j17QToSZ9jeZmnP7burwfksfQq2v4zu-Y/edit%23heading%3Dh.7lc2dw9cimru&sa=D&ust=1587613173867000>`__
from 0 to 10,000 milliseconds and only in whole numbers. 

Below is an example of the delay command. In this example, the delay is
set for 1500 milliseconds (or 1.5 seconds).

.. code-block:: c

   delay(1500);  //Produces a 1.5 second delay

Note that fractional delays do not work. For delays below 1ms you will need to use a different function, delayMicroseconds() which is covered in a later lesson.

.. code-block:: c

   delay(.25);  //THIS DOES NOT WORK
   
Code
----

1. Write a program to turn your LED on and off and on again. The program
   should turn your LED on for two seconds and then off for one second
   and then back on. This code should again be placed in your setup
   function.

IMPORTANT: Do not forget to make sure to set the pin the LED is using to
an output.

TEACHER CHECK \_\_\_\_\_
