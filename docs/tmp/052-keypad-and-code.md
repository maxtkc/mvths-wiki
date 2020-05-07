# Overview

In this lesson you will you use your knowledge of keypads and arrays to make keypad security software.

### Exercise:

Write a program to read and display key presses on the serial monitor.

NOTE: It is important that you setup your array as a char. For example:

#### char nameofarray\[3\];

TEACHER CHECK \_\_\_\_

### Exercise:

Write a program to read each key press and store the key that was pressed into an array. The first key pressed should be stored in the 0 index of the array and the second key pressed should be stored in the 1 index of the array and so on for a total of five key presses.

After five keys are pressed it should display all of the elements of the array. (see your code from above for displaying elements of an array)

TEACHER CHECK \_\_\_\_

### Exercise:

Modify your code from above to display the count of the key presses in addition i.e. after one key is pressed it should display one and so on.

TEACHER CHECK \_\_\_\_

### Exercise:

Modify your code from above so that it stops after the user presses the button five times and displays “Done.”

TEACHER CHECK \_\_\_\_

### Challenge:

Modify your code so that it compares the five keys the user presses with five keys stored in an array. If the each of the five keys pressed matches each of the five keys stored in the array, in the correct order, display “Open” otherwise display “Error”.

TEACHER CHECK \_\_\_\_

IR REMOTE CONTROL

# Overview

Infrared remotes are commonly used to control consumer audio and video devices. They can also be used for cameras and household appliances such as air conditioners. Unlike the previous user interface devices you have learned about, remotes are not physically connected to the device they are controlling. In the case of IR remotes they communicate with the device by using a signal composed of infrared light.

![](images/image5.png)

## IR Circuit

In order to convert the infrared light signal into a digital voltage signal that your MCU can read you will need to use an IR receiver.

![](images/image116.png)

### Exercise

The IR receiver you are going to use is V39338 made by Vishay and will be provided by your teacher. There are many versions of IR receivers and most work similarly to this device though may have a different order of pins.

1.  Using the diagram below (IMPORTANT) connect the power and ground pins of the device.
2.  Connect the signal pin to your oscilloscope and record the default value of the signal pin.

                Default voltage level: \_\_\_\_\_\_\_\_\_\_\_

3.  Press a button your IR remote and note if there is any change on your scope.
4.  Adjust your scope settings so that you can see pulses when you press a button on your IR remote. If you are having trouble seeing the signal set the time/div dial to 5ms.

![](images/image65.png)

## Decoding IR Signals

The signals produced by IR remotes are fairly complex but not impossible to decode with the use of your oscilloscope. Each remote corresponds to a specific transmission protocol such as NEC, Sony SIRC and Philips RC5. The remote used in this project uses the NEC protocol.  

The signal is made up of four components: a start pulse, a space, an address (16-bit), and a command (16-bit). Within the address and command parts of the signal a zero is represented as a short low pulse and a one is represented as a long low pulse.

![](images/image113.png)

### Exercise

Using your oscilloscope make the following measurements. Make sure to include the correct units.

Start =         \_\_\_\_\_\_\_\_\_\_

Space =         \_\_\_\_\_\_\_\_\_\_

Zero =                \_\_\_\_\_\_\_\_\_\_

One =                 \_\_\_\_\_\_\_\_\_\_

1\. TEACHER CHECK \_\_\_\_

## IR Remote Code

Follow the steps provided below to install and use the example IRrecvDemo code. Using this code your microcontroller can capture the signal from your IR receiver, convert the pulses into numbers and print these numbers on your serial monitor.

### Exercise:

1.  Open the IRrecvDemo code which should be be found in your Examples/IRremote. The IRremote directory should be found at the bottom of the examples menu under Examples from Custom Libraries. If you cannot find this directory you must install it using the manager libraries option. The file you want to install is called IRremote by Shirriff.
2.  Connect the signal pin of your IR receiver to the correct pin on your microcontroller. This pin number is listed at the top of the IRrecvDemo code. Note: You cannot use another pin with this code.
3.  Download the code and use your remote to display values in the Serial Monitor. Note that these values are displayed in hex.
4.  Write down the hex values for the following buttons.

|               |           |
| ------------- | --------- |
| Button Press  | Hex Value |
| 1             |           |
| 2             |           |
| 3             |           |
| “right arrow” |           |
| VOL-          |           |

2\. TEACHER CHECK \_\_\_\_

## Hex Values

Using your scope decode the signal for button 1 and confirm that this matches the decoded signal provided by the code.

### Exercise:

1.  Capture the signal for button 1 on your oscilloscope.
2.  Record both the 16-bit address and 16-bit command in the top row of boxes provided below. Make sure to correctly identify which pulses are ones and which pulses are zeros.
3.  Convert the value in binary to a value in hex and place the hex value in bottom row of boxes.

![](images/image3.png)

4.  Compare the hex value you measured on the scope with the hex value you received in your serial monitor.

                Value from oscilloscope:         \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

                Value from Serial Monitor:        \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

3\. TEACHER CHECK \_\_\_\_

## Remote Control

Using what you have learned so far you can now use your remote control to control any device on your breadboard.

### Exercise

Add an LED to your breadboard and modify your code so that when a user presses the button 1 the LED turns on and when the user press the button 2 the LED turns off.

4\. TEACHER CHECK \_\_\_\_
