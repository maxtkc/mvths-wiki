# Overview

Binary is a way of representing numbers in base-2. It is also one of the number [bases](https://www.google.com/url?q=https://docs.google.com/document/d/1BmZbXzxnD2j17QToSZ9jeZmnP7burwfksfQq2v4zu-Y/edit%23heading%3Dh.r9xkk2b3evb&sa=D&ust=1587613174010000) commonly used in writing code. Base-2 numbers have exactly two digits, 0 and 1. These digits can be used to directly represent the two possible states in your microcontroller (5V or HIGH) and (0V or LOW). In this way, all numbers stored inside your microcontroller are represented directly in binary.

# Printing Binary

You can use the serial print command to print numbers in binary as well as decimal. The following print command will print a number in decimal by default.

#### Serial.print(6);                //this will print 6

Using an optional argument you can specify alternative base representations.

#### Serial.print(7, DEC);        //this will print 7

#### Serial.print(7, BIN);        //this will print 111

### Exercise:

1.  Using what you learned above print the numbers 1, 9 and 23 in both decimal and binary in your Serial Monitor.

TEACHER CHECK \_\_\_

2.  Print two columns of numbers, one in decimal and one in binary. These numbers should increment from 0 and have a .3 second delay between increments.

TEACHER CHECK \_\_\_\_

# Leading Zeros

It is often easier to read binary (and other base) numbers with leading zeros. Leading zeros are zeros placed to the left of the number you are printing or reading. You can find more information about leading zeros [here](https://www.google.com/url?q=https://docs.google.com/document/d/1BmZbXzxnD2j17QToSZ9jeZmnP7burwfksfQq2v4zu-Y/edit%23heading%3Dh.hf5nphnveoo6&sa=D&ust=1587613174013000).
