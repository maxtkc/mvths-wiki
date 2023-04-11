Formating
=========

Overview
--------

The following are some more techniques for formating your text and variables that will be helpful as you move forward. The first is that the command characters can be placed inside the text of your print function. The second is that you can print gramatical characters with single quotes.

The following two lines of code...

.. code-block:: c
   
   Serial.print("bike");
   Serial.print('\n');
   

...are equivalent to the following one line of code.

.. code-block:: c
   
   Serial.print("bike\n");
   
**NOTE: You cannot do the same when printing variables. When printing a variable, you must use an addtional print statement if you want a new line.**
 
Initializing
------------

In order to use a variable in your code, you must first set up the variable so the program knows the type and name of the variable. We call this initializing a variable. The following are three examples of how to initialize a variable.

.. code-block:: c
