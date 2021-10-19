Fractional Variable Types
==============================

Overview
--------

In addition to variable types for storing whole numbers and characters as you learned about in previous lessons, there is a variable type for storing
factional numbers. The variable type float or floating-point numbers can be as large as 3.4028235E+38 and as low as -3.4028235E+38. 
They are stored as 32 bits (4 bytes) of information. The following is an example of initializing a floating-point type.

While it may seem tempting to simply initialize every number as a float since it covers the widest range, it is best to only initialize variables to the size that you
need. Floats use a lot of memory and memory gets used up fast in microcontrollers.

.. code-block:: c
  
    float y = -3.797;

Exercise:
~~~~~~~~~

1. Write a program that displays a factional number in column your serial monitor.
2. Modify your program so that it repeatedly adds one one thousandth (.001) to your original number and
   displays that in a column in your serial monitor.
3. Modify your code to include the name of your variable in your code with an equals sign. For example, if your variable name is
   "bugs" than in your serial monitor I should see: "bugs = 9.04"
