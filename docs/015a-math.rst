Math
=========

Overview
--------

It is possible to perform any mathematical operation in your code. The most common operations are addition, subtraction, multiplication and
division of variables. The following shows the operation of adding 4 to the original value of m.

.. code-block:: c
 
  m = m + 4;
  
In the above example if m was initially 3 than the value of m after the addition is 7. You might wonder why you cann not just write
m + 4. In order to store a new value in a variable you must use the equals sign. Essentially, you need to add 4 to m and THEN put this
new value into m. 

The 

Exercise:
~~~~~~~~~

1. Initialize the variable z at the top of your code file and set its
   initial value to 9.


.. code-block:: c

  int z = 9;    //Set the initial value of z to 9
  int r = 1;    //Set the initial value of r to 1;
  
  void setup() {
    z = z + 5;    //Add 5 to z
    r = z;        //Place the value of z into r
  }


