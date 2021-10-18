More Variable Types
==============

Overview
--------

In the previous lesson, you learned about basic variable types for whole numbers. In addition, there are variable types for characters and fractional numbers. Below we will
at the variable types, char, string, float and double. 

|**char**
The variable type char is used to store characters. Characters used to represent text both letters, numbers and punctuation. The basic character set available to us is 
represented by the (American Standard Code for Information Interchange) or ASCII table. This table was first established in 1961. 

.. figure:: images/ASCII-Table.png
   :alt: 

The ASCII table includes all letters of the alphabet in both lower case and upper case as well as a variety of punctuation and numbers. The table provides a way for your 
microcontroller and all computers to store character information (what you read on the screen) as numbers. As you can see in the table, the numbers from 0 to 127 in decimal represent all of the characters you need to represent text on your screen. For example, the number 43 represents the character capital C, and the number 51 represents the
character 3. Since this table was first developed prior to the advent of modern computers, many of the control characters between 0 and 32 are no longer used. 

Note that characters are initialized using single quotes as in the following.

.. code-block:: c

  int x = 'a';
  int myLetter = 'B';

Exercise:
~~~~~~~~~

1. Initialize a new variable using the char type and set it to a value in the ASCII table. Print this charater repeatedly in a column in you serial monitor. Make sure to
   include a short delay so that the serial monitor does not crash.

2.


.. code-block:: c

  int x;
  int counter = 9;
