Defines
=========

Overview
--------

In order to make your code more readable, it is helpful to use the #define notation. A #define is a preprocessor directives which means it is processed before your code is compiled into a hex file. The #define is followed by two values. Before your code is compiled every instance of the first value is replaced by the second.

Below are two example defines. Before this code compiles, every instance of START_BTN in your code will be replaced with a 2 and every instance of PRESSED in your code will be replaced with a 0. This is useful because words like START_BIN and PRESSED are far more readable than 2 and 0. Yet your compiler needs actual values 2 and 0 before it can compile the code. 

Defines can be written in any format you like, but convention strongly dictates that defines are written in all caps. This way it is very easy to see what defines are in your code. Note that you have already been using defines, HIGH and LOW which are pre-establised by the Arduino IDE.

.. code:: C

   #define START_BTN 2
   #define PRESSED 0
   
   
 
.. code:: C

   pinMode(START_BTN, INPUT);

   int buttonValue = digitalRead(START_BTN);

   if (buttonValue == PRESSED) {
   // some code here
   }



asdfasf
