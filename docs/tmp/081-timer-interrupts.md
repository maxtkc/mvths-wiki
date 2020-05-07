# Overview

Timer interrupts can be used to execute code at exact intervals in the background of your code and to create precise waveforms external to your device. The ATMega328 contains three separate timers. Timer0 and Timer2 are 8-bit timers. Timer1 is a 16-bit timer. 8-bit timers can count to a maximum of 255...as should be obvious to anyone who has gotten this far in the guide. You can figure out the maximum count of a 16-bit timer. These timers are not running by default. Using registers you can turn them on, set the frequency of their count with a pre-scaler, and when the call interrupts.

### Challenge

Design a circuit and program that uses [timer0](https://www.google.com/url?q=https://docs.google.com/document/d/1BmZbXzxnD2j17QToSZ9jeZmnP7burwfksfQq2v4zu-Y/edit%23heading%3Dh.fisakateqwa0&sa=D&ust=1587613174393000) to flash an LED at frequency of exactly 31.25kHz. In order to do this, the timer will need to interrupt every time the counter overflows. At every interrupt, it will need to toggle the value of an LED.

You will need to refer to Timer0 Register Description (15.9) in your printed datasheet to complete this challenge.

1.  Determine the correct name of the interrupt service routine for overflow of timer0. You will need to check the list of interrupt service routine names. A link can be found in the section on interrupts in concepts.
2.  Set Timer/Counter Control Register B to that the timer is running but there is no prescaling of the time
3.  Set Timer/Counter Interrupt Mask Register so that Timer0 will call an interrupt every time Timer0 overflows.
4.  Clear the other Timer0 control register (TTCR0A) to ensure that the waveform generation mode (table 15-8) is set to Normal.
5.  Demonstrate the frequency of the flashing LED with an oscilloscope.

TEACHER CHECK \_\_\_

### Challenge

Modify your code so that the LED flashes at a frequency of close to 488 Hz. In order to do this, you will need to change the prescale value for Timer0. Show your calculations below.

TEACHER CHECK \_\_\_\_

### Challenge

Modify your code so that the LED flashes at a frequency of close to 14.8khz. In order to do this, you will need to set the device to interrupt on a compare match with OCR0A. This will involve calculating the correct value for match and setting this value in OCR0A. It will also involve determining the correct interrupt label for Timer0 compare match with OCR0A. You will need to select the correct pre-scale value and set the correct bit for interrupt in TIMSK0. Show your calculations below.

TEACHER CHECK \_\_\_\_
