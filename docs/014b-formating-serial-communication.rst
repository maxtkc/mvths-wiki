Formating Serial Communication
==============================

Overview
--------

In order to make the information you are sending to the terminal window more easily readable, it is important to know how to format the text.

Columns and Separators
---------------------

As you may have noted in the previous lesson, the word "cat" was displayed across the screen with no spaces making it difficult to read. You can display text in a column by printing a command character. There are two command characters available in the Serial function. One is a new line represented by '\n' and the other is a tab represented by '\t'. 

.. code-block:: c

   Serial.print('\t');		//produces a tab
   Serial.print('\n');		//produces a new line
   
The following code will write the word "dog" in a column. 

.. code-block:: c

   Serial.print("dog"); //This will print the word "dog"
   Serial.print('\n');  //This will create a new line
   
Exercise:
~~~~~~~~~

#. Write a program that repeatedly prints the word "robot" in your terminal window. The word "robot" should be displayed in a single column in your window as demonstrated below.

   .. code-block:: c

      robot
      robot
      robot

   TEACHER CHECK \_\_\_\_\_

#. Modify your program so that it prints the word "robot" and the word "engineer" in two columns separated by a tab as shown below. Your code should have one statement for printing "robot" and one statement for printing "engineer".  

   .. code-block:: c

      robot    engineer
      robot    engineer
      robot    engineer
   
#. Modify your program so that there are three columns of words.

   TEACHER CHECK \_\_\_\_\_
