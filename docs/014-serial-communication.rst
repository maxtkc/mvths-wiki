Serial Communication
====================

Overview
--------

`Serial communication <https://docs.google.com/document/d/1BmZbXzxnD2j17QToSZ9jeZmnP7burwfksfQq2v4zu-Y/edit#bookmark=id.drcn0pnn5flp>`__
provides an excellent way to send data from your 
computer to your microcontroller and to send data from your 
microcontroller to your computer. It can be used as a way to provide a
human interface to your device allowing the user to type commands on the
computer that control operations on your device. It is also commonly
used to debug a problem in your device by providing a way to visualize
what is happening in your code.

Reading Data
------------

Using the serial command you will send data (numbers and text) from
your microcontroller to your computer. Serial data must be tranmitted
at a specific speed or `baud rate <https://docs.google.com/document/d/1BmZbXzxnD2j17QToSZ9jeZmnP7burwfksfQq2v4zu-Y/edit#bookmark=id.akrmhbnr74pi>`__. The baud is named for Jean-Maurice-Emile 
Baudot and is measured is bits per second (bps). The computer must
also be set up to receive the serial data at the same baud rate.

Exercise:
~~~~~~~~~

1. Use the following command to set up the serial port on your 
microcontroller and set the transmission rate to 9600 bps. This
command only needs to be run once in your code so where should 
you put it?

                Serial.begin(9600);

2. Use the following command to send the word "cat" to your terminal
   window. This command also only needs to be run once. NOTE: If you 
   cut and paste the code below you will need to replace the
   quotation marks with ones typed from your keyboard. The characters 
   on the page in your guide are different from the characters in your IDE.

                Serial.print("cat");

3. Upload the code to the microcontroller.
4. Open the  `terminal window <https://docs.google.com/document/d/1BmZbXzxnD2j17QToSZ9jeZmnP7burwfksfQq2v4zu-Y/edit#bookmark=id.t0c1bmp6om>`__. 
If you are successful the word "cat" should be displayed in your terminal window.

TEACHER CHECK \_\_\_\_\_

Looping Data
------------

You can use the loop function to send data repeatedly to the terminal
window.

Exercise:
~~~~~~~~~

Repeat the steps above but instead of placing your serial.write command
in the setup function, place it in the loop function. IMPORTANT: Make
sure to add a delay of at least 100ms to your loop function. This will
ensure that the program does not try to send data too quickly to the
serial port.

TEACHER CHECK \_\_\_\_\_

FORMATING SERIAL COMMUNICATION

Overview
--------

In order to make the information you are sending to the terminal window
readable, it is important to know how to format the text.

Column and Separators
---------------------

As you may have noted in the previous lesson, the word “cat” was
displayed across the screen making it difficult to read. You can display
text in a column by simply adding a carriage return at the end of each
line using the following command.

Serial.println();

Exercise:
~~~~~~~~~

1. Write a program that repeatedly prints the word “robot” in your
   terminal window. Using the addition of the command shown above ensure
   that the word “robot” is displayed in a single column in your window.

TEACHER CHECK \_\_\_\_\_

2. Modify your program so that it prints the word “robot” and the word
   “engineer” in two columns and a space between the words. This should
   be accomplished with at least three separate print statements.
3. Modify your program so that a colon separates the two columns.
4. Modify your program so that a `tab
   separates <https://www.google.com/url?q=https://docs.google.com/document/d/1BmZbXzxnD2j17QToSZ9jeZmnP7burwfksfQq2v4zu-Y/edit%23heading%3Dh.idcad0tlxp8n&sa=D&ust=1587613173880000>`__ the
   two columns.

TEACHER CHECK \_\_\_\_\_
