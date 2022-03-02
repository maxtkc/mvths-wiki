Variables
=========

Overview
--------

Variables are placeholders used to store values that can be modified. Just as you use *x* or *y* to represent a number in algebra, you can use *x* or *y* as a place holder for a number in your code. This is particularly useful if you have a value in your code that is going to change. For example, if you wanted to keep track of the number of times a user pressed a button you could create a variable and call it "x" or "button" (or just about anything you like) and store the number of times a button was pressed in that variable.

Initializing
------------

In order to use a variable in your code, you must first set up the variable so the program knows the type and name of the variable. We call this initializing a variable. The following are three examples.

.. code-block:: c

   int x;         //A simple initialization with no initial value.
   int y = 9;     //Initializing a variable with an initial value of 9
   int dog = -2;  //Note that any set of characters can be usee for a variable name.

For the time being, you will initalize variables at the top of your code file, that is above and 
outside of both the loop and setup functions.  

Exercise:
~~~~~~~~~

1. Initialize the variable z at the top of your code file and set its
   initial value to 9.

.. raw:: html

   <!-- end list -->

2. Print the variable to your terminal window using the following
   command.
.. code-block:: c

   Serial.print(z);

TEACHER CHECK \_\_\_\_\_


