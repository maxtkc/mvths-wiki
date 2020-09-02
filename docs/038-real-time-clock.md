# Real Time Clock

## Overview

In this lesson, you will learn how to use an external real time clock (RTC) to create a clock circuit. The IC you will be using is a [DS1307](https://www.google.com/url?q=https://datasheets.maximintegrated.com/en/ds/DS1307.pdf&sa=D&ust=1587613174000000) made by Dallas Semiconductor. The device can keep track of time, date and day of week. It can automatically adjust for days in a month (30 vs 31) and can account for leap year. It can also be used with a low power battery backup to keep time during loss of power. This device also uses I2C as its communication protocol.

![](images/image48.png)![](images/image100.png)

DS1307 IC (left) and 32.768Khz clock crystal (right)

# Circuit

Below is the sample circuit diagram from the [DS1307](https://www.google.com/url?q=https://datasheets.maximintegrated.com/en/ds/DS1307.pdf&sa=D&ust=1587613174001000) datasheet. Use this diagram to complete the circuit on your breadboard. You will NEED to use the datasheet to determine which pin on the DS1307 is GND, SDA, SCL etc. You can find the DS1307 in the grey bins under ICs marked Misc IC. Notes:

  - You do not need to connect SQWT/OUT or Vbat.
  - The crystal is  a 32.768Khz clock crystal.
  - The pull-up resistors (Rpu) are both 10K
  - Connect SCL from the DS1307 to SCL on the Metro Mini
  - Connect SDA from the DS1307 to SDA on the Metro Mini

![](images/image18.png)

# Code

Open the file under Examples/Grove - RTC DS1307/SetTimeAndDisplay. If this file does not exist use the manage library function to find the Grove - RTC DS1307 library. Upload the code to the Metro Mini and open the Serial Monitor. You should see the time on the left and the date on the right.

# Set Time

You can set the time in the Setup function in your code. Try setting different times and dates. Note that you will need to set the correct day-of-week.

# 12 Hour vs 24 Hour

The DS1307 can be set for either 24 hour or 12 hour time. The software library you are using may be set for 24 hour time. You can test the format by setting the time to 12:59:55 and wait five seconds to see if it changes to 1:00 or 13:00.

# Change to 12 hour time (optional)

If your library is set to 24 hour time you can convert it to 12 hour time, by following the steps below to convert the library code itself.

1.  Open your Windows file manager
2.  Navigate to My Documents/Arduino/libraries/Grove RTC DS1307
3.  Right click on DS1307.cpp and Open with Atom
4.  Scroll down to the function void DS1307::getTime
5.  As shown below comment out the first line and add the second line.

#### //hour = bcdToDec(Wire.read() & 0x3f);// Need to change this if 12 hour am/pm

####          hour = bcdToDec(Wire.read() & 0x1f);

6.  Scroll down to the function void DS1307::setTime
7.  As shown below comment out the first line and add the second line.

#### //Wire.write(decToBcd(hour)); // If you want 12 hour you need to set bit 6

####     Wire.write(decToBcd(hour)|0x40);

TEACHER CHECK \_\_\_\_

# Time

Run the example code and show the results in the serial monitor.

TEACHER CHECK \_\_\_\_

# Minimize Code

As with other lessons, save a copy of the code and minimize the code. In this case, minimize the code to just display the time including hour, minute and second.

TEACHER CHECK \_\_\_\_
