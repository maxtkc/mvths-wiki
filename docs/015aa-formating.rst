Formating Variables
====================

Overview
--------

The following are some more techniques for formating variables which are slightly different for formating text. The first is that the command characters can be placed inside the text of your print function. The second is that you can print gramatical characters with single quotes.

The following two lines of code...

.. code-block:: c
   
   Serial.print("bike");
   Serial.print('\n');

...are equivalent to the following one line of code.

.. code-block:: c
   
   Serial.print("bike\n");
   
**NOTE: You cannot do the same when printing variables. When printing a variable, you must use an addtional print statement if you want a new line or using a different print statement as shown below.**

.. code-block:: c
   
   Serial.println(x);
   
Additionally it is possible to print grammatical characters using single quotes.

.. code-block:: c
   
   Serial.print(':'); //Prints a colon
   Serial.print(','); //Prints a comma
   Serial.print(' '); //Prints a space
 
