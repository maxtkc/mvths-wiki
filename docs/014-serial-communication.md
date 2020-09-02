# Serial Communication

## Overview

Serial communication provides an excellent way to send data to and get data from your microcontroller. It can be used as a way to provide a human interface to your device allowing the user to type commands on the computer that control operations on your device. It is also commonly used to debug a problem in your device by providing a way to visualize what is happening in your code.

## Reading Data

Serial communication can be used to read the value a variable or the state of a sensor attached to a computer.

### Exercise:

1.  Use the following command to set up the serial port for the baud rate of 9600 bps.

                Serial.begin(9600);

2.  Use the following command to send the word “cat” to your terminal window. This command should be placed in your setup function. NOTE: If you cut and paste the code below you will need to replace the quotation marks as the characters on the page are different from the characters in your IDE.

                Serial.print(“cat”);

3.  Download your code to the microcontroller.
4.  Open the terminal window. If you are successful the word “cat” should be displayed in your terminal window.

TEACHER CHECK \_\_\_\_\_

## Looping Data

You can use the loop function to send data repeatedly to the terminal window.

### Exercise:

Repeat the steps above but instead of placing your serial.write command in the setup function, place it in the loop function. IMPORTANT: Make sure to add a delay of at least 100ms to your loop function. This will ensure that the program does not try to send data too quickly to the serial port.

TEACHER CHECK \_\_\_\_\_

FORMATING SERIAL COMMUNICATION

## Overview

In order to make the information you are sending to the terminal window readable, it is important to know how to format the text.

## Column and Separators

As you may have noted in the previous lesson, the word “cat” was displayed across the screen making it difficult to read. You can display text in a column by simply adding a carriage return at the end of each line using the following command.

Serial.println();

### Exercise:

1.  Write a program that repeatedly prints the word “robot” in your terminal window. Using the addition of the command shown above ensure that the word “robot” is displayed in a single column in your window.

TEACHER CHECK \_\_\_\_\_

2.  Modify your program so that it prints the word “robot” and the word “engineer” in two columns and a space between the words. This should be accomplished with at least three separate print statements.
3.  Modify your program so that a colon separates the two columns.
4.  Modify your program so that a [tab separates](https://www.google.com/url?q=https://docs.google.com/document/d/1BmZbXzxnD2j17QToSZ9jeZmnP7burwfksfQq2v4zu-Y/edit%23heading%3Dh.idcad0tlxp8n&sa=D&ust=1587613173880000) the two columns.

TEACHER CHECK \_\_\_\_\_
