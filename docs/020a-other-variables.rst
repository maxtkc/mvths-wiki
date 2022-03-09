Other Variables
==============

Overview
--------

So far you have initialized all of your variables as ints.

.. code-block:: c

  int x;
  int counter = 9;

But there are many other numeric variable types supported in C such as byte, int, unsigned int, long and unsigned long. Unlike variables in math which 
can be used for any number, there are limits to the range of numbers that a variables in code can hold. For every variables on your micrcontroller of computer
a physical space must be reserved to store that variable. The type of variable that you initialized determines how much space is stored and whether that 
variable can have a negative value. For example, when you initialize an unsigned int exactly 16 bits of space are reserved on your microcontroller
for that variable. With 16 bits of space it is possible to record a number from 0 to 65535. 

.. code-block:: c

  unsigned int r = 5;

What makes this a little more complicated is that a variable type can also be defined to store negative as well as positive numbers. An 
int (which can support negative numbers) also takes up 16 bits of space on your microcontroller, but since it can support both positive and negative numbers
it can record a range of -32768 to +32767. Note that this range represents the same a total of 65535 possible values as with an unsigned int, but half of the 
range is positive and half of the range is negative. 

Exercise:
~~~~~~~~~

1. Initialize a variable as a byte (8 bits). In your loop function continously add one to the variable and print the result in your serial monitor. Include a small delay of at   least 5ms so that the code does not crash the serial port. Record the highest value of the count in your notebook. When you initialize a variable as a byte is only 8 bits of space are reserved for the variable so the highest number it can reach will be significantly less. Once the microcontroller reaches the highest value of the byte is starts counting from zero again.

2. Initialize a varible as each of the following types shown in the table below. Continously increment or decrement (add one or subtract one) from the variable in your loop function and print the value in your serial monitor. Use this code to determine the highest and lowest value for each variable type. Copy the table to your note book.


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





