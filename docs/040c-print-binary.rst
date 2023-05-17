Printing Binary
======

Overview
--------
By default, the print command prints numbers in decimal. By adding a second argument to the print command, you can print numbers in binary. 

.. code-block:: C

   Serial.print(6);                //this will print 6

Using an optional argument you can specify alternative base representations.

.. code-block:: C

   Serial.print(7, DEC);        //this will print 7

   Serial.print(7, BIN);        //this will print 111


Exercise:
~~~~~~~~~

#. Using what you learned above print the numbers 1, 9 and 23 in both decimal and binary in your Serial Monitor.

   TEACHER CHECK \_\_\_

#. Print two columns of numbers, one in decimal and one in binary. These numbers should start at zero and increment by one and have a .3 second delay between increments.

   TEACHER CHECK \_\_\_\_

