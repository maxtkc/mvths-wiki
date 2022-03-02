Formating Serial Communication
==============================

Overview
--------

In order to make the information you are sending to the terminal window more easily readable, it is important to know how to format the text.

Columns and Separators
---------------------

As you may have noted in the previous lesson, the word "cat" was displayed across the screen with no spaces making it difficult to read. You can display text in a column by simply adding a carriage return at the end of each line using the following command. Note the addition of 'ln' at the end of the command. This stands for line as in new line.

.. code-block:: c

   Serial.println(); //This will put a line return in your terminal window.
   
.. code-block:: c

   Serial.println("hello"); //This will print "hello" and then add a line return.
   
In addition, the following commands will produce a tab, a space and a colon respectively. 
   
.. code-block:: c

   Serial.print('\t');		//produces a tab
   Serial.print(' ');		//produces a space
   Serial.print(':');		//produces a colon


Exercise:
~~~~~~~~~

#. Write a program that repeatedly prints the word "robot" in your terminal window. The word "robot" should be displayed in a single column in your window as demonstrated below.

   .. code-block:: c

      robot
      robot
      robot

   TEACHER CHECK \_\_\_\_\_

#. Modify your program so that it prints the word "robot" and the word "engineer" in two columns and a space between the words as shown below. To do this correclty, you will need to use at least two print statements, one for "robot" and one for "engineer". 

   .. code-block:: c

      robot engineer
      robot engineer
      robot engineer
   
#. Modify your program so that a colon separates the two columns.

#. Modify your program so that a `tab separates the two columns.

   TEACHER CHECK \_\_\_\_\_
