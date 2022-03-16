Mcp9808 Temperature Sensor
==========================

Overview
--------

In this lesson you will learn to use the MCP9808 temperature sensor. The MCP9808 is a digital sensor that outputs temperature readings natively in Celsius. This is the first complex device (as opposed to an individual component) you will be adding to your breadboard.

It communicates with a microcontroller using the I2C protocol which is one of many communication protocols you will use.

Setup
-----

#. Find an MCP9808 in the bin labeled “Sensors(Light, Color and Temperature)”

#. Remove the power (USB cable) from your breadboard and follow all rules for complex devices.
#. Insert the MCP9808 into your breadboard.
#. Provide power to your MCP9808. Connect Vdd of the MCP9808 to power and Gnd of the MCP9808 to ground.
#. Enable the MCP9808 to communicate with your Metro Mini. Connect the SDA (data) and SCL (clock) communication pins to the SDA
   and SCL pins on your microcontroller. On your Metro Mini or Arduino the SDA pin is A4 and the SCL pin is A5.

TEACHER CHECK \_\_\_\_\_

Program
-------

1. Open the example file under File/Examples/Adafruit MCP9808
   Library/mcp9808test. If this file is not installed in your Examples
   folder, ask your teacher for help.
2. Download the file to your microcontroller.
3. Open the Serial Monitor and view the results.

TEACHER CHECK \_\_\_\_\_
