Math
=========

Overview
--------

It is possible to perform any  `mathematical operation <https://www.google.com/url?q=https://docs.google.com/document/d/1BmZbXzxnD2j17QToSZ9jeZmnP7burwfksfQq2v4zu-Y/edit%23heading%3Dh.j1vujjth5hql&sa=D&ust=1587613173884000>`__ in your code. The most common operations are addition, subtraction, multiplication and
division of variables. The following shows the operation of adding 4 to the original value of m.

.. code-block:: c
 
  m = m + 4;
  
In the above example if m was initially 3 than the value of m after the addition is 7. You might wonder why you cann not just write
m + 4. In order to store a new value in a variable you must use the equals sign. Essentially, you need to add 4 to m and THEN put this
new value into m. The following are examples of addition, subtraction, multipication and division.

.. code-block:: c

 x = x + 1;		//adds 1 to x
 z = z - 9;		//subtracts 9 from x
 y = y * 4;		//multiplies x by 4
 x = x / 7;		//divides x by 7

Exercise:
~~~~~~~~~

1. Read the following code and determine the final value of r at the bottom of the code. Write this value 
   in your notebook.

.. code-block:: c

  int z = 9;    //Set the initial value of z to 9
  int r = 1;    //Set the initial value of r to 1;
  
  void setup() {
    z = z + 5;    //Add 5 to z
    r = z;        //Place the value of z into r
  }

   TEACHER CHECK \_\_\_\_\_

2. Create a code file that prints a variable as it counts up from 5.

   #. Initialize a variable to the value of 9. Make sure to place the initialization above your setup function.

   #. Using the plus operator defined above, add one to the variable in your loop function. This way the variable will continue to count infinitely.

   #. Print out the value of your variable using the serial function.

   #. Add a half second delay in your loop so that it does not send data to the serial port too quickly.

   TEACHER CHECK \_\_\_\_\_

3. Modify your code so that the variable starts at the value 9 and
   counts down by one every 500 milliseconds. It should display the
   values in a column in your terminal window.

   TEACHER CHECK \_\_\_\_\_

4. Modify your code so that there are two variables x and y. The
   variable x should start at 6 and count up by 2. The variable y should
   start at 50 and count down by 2. The variables should be displayed in
   two columns in your terminal window.

   TEACHER CHECK \_\_\_\_\_
