# Registers Io

## Overview

In this section you will learn how to directly control the ATMega328 (the microcontroller on the Arduino board) using registers. Every function or command you have written using the Arduino libraries can be accomplished by directly writing to registers. In fact, this is exactly what is behind all of the Arduino libraries you have used so far.

The following sections will require you to use the [ATMega328 datasheet](https://www.google.com/url?q=http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-7810-Automotive-Microcontrollers-ATmega328P_Datasheet.pdf&sa=D&ust=1587613174384000)...which is over 600 pages\! In addition to the on-line version referenced above, I highly recommend using a printed version we have in the classroom.

## Registers

Registers are 8-bit memory locations that can be used to control any function on your microcontroller. Check out the section in concepts on [Registers](https://www.google.com/url?q=https://docs.google.com/document/d/1BmZbXzxnD2j17QToSZ9jeZmnP7burwfksfQq2v4zu-Y/edit%23heading%3Dh.f13ytdd3fjv&sa=D&ust=1587613174385000).

## Setting Pin Values

There are two registers involved in setting pin values. One register is used to control the direction of the pin (input or output). The other register is used to set the value of the pin. Setting these two registers would be equivalent to using the following commands in the Arduino library.

#### pinMode(3, OUTPUT);

#### digitalWrite(3, HIGH):

### Challenge:

On your ATMega328 set bit 3 of PortB to HIGH. In order to do this you will need to read the following section in the datasheet: Configuring the Pin 14.2.1 (printed version) 13.2.1 ([on-line version](https://www.google.com/url?q=http://ww1.microchip.com/downloads/en/DeviceDoc/Atmel-7810-Automotive-Microcontrollers-ATmega328P_Datasheet.pdf&sa=D&ust=1587613174386000)). You will also need to refer to the following register description: Register Description 14.4 (printed version) 13.4 (on-line version)

        

TEACHER CHECK \_\_\_\_

### Challenge:

On your ATMega328 read bit 2 of PORTC. If this bit is HIGH set bit 5 of PortB to HIGH. Set your circuit up with a button and an LED.  You will need to read section 14.2.4 Reading the Pin Value in your printed datasheet. IMPORTANT: Unless the pins on any port are physically tied to 5V or ground, they will float. For example if you read the value of PINC than ALL pins that are not tied to 5V or ground will be in an unknown state.

TEACHER CHECK \_\_\_\_

### Challenge:

Again using only C and no external libraries design a circuit and program that toggles the value of an LED when a button is pressed. You should read section 14.2.2. in your printed datasheet.

TEACHER CHECK \_\_\_
