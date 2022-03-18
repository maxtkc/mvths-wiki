Defines
=========

Overview
--------

In order to make your code more readable, it is useful to take advantage of the #define notation. A #define is one of the preprocessor directives that can be used in C. A preprocessor directive is specifically a directive that is processed before your code is compiled. #define acts as a simple find and replace in your code.

Below is an example of two defines. Before this code compiles, ,  #define that will substitute the number 2 for the text START_BTN. This means that before you code compiles, the number 2 will be used to replace the text START_BTN anywhere in your code.

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
