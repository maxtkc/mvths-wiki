Functions
======

Overview
--------

In this lesson, you will write your own function. So far, you have used many functions that were pre-written for you such as, delay(), digitalWrite(), Serial.print(), etc. You have also modified two functions (setup and loop) that are created by the IDE. One of the most powerful features of programming is the ability to write your own functions. Creating a function allows you to avoid writing the same code multiple times. For example, the delay() function involves many lines of code. If you did not have access to this function, you would need to add all these same lines of code to your code file everywhere you want to use a delay. Instead, you can just call the function with one line of code whenever you need to use it. 

The following is an example of a very simple function that accepts a value, multiplies it by two and returns the result. For example, if you passed the value 4 to the function, you would get back the value 8. 
.. code:: 

   void times_two(int val) {
      val *= 2;
      return val;
   }

Passing a value to this function would look like the following.

.. code::

   x = times_two(6);  // Pass the value 6 to the function times_two and place the result in the variable x. 
   
The value of x is now 12 since it was multiplied by two by the function.

When writing a function, you can name a function anything you want, but it is good to give it a name that indicates what is does. In case above, the function times_two multiplies a number by 2. You must also create a variable for the argument (or number) passed to the function. In the case above, the variable is named val. Again, try to use variable names that indicate the purpose of the variable.

   
   
   
Exercise:
~~~~~~~~~

Create a function to convert Celsius to Fahrenheit. This is a simple function and used here just to provide some experience with how to write a function. 
