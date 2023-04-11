Formatting Text
==============================

Overview
--------

In order to make the information you are sending to the terminal window more easily readable, it is important to know how to format the text.

Columns and Separators
---------------------

As you may have noted in the previous lesson, the word "cat" was displayed across the screen with no spaces making it difficult to read. You can format text by adding control characters at the end of the text.  The addition of '\n' prodduces a new line and the addtion of '\t' produces a tab.

The following code will write the word "dog" in a column. 

.. code-block:: c

   Serial.print("dog\n"); //This will print the word "dog" with a new line
   
The following code will produce a two columns of words separated by a tab. 
   
.. code-block:: c

   Serial.print("dog\t"); //This will print the word "dog" with a tab
   Serial.print("cat\n"); //This will print the word "cat" with a new line
   
It is also possible to insert grammatical character to separate your columns as shown below.  
   
.. code-block:: c

   Serial.print("dog :"); //This will print the word "dog"
   Serial.print(" cat\n"); //This will print the word "dog"
   
Exercise:
~~~~~~~~~

#. Write a program that repeatedly prints the word "robot" in your terminal window. The word "robot" should be displayed in a single column in your window as demonstrated below.

   .. code-block:: c

      robot
      robot
      robot

   TEACHER CHECK ____

#. Modify your program so that it prints the word "robot" and the word "engineer" in two columns separated by a tab as shown below. Your code should have one statement for printing "robot" and one statement for printing "engineer".  

   .. code-block:: c

      robot    engineer
      robot    engineer
      robot    engineer
   
#. Modify your program so that there are three columns of words separated by hypens.

TEACHER CHECK ____
