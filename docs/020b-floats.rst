Floats
==============================

Overview
--------

In addition to variable types for storing whole numbers as you learned about in previous lessons, there is a variable type for storing factional numbers. The variable type float (for floating-point number) can store numbers between 3.4028235E+38 and -3.4028235E+38. floats need  32 bits (4 bytes) of storage space, twice as much as an int. While this may not seem like much, storage space can get used up quickly on a microcontroller, so it is best to only initialize variables to the size that you need for your program. The following is an example of initializing a floating-point type.

.. code-block:: c
  
    float y = -3.797;

Exercise:
~~~~~~~~~

#. Write a program that displays a fractional number in column your serial monitor.
#. Modify your program so that it repeatedly adds one one thousandth (.01) to your original number and displays that in a column in your serial monitor.
#. Modify your code to print the name of your variable in your code with an equals sign. For example, if your variable name is "dogs" and you set the initial value to 9.04 than in your serial monitor you should see:

.. code-block:: C

   dogs = 9.04
   dogs = 9.05
   dogs = 9.06
