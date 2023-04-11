Formating Variables
====================

Overview
--------

The following are some  techniques for formating variables which are slightly different because the command characters cannot be placed inside your print function.

For example, assuming there is a variable named x, you could print x in a column by using the following two statements.

.. code-block:: c
   
   Serial.print(x);        //Print the value of the variable x
   Serial.print('\n');     //Printe a new line.

Alternatively, you can using an additional command *Serial.println()* to print a new line after you print the variable. The following will also print the variable x in a single column.

.. code-block:: c
   
   Serial.println(x);
   
Exercise
------------

Print the following text and number as a variable in a column in your serial window. Note the number 7 should be printed as a variable.

.. code-block:: c
   
  New value = 7
  New value = 7
