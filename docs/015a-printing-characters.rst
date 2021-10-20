Printing Characters
==============

Overview
--------

In the previous lesson, you learned about the variable type int which is designed to store whole numbers. In addition, there are many other variable types including char.
The variable type char is used to store characters. Characters used to represent text both letters, numbers and punctuation. The basic character set available to us is 
represented by the (American Standard Code for Information Interchange) or ASCII table. This table was first established in 1961. 

.. figure:: images/ASCII-Table.png
   :alt: 

The ASCII table includes all letters of the alphabet in both lower case and upper case as well as a variety of punctuation and numbers. The table provides a way for your 
microcontroller and all computers to store character information (what you read on the screen) as numbers. As you can see in the table, 
the numbers from 0 to 127 in decimal represent all of the characters you need to represent text on your screen. For example, the decimal 
number 67 represents the character capital C, and the decimal number 51 represents thecharacter 3. Since this table was first developed prior 
to the advent of modern computers, many of the control characters between 0 and 32 are no longer used. 

Note that characters are initialized using single quotes as in the following.

.. code-block:: c

  char x = 'a';           //Stores an ASCII representation of a lower case 'a'.
  char myLetter = 'B';    //Stores an ASCII representation of a lower case 'a'.
  char num = '9';         //Stores an ASCII representation of the number 9.

It is worth noting that the actual values of variables above (in decimal) are stored in their numeric equivalents 97, 66 and 57 repsectively. 

.. code-block:: c

  char x = 't';
  char x = 116; //both are equivalent.
  

Exercise:
~~~~~~~~~

1. Initialize a new variable using the char type and set it to a letter value in the ASCII table. Print this charater repeatedly in a column in you serial monitor. Make sure to
   include a short delay so that the serial monitor does not crash.

2. Initialize a new variable using the char type and set it to a number value in the ASCII table. Again, print this character in a column.

3. Initialize a new char and this time set it to the ASCII number value of a character. For example if you wanted to print 'W' you would set the value of your 
   char to 87. Note there are no quotes. Print this value in a column.
4. **Super Challenge** Modify your code file to print a letter in a single column in your serial monitor, but only using the Serial.print() function, 
   NOT Serail.println(). A hint is that LINEFEED in the ASCII table sets a new line in your serial monitor.



