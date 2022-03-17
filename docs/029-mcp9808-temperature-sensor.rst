Mcp9808 Temperature Sensor
==========================

Overview
--------

In this lesson you will learn to use the MCP9808 temperature sensor. The MCP9808 is a digital sensor that outputs temperature readings natively in Celsius. This is the first complex device (as opposed to an individual component) you will be adding to your breadboard.

The components you have used so far communicate with your microcontroller either directly with one of your digital ports as in a button which produces either a high or low signal, or directly with an analog port as in a light sensor which coupled with a resistor can produce a voltage level. The MCP9808 is the first of many devices that communicates with your micrcontroller using a complex protocol called I2C. This protocol uses two lines for communication. One line, SCL, represents the clock signal. The other line, SDA, represents the data signal. There is also a dedicated SCL and SDA line on your microcontroller. These lines must be connected together  (SDA to SDA and SCL to SCL) for the communication to work. 

Setup
-----

#. Find an MCP9808 in the bin labeled “Sensors(Light, Color and Temperature)”

#. Disconnect the power (USB cable) from your USB hub and follow all rules for complex devices.
#. Insert the MCP9808 into your breadboard.
#. Provide power to your MCP9808 by connecting Vdd of the MCP9808 to power and Gnd of the MCP9808 to ground.
#. Enable the MCP9808 to communicate with your Metro Mini. Connect the SDA (data) and SCL (clock) communication pins to the SDA and SCL pins on your microcontroller. On your Metro Mini or Arduino the SDA pin is A4 and the SCL pin is A5.

TEACHER CHECK \_\_\_\_\_

Program
-------

1. Open the example file under File/Examples/Adafruit MCP9808
   Library/mcp9808test. If this file is not installed in your Examples
   folder, ask your teacher for help.
2. Download the file to your microcontroller.
3. Open the Serial Monitor and view the results.

TEACHER CHECK \_\_\_\_\_
