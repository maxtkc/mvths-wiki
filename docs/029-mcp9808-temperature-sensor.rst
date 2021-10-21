Mcp9808 Temperature Sensor
==========================

Overview
--------

In this lesson you will learn to use the MCP9808 temperature sensor. The
MCP9808 is a digital sensor that outputs temperature readings natively in
Celsius. This is the first complex device (as opposed to an individual component) you will be adding to your breadboard.

1. Always remove power from your board when setting up a complex device. This is generally a good idea when adding any component to your breadboard, but very important
   when adding a complex device. These devices cost more than individual components and can be damaged more easily. The easiest way to remove power from your board
   is to unplug the USB.
   
2. Carefully connect the device to your circuit following the schematic and instructions provided.

3. MOST IMPORTANT: Make sure the power and ground are attached correctly. Reversing these two connections is the number one reason for damaging and complex device.

4. Apply power to your board. If you see smoke or it gets hot, remove power immediately.

It communicates with a microcontroller using the I2C protocol
which is one of many `communication
protocols <https://www.google.com/url?q=https://docs.google.com/document/d/1BmZbXzxnD2j17QToSZ9jeZmnP7burwfksfQq2v4zu-Y/edit%23heading%3Dh.zbv2l6wpi6ec&sa=D&ust=1587613173970000>`__ you
will use.

Setup
-----

1. Find an MCP9808 in the bin labeled “Sensors(Light, Color and Temperature)”
2. Remove the power (USB cable) from your breadboard.
3. Insert the MCP9808 into your breadboard.
4. Connect Vdd to power and Gnd to ground.
5. Connect the SDA (data) and SCL (clock) communication pins to the SDA
   and SCL pins on your microcontroller. You can locate the I2C pins
   (SDA, SCL) on your Metro Mini from this
   `diagram <https://www.google.com/url?q=https://docs.google.com/document/d/1BmZbXzxnD2j17QToSZ9jeZmnP7burwfksfQq2v4zu-Y/edit%23heading%3Dh.m133u0p0njav&sa=D&ust=1587613173971000>`__.

TEACHER CHECK \_\_\_\_\_

Program
-------

1. Open the example file under File/Examples/Adafruit MCP9808
   Library/mcp9808test. If this file is not installed in your Examples
   folder, you will need to install it using the `manage
   libraries <https://www.google.com/url?q=https://docs.google.com/document/d/1BmZbXzxnD2j17QToSZ9jeZmnP7burwfksfQq2v4zu-Y/edit%23heading%3Dh.5ie0wlz76yki&sa=D&ust=1587613173972000>`__ function.
   Just search for “Adafruit MCP9808 Library” in library manager.
2. Download the file to your microcontroller.
3. Open the Serial Monitor and view the results.

TEACHER CHECK \_\_\_\_\_
