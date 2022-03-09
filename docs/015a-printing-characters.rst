Printing Characters
==============

Overview
--------

In this lesson you are going to learn about printing ASCII characters. These are the characters used to represent text letters, numbers and punctuation. The basic character set is represented by the (American Standard Code for Information Interchange) or ASCII table (shown below). This table was first established in 1961 and still represents a useful standard for characters.

.. figure:: images/ascii_table.png
   :alt: 

Under the Char columns you can see all letters of the alphabet in both lower case and upper case as well as a variety of punctuation and numbers.  The table provides way for your microcontroller and computer to have a common language for converting numbers to characters. Note that for each character under the Char columns there is a corresponding number in decimal that represents that character. For example, the decimal number 67 represents the character capital C, and the decimal number 51 represents thecharacter 3. 

In addition to printed characters you can see some control characters listed such as LINE FEED and CARRIAGE RETURN n the lower portion of the table. Since this table was first developed prior to the advent of modern computers, many of the control characters between 0 and 32 are no longer used. 

The following shows examples of how you might initialize a variable to hold a character. In the previous lesson, you learned about the variable type int which is designed to store whole numbers. In addition, there are many other variable types including char. The variable type char is used to store characters. 

.. code-block:: c

  char x = 'a';           //Stores an ASCII representation of a lower case 'a'.
  char myLetter = 'B';    //Stores an ASCII representation of an upper case 'B'.
  char num = '9';         //Stores an ASCII representation of the number 9.

It is worth noting that the actual values of variables above are stored in their numeric equivalents 97, 66 and 57 repsectively. 

.. code-block:: c

  char x = 't';
  char x = 116; //both are equivalent.
  
Exercise:
~~~~~~~~~

#. Initialize a new variable using the char type and set its initial value to a character. Print this charater repeatedly in a column in you serial monitor. Make sure to include a short delay so that the serial monitor does not crash.

#. Initialize a new variable using the char type and set its initial value to a number that represents a character in the ASCII table. Again, print this character in a column.
 
#. **Super Challenge** Modify your code file to print a letter in a single column in your serial monitor, but only using the Serial.print() function, NOT Serail.println(). A hint is that LINEFEED in the ASCII table sets a new line in your serial monitor.



