Formating Serial Communication
==============================

Overview
--------

In order to make the information you are sending to the terminal window
more easily readable, it is important to know how to format the text.

Column and Separators
---------------------

As you may have noted in the previous lesson, the word "cat" was
displayed across the screen making it difficult to read. You can display
text in a column by simply adding a carriage return at the end of each
line using the following command. Note the addition of 'ln' at the end of the command.
This stands for line as in new line.

.. code-block:: c

   Serial.println();
   
In addition, the following commands will produce a tab, a space and a colon respectively. 
   
.. code-block:: c

   Serial.print('\t');		//produces a tab
   Serial.print(' ');		//produces a space
   Serial.print(':');		//produces a colon


Exercise:
~~~~~~~~~

1. Write a program that repeatedly prints the word "robot" in your
   terminal window. Using the addition of the command shown above ensure
   that the word "robot" is displayed in a single column in your window.

TEACHER CHECK \_\_\_\_\_

2. Modify your program so that it prints the word "robot" and the word
   "engineer" in two columns and a space between the words. Note that will want to print the word "robot" then print a space and then print the word
   "engineer" with a line return.
   
3. Modify your program so that a colon separates the two columns.

4. Modify your program so that a `tab
   separates the two columns.

TEACHER CHECK \_\_\_\_\_
