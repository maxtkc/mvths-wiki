Printing Characters
==============

Overview
--------

At the most basic level, computers store only numbers. All images, colors, lines, letters and punctuation are all represented by numbers. In this lesson you are going to learn how to print letters and punctuation from the ASCII (American Standard Code for Information Interchange) character set. The ASCII character set was established way back in 1961 as a way to represent a full set of english alphabet and punctuation in just eight bits. 

The basic character set is represented by the  or ASCII table (shown below). This table was first established in 1961 and still represents a useful standard for characters.

.. figure:: images/ascii_table.png
   :alt: 

Under the Char columns you can see all letters of the alphabet in both lower case and upper case as well as a variety of punctuation and numbers.  The table provides way for your microcontroller and computer to have a common language for converting numbers to characters. Note that for each character under the Char columns there is a corresponding number in decimal that represents that character. For example, the decimal number 67 represents the character capital C, and the decimal number 51 represents thecharacter 3. 

In addition to printed characters you can see some control characters listed such as LINE FEED, CARRIAGE RETURN, and HORIZONTAL TAB in the initial portion of the table. Since this table was first developed prior to the advent of modern computers, many of the control characters between 0 and 32 are no longer used. 

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

#. Initialize a new variable using the char type

#. Set the initial value of the new variable to a character i.e. a letter, number or punctuation mark. Remember to use single quotes.

#. Print this charater repeatedly in a column in you serial monitor. 

#. Initialize a new variable using the char type, but this time set its initial value to a number that represents a character in the ASCII table. Again, print this character in a column.

#. Modify your code so that your variable is initialized to an exclamation point. You can use either '!' or the number that refers to this character. In your loop function increase this variable by one each time through the loop. Now print the variable.

   TEACHER CHECK ___
 
#. **Super Challenge** Modify your code file to print a letter in a single column in your serial monitor, but only using the Serial.print() function, NOT Serail.println(). **HINT:** LINEFEED in the ASCII table sets a new line in your serial monitor.



