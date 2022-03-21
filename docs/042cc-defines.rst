Defines
=========

Overview
--------

In order to make your code more readable, it is helpful to use the #define notation. A #define is a preprocessor directives which means it is processed before your code is compiled into a hex file. The #define is followed by two values. Before your code is compiled every instance of the first value is replaced by the second.

Below are two example defines. Before this code compiles, every instance of START_BTN in your code will be replaced with a 2 and every instance of PRESSED in your code will be replaced with a 0. This is useful because words like START_BIN and PRESSED are far more readable than 2 and 0. Yet your compiler needs actual values 2 and 0 before it can compile the code. 

Defines can be written in any format you like, but convention strongly dictates that defines are written in all caps. This way it is very easy to see what defines are in your code. Note that you have already been using defines, HIGH, LOW, INPUT and OUTPUT which are pre-establised by the Arduino IDE.

.. code:: C

   #define START_BTN 2
   #define PRESSED 0
   

Below are two examples of how the above defines might be used in your code. Notice how much easier it is to read the first example versus the second.
 
.. code:: C

   pinMode(START_BTN, INPUT);

   int buttonValue = digitalRead(START_BTN);

   if (buttonValue == PRESSED) {
   // some code here
   }


.. code:: C

   pinMode(2, INPUT);

   int buttonValue = digitalRead(2);

   if (buttonValue == 0) {
   // some code here
   }

Exercise:
~~~~~~~~~

Write a program that takes a button input and turns on an LED. Include defines to make the code easier to read.
