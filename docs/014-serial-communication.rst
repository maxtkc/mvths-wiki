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

.. code-block:: c

   Serial.begin(9600);

2. Use the following command to send the word "cat" to your terminal
   window. This command also only needs to be run once. NOTE: If you 
   cut and paste the code below you will need to replace the
   quotation marks with ones typed from your keyboard. The characters 
   on the page in your guide are different from the characters in your IDE.

.. code-block:: c

   Serial.print("cat");

3. Upload the code to the microcontroller.
4. Open the  `terminal window <https://docs.google.com/document/d/1BmZbXzxnD2j17QToSZ9jeZmnP7burwfksfQq2v4zu-Y/edit#bookmark=id.t0c1bmp6om>`__. 
If you are successful the word "cat" should be displayed in your terminal window.

TEACHER CHECK \_\_\_\_\_

