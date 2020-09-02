# Mcp9808 Temperature Sensor

## Overview

In this lesson you will learn to use the MCP9808 temperature sensor. The MCP9808 is a digital sensor that produces the temperature natively in Celsius. It communicates with a microcontroller using the I2C protocol which is one of many [communication protocols](https://www.google.com/url?q=https://docs.google.com/document/d/1BmZbXzxnD2j17QToSZ9jeZmnP7burwfksfQq2v4zu-Y/edit%23heading%3Dh.zbv2l6wpi6ec&sa=D&ust=1587613173970000) you will use.

# Setup

1.  Find an MCP9808 in the bin labeled “Temperature Sensor”
2.  Remove the power (USB cable) from your breadboard.
3.  Insert the MCP9808 into your breadboard.
4.  Connect Vdd to power and Gnd to ground.
5.  Connect the SDA (data) and SCL (clock) communication pins to the SDA and SCL pins on your microcontroller. You can locate the I2C pins (SDA, SCL) on your Metro Mini from this [diagram](https://www.google.com/url?q=https://docs.google.com/document/d/1BmZbXzxnD2j17QToSZ9jeZmnP7burwfksfQq2v4zu-Y/edit%23heading%3Dh.m133u0p0njav&sa=D&ust=1587613173971000).

TEACHER CHECK \_\_\_\_\_

# Program

1.  Open the example file under File/Examples/Adafruit MCP9808 Library/mcp9808test. If this file is not installed in your Examples folder, you will need to install it using the [manage libraries](https://www.google.com/url?q=https://docs.google.com/document/d/1BmZbXzxnD2j17QToSZ9jeZmnP7burwfksfQq2v4zu-Y/edit%23heading%3Dh.5ie0wlz76yki&sa=D&ust=1587613173972000) function. Just search for “Adafruit MCP9808 Library” in library manager.
2.  Download the file to your microcontroller.
3.  Open the Serial Monitor and view the results.

TEACHER CHECK \_\_\_\_\_
