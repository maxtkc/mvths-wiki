Serial Communication
====================

Overview
--------

Serial communication provides an excellent way to send data from your computer to your microcontroller and to send data from your microcontroller to your computer. It can be used as a way to provide a human interface to your device allowing the user to type commands on the computer that control operations on your device. It is also commonly used to debug a problem in your device by providing a way to visualize what is happening in your code.

Technically, serial communication can refer to many different protocols including, SPI, I2C, CAN which you will learn about later. But in this case we are using serial communication to refer to USART. USART is a very old serial communication protocol which stands for Universal Synchronous/Asynchronous Receiver/Transmitter. It uses two lines for communication, RX for receiving data and TX for transmitting data. Some devices such as the Arduino Uno have these pins labled. On the Metro Mini Rx is pin 0 and TX is pin 1. Though you do not need to connect these pins because they are routed through the USB cable by the circuit board.

Reading Data
------------

Using the serial command you will send data (numbers and text) from your microcontroller to your computer. Serial data must be tranmitted at a specific speed or baudrate. The baud is named for Jean-Maurice-Emile Baudot and is measured is bits per second (bps). The default baudrate in Arduino IDE is 9600 bps. The computer must also be set up to receive the serial data at the same baud rate.

Exercise:
~~~~~~~~~

1. Use the following command to set up the serial port on your microcontroller and set the transmission rate to 9600 bps. This command only needs to be run once in your code so where should you put it?

.. code-block:: c

   Serial.begin(9600);

2. Use the following command to send the word "cat" to your terminal window. This command also only needs to be run once.

.. code-block:: c

   Serial.print("cat");

3. Upload the code to the microcontroller.
4. Open the terminal window on our Arduino IDE using the button shown on the far right below. It looks a bit like a magnifying glass.

   .. figure:: images/serialmonitor.PNG
      :alt: 
   
5. If you are successful the word "cat" should be displayed in your terminal window. If you do not see the word "cat" make sure the baud rate on the terminal window is also set to 9600. You can find the baudrate setting on the bottom left of the terminal window as shown below. NOTE: The baud rate set in your code and the baudrate set in the window must match.

   .. figure:: images/Baudrate96.PNG

TEACHER CHECK \_\_\_\_\_

