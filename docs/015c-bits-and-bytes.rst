Bits and Bytes
==============

Overview
--------
In this lesson, you will learn a little bit, no pun intended, about how information is stored on your microcontroller and computers in general. The microcontroller on your Arduino Uno or your Metro Mini both use an 8-bit architecture. By comparison, a modern Intel processor uses a 64-bit architecture. A bit refers to the smallest amount of data that can be stored on a processor. A bit is represented by a single transistor and can have only two possible states, on or off. Mathematically, we refer to these states as 1 and 0 respectively. To be clear, your microcontroller can store more than 8 bits of information, but it can only store 8 bits at a time, whereas the Intel processor can store 64 bits at a time. 

A byte is simply 8 bits. There are a number of stories about the origin of this term but my favorite and possibly most likely, is that a bite is bigger than a bit, but the spelling of bite would lead to confusion, so it was changed to byte. Its size can be remembered by thinking of byte as by-eight. Why data is measured in increments of 8 also seems to be under debate, but it may have been that some early computers used eight lines for communication. There also exists a nibble. A much less used term that refers to 4 bits. 

Generally, we print numbers in decimal (i.e. using the digits 0-9), but you can also print numbers as bits (or binary) and as they are represented in bits inside your controller. This can be done by adding the define BIN to your print statement as shown below.

.. code-block:: c

  Serial.println(x, BIN);    

Exercise
---------

#. Write a program that prints a column of numbers starting at zero incrementing by one. Make sure to include a short delay. 

#. Now change your print statement to print in bits or binary. Notice that the number is represented in zeros and ones. In a later lesson, we will show you how to convert numbers in binary format to decimal. What is important to note at this point is how my digits (1s or 0s) are represented on a single line. 


