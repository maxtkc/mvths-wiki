Variable Types
==============

Overview
--------

So far you have initialized all of your variables as ints.

.. code-block:: c

  int x;
  int counter = 9;

But there are many other numeric variable types supported in C such as ( byte, int, unsigned int, long, unsigned long, float, double. 
Each variable type determines the overall range of numbers the variable supports. For example, an unsigned int supports a range of 0 to 65535. 

.. code-block:: c

  unsigned int r = 5;

This number might seem arbitary but it represents exactly 16 bits. When you initialize an int exactly 16 bits of storage space are reserved for that variable. An 
int, by comparison supports a range of -32768 to +32767. Note that this range represents a total of 65535 possible values (as with an unsigned int) but half of the 
range is positive and half of the range is negative. Essentially, one of the 16 bits is reserved for the sign. A signed int can represent negative numbers as well as 
positive numbers, but an int can represent a higher range of positive numbers.

Exercise:
~~~~~~~~~

1. Initialize a varible as each of the following types shown in the table below. Continously increment or decrement (add one or subtract one) from the variable in your 
loop function and 

TEACHER CHECK \_\_\_\_\_

2. Modify your program so that it prints the word "robot" and the word
   "engineer" in two columns and a space between the words. This should
   be accomplished with at least three separate print statements. An
   introduction to formating serial communication can be found `here <https://www.google.com/url?q=https://docs.google.com/document/d/1BmZbXzxnD2j17QToSZ9jeZmnP7burwfksfQq2v4zu-Y/edit#bookmark=id.l7j52u85ivgp>`__.



