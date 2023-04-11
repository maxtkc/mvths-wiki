Variables
=========

Overview
--------

Variables are placeholders used to store values that can be modified. Just as you use *x* or *y* to represent a number in algebra, you can use *x* or *y* as a place holder for a number in your code. This is particularly useful if you have a value in your code that is going to change. For example, if you wanted to keep track of the number of times a user pressed a button you could create a variable and call it "x" or "button" (or just about anything you like) and store the number of times a button was pressed in that variable.

Initializing
------------

In order to use a variable in your code, you must first set up the variable so the program knows the type and name of the variable. We call this initializing a variable. The following are three examples of how to initialize a variable.

.. code-block:: c

   int x;         // This initializes x as a variable with no initial value.
   int y = 9;     // This initializes x as a variable with an initial value of 9.
   int dog = -2;  // This initializes dog as a variable with an initial value of -2.

For the time being, you will initalize all variables at the top of your code file, that is above and outside of both the loop and setup functions as shown below. Note that setting your varible at the top of your code file makes it a global variable. We will learn more about what that means later.

.. code-block:: c

   int count;         // This initializes count as a variable with no initial value.
   
   void setup() {
    // Your code goes here.
   }

Exercise:
~~~~~~~~~

#. Initialize the variable z at the top of your code file and set its initial value to 9.

#. Print the variable to your terminal window using the following command.

   .. code-block:: c

      Serial.print(z);
 
#. Initialize two variables and give them different initial values.

#. Print both values in two colums separated by a tab.

TEACHER CHECK ____
