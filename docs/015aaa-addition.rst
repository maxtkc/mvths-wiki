Addition
=========

Overview
--------

It is possible to perform most mathematical operations in your code, but in this lesson we are going to start with addition. The following is an example of how to add 4 to the variable m. It is **important** that while this operation does result in a value of 6 it does **NOT** change the value of m. In the exercises below, you will see that you can add a value to a variable without changing the variable. This can be very useful. 

.. code-block:: c
 
 int m = 6;
 
  m + 4;  //4 is added to m which results in a total of 10, but the value of m remains 6.
  
  
In the following example, m and 4 are added together and the result of this operation is placed into m. In this case, m has a new value.

.. code-block:: c
 
 int m = 6;
 
  m = m + 4;  //4 is added to m and this value is now placed in m, so the new value of m is 10
  
Exercise
---------
#. Initialize a variable r at the top of your code and set its value to 6. 
#. In your loop function, add r and 4 as shown above. 
#. Print r in a column your serial monitor.

TEACHER CHECK ____

#. Move the addition of r and 4 into your print statement as shown below. 

.. code-block:: c
 
  Serial.println(r + 4);
  
  
TEACHER CHECK ____

#. 
  
In the above example if m was initially 3 than the value of m after the addition is 7. You might wonder why you cannot just write m + 4. The only way to set or change the value of a variable is with the equals sign. Adding 4 to m does create a new value, but does not change the value of m. Essentially, you need to add 4 to m and THEN put this new value into m. The following are examples of addition, subtraction, multipication and division.

.. code-block:: c

 x = x + 1;		//adds 1 to x
 z = z - 9;		//subtracts 9 from x
 y = y * 4;		//multiplies x by 4
 x = x / 7;		//divides x by 7

Exercise:
~~~~~~~~~

#. Read the following code and determine the final value of r at the bottom of the code. Write this value in your notebook. you do not need to write this code in the Arduino IDE or program your microcontroller.

   .. code-block:: c

     int z = 9;    //Set the initial value of z to 9
     int r = 1;    //Set the initial value of r to 1;
  
     void setup() {
       z = z + 5;    //Add 5 to z
       r = z;        //Place the value of z into r
     }

   TEACHER CHECK \_\_\_\_\_

#. Create a code file that prints a variable as it counts up from 5.

   #. Initialize a variable to the value of 5. Make sure to place the initialization above your setup function.

   #. Using the plus operator defined above, add one to the variable in your loop function. This way the variable will continue to count infinitely.

   #. Print out the value of your variable using the serial function. The values must be printed in a column and must start at 5.

   #. Add a half second delay in your loop so that it does not send data to the serial port too quickly.
   

   TEACHER CHECK \_\_\_\_\_

#. Modify your code so that the variable starts at the value 9 and counts down by one every 500 milliseconds. It should display the values in a column in your terminal window and begin at 9.

   TEACHER CHECK \_\_\_\_\_

#. Modify your code so that there are two variables x and y. The variable x should start at 6 and count up by 2. The variable y should start at 50 and count down by 2. The variables should be displayed in two columns in your terminal window.

   TEACHER CHECK \_\_\_\_\_
