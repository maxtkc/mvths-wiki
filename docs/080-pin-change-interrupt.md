# Pin Change Interrupt

## Overview

The ATMega328 is capable of calling an interrupt based on input change on most of its i/o pins. For example, you could use an interrupt to check if a user pressed a button. You can, of course, simply check and read any pin in your code to determine if a button is pressed. The advantage of using interrupts is that you do not need to constantly check the pin in your code. This is an advantage particularly if you have delays in your code, where the cannot check the pin. The interrupt happens in the background and is immediate….well actually within four clock cycles. You can calculate how long that is if you want.

For more information on interrupts check [lessons](https://www.google.com/url?q=https://docs.google.com/document/d/1BmZbXzxnD2j17QToSZ9jeZmnP7burwfksfQq2v4zu-Y/edit%23heading%3Dh.ob48nqqcf4xy&sa=D&ust=1587613174390000).

### Challenge

Using only C and no external libraries, design a circuit and program that uses an external interrupt to toggle the value of an LED when a button is pressed. The button should be connected to bit 3 of PortC. You should read the overview of section 13 in your datasheet and the Register Description 13.2

TEACHER CHECK \_\_\_\_

### Challenge

Following the same guidelines given above, modify your circuit and code so that you LED toggles on the falling edge of a button. Note that you will need to use a pin connected to either INT0 or INT1.

TEACHER CHECK \_\_\_\_
