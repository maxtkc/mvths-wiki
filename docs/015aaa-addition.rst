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
#. **IMPORTANT:** Make sure to include a delay of at least 10ms so the serial communication does not crash your serial monitor.

   TEACHER CHECK ____

#. Move the addition of r and 4 into your print statement as shown below. 

   .. code-block:: c
 
      Serial.println(r + 4);
  
  
   TEACHER CHECK ____
   
#. Using the example above, write a program that prints a column of values starting at 6 and increasing by 3 indefinitely, as shown below.

   .. code-block:: c
 
     6
     9
     12
     15
     18
     ...
 
   TEACHER CHECK ____
  
