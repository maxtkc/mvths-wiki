# Lcd Display

## Overview

Liquid Crystal Displays (LCDs) are a common interface on many electronic devices as they are low cost and fairly easy to use. The ones we will be using are alphanumeric which means that they can display letters and numbers and some custom characters.

The LCD you are using has a backpack that allows your microcontroller communicate with the LCD using I2C which requires only two wires (SDA for data and SCL for clock). If you don’t recall

### Exercise:

Follow the steps below to connect and use your LCD display.

IMPORTANT: Using the screw terminals on the LCD, you should cut and strip your own wire. Do NOT use precut jump wires because the screw terminals will damage them.

1.  Set up a standard microcontroller board.
2.  Disconnect the board from power. This way you will not hurt your LCD if you plug it in incorrectly.
3.  On the back of the LCD you will see five screw terminal connectors.

<!-- end list -->

1.  Connect the GND terminal to the ground on your board
2.  Connect the 5V terminal to the 5V logic on your board.
3.  Connect the CLK terminal to the SCL pin on your microcontroller
4.  Connect the DAT terminal to the SDA pin on your microcontroller.

 TEACHER CHECK \_\_\_\_

5.  Connect your circuit to power.

### Exercise:

In this exercise you will be sending simple text to your LCD screen.

1.  Make sure the library titled Adafruit LiquidCrystal is installed. If you don’t know how to install a library, you should refer to that section of this document.
2.  Use the following code to write text to the LCD. If you code does not compile make sure that you have the Adafruit LiquidCrystal library installed.

\#include "Adafruit\_LiquidCrystal.h"

// Connect via i2c, default address \#0 (A0-A2 not jumpered)

Adafruit\_LiquidCrystal lcd(0);

void setup() {

  // set up the LCD's number of rows and columns:

  lcd.begin(16, 2);

  // Print a message to the LCD.

  lcd.print("hello, world\!");

 }
