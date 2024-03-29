Other Variables
==============

Overview
--------

So far you have initialized all of your variables as ints. An int, when compiled for the Arudino Uno, Metro Mini or any board based on an 8-bit Atmel processor, defines a type of variable that has a total of 16-bits. (For SAMD-based boards the value is 32-bits). This means there are 16 bits of storage reserved for this variable. ints are also signed. This means the variable can be a negative or positive number.

.. code-block:: c

  int x;
  int counter = 9;

There are also many other numeric variable types supported in C including byte, unsigned int, long and unsigned long. Unlike variables in math which can be used for any number, there are limits to the range of numbers that a variables in code can hold. For every variable type in code, a fixed amount space on the micrcontroller must be reserved to store that variable. The variable type determines the amount of storage space reserved. For example, when you initialize an *unsigned int* exactly 16 bits of space are reserved on your microcontroller for that variable. With 16 bits of space it is possible to record a number from 0 to 65535. 

.. code-block:: c

  unsigned int color = 5;
  byte f = 2;
  long z = 34900;

What makes this a little more complicated is that some variable typess can store negative and positive values and some can only store positive values. An int (which can support negative and positive numbers) also takes up 16 bits of space on your microcontroller, but since it can support both positive and negative numbers it can store a range of -32768 to +32767. Note that this range represents the same a total of 65535 possible values as with an unsigned int, but half of the range is positive and half of the range is negative. Also, note that the variable types listed here can **ONLY store whole numbers.** Variables that can store fractional numbers will be addressed in the next lesson. 

Exercise:
~~~~~~~~~

#. Initialize a variable as a byte (8 bits). In your loop function continously add one to the variable and print the result in your serial monitor. Include a small delay of at   least 5ms so that the code does not crash the serial port. Record the highest value of the count in your notebook. When you initialize a variable as a byte, only 8 bits of space are reserved for the variable so the highest number it can reach will be significantly less than with an int. Once the microcontroller reaches the highest value of the byte is starts counting from zero again.

#. Copy the table to your note book. Initialize a varible as a byte. Continously increment or decrement (add one or subtract one) from the variable in your loop function and print the value in your serial monitor. Use this code to determine the highest and lowest value for the byte type. Add these values to your table. For the remainder of the variable types, look up the highest and lowest values for each type.


.. list-table:: Ohms Law
   :widths: 25 25 50
   :header-rows: 1

   * - Variable type
     - Lowest value
     - Highest value
   * - byte
     - 
     - 
   * - int
     - 
     - 
   * - unsigned int
     - 
     - 
   * - long
     - 
     - 
   * - unsigned long
     -
     - 

TEACHER CHECK \_\_\_\_\_





