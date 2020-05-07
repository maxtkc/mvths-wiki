# Overview

In this project you will be using a digital sensor to read temperature. Digital sensors are often more accurate but more complex to use as compared with analog sensors. The BS18B20 made by Dallas Semiconductor is a commonly used digital temperature sensor that can be networked with over 100 devices on a single wire.  The 1-Wire protocol which was developed by Dallas Semiconductor and is one of many [communication protocols](https://www.google.com/url?q=https://docs.google.com/document/d/1BmZbXzxnD2j17QToSZ9jeZmnP7burwfksfQq2v4zu-Y/edit%23heading%3Dh.zbv2l6wpi6ec&sa=D&ust=1587613174080000) you will learn how to use to communicate with a variety of devices.

# Circuit Testing

In this section, you will connect your digital sensor to your microcontroller so that you can display the data from the sensor on your serial monitor.

## Diagram

Using the [datasheet](https://www.google.com/url?q=https://datasheets.maximintegrated.com/en/ds/DS18B20.pdf&sa=D&ust=1587613174081000) for the DS18B20 find the range of temperature the DS18B20 is capable of measuring.

Low Temperature: \_\_\_\_\_\_\_ Celsius                High Temperature: \_\_\_\_\_\_\_\_\_ Celsius

Low Temperature: \_\_\_\_\_\_\_ Fahrenheit        High Temperature: \_\_\_\_\_\_\_\_ Fahrenheit

### Exercise:

1.  Draw a front view diagram of the DS18B20 including labels for all three pins. The diagram can be found on page one of the DS18B20 datasheet (which can be found using the link above.)

<!-- end list -->

2.  Disconnect power (USB) from your circuit and using the diagram below, wire the device to your breadboard.

![](images/image27.png)

TEACHER CHECK \_\_\_\_

3.  Connect power (USB) back to your breadboard.

## Software

There are a variety of libraries and sample programs designed for the DS18B20. For this lesson, we will be using the example file “DS18x20\_temperature”.

### Exercise

1.  Open the example file, Examples/OneWire/DS18x20\_temperature. If this file is not installed in your Examples folder, you will need to install it using the [manage libraries](https://www.google.com/url?q=https://docs.google.com/document/d/1BmZbXzxnD2j17QToSZ9jeZmnP7burwfksfQq2v4zu-Y/edit%23heading%3Dh.5ie0wlz76yki&sa=D&ust=1587613174083000) function. Just search for “onewire” in library manager. Select the library titled “OneWire” by Jim Studt.
2.  Connect the output of the DS18B20 to pin 10 (MetroMini) of your microcontroller as noted at the top of the example code.
3.  Download and run the program. View the results in your serial monitor.
4.  Record the temperature below.

<!-- end list -->

1.  Centigrade: \_\_\_\_\_\_\_\_\_
2.  Farhenheit: \_\_\_\_\_\_\_\_\_

TEACHER CHECK \_\_\_\_

## Multiple Sensors

It is also possible to connect multiple DS18B20 sensors to the same signal line. In order that these devices do not conflict each of the millions of DS18B20’s manufactured has a unique ID represented in  64 bits.

### Exercise

1.  Insert second sensor in your breadboard.
2.  Connect the power and ground pins
3.  Connect the output pin to the output pin of the other DS18B20 on your board. Note that you will NOT need an additional pull-up resistor.

TEACHER CHECK \_\_\_\_

4.  Download and run the program. View the results in your serial monitor. Note that this software provides a lot of information. The following is an example. The ROM number indicates the unique ID number for the sensor. Chip identifies the type of sensor. Data indicates the raw data from the sensor.

![](images/image93.png)

5.  Record the temperatures sensor IDs in the table below.

|           |            |            |
| --------- | ---------- | ---------- |
| Sensor ID | Centigrade | Fahrenheit |
|           |            |            |
|           |            |            |

6.  Do they each produce the same temperature reading?
