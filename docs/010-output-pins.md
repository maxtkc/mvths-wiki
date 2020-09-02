# Output Pins

## Overview

The digital pins on your microcontroller (described above) can be used as either [inputs or outputs](https://www.google.com/url?q=https://docs.google.com/document/d/1BmZbXzxnD2j17QToSZ9jeZmnP7burwfksfQq2v4zu-Y/edit%23heading%3Dh.12g8aset9qzv&sa=D&ust=1587613173860000). As an output, the voltage on the pin can be set to either HIGH (5V) or LOW (0V). A pin set as an output can be used to control an LED, a speaker, a motor or just about any sort of electronic device.

### Exercise:

In this first exercise, you will set one of the pins of your microcontroller as an output pin and then set that pin to HIGH.

1.  Open a new code file (File/New) in your Arduino IDE.

<!-- end list -->

2.  Type the following two lines of code inside your setup [function](https://www.google.com/url?q=https://docs.google.com/document/d/1BmZbXzxnD2j17QToSZ9jeZmnP7burwfksfQq2v4zu-Y/edit%23heading%3Dh.45j551ci2de&sa=D&ust=1587613173861000). The first line sets pin 8 on your microcontroller as an output pin. The second line sets the value of pin 8 to HIGH.

pinMode(8, OUTPUT);

digitalWrite(8, HIGH);

        

3.  Compile and download your code. If you have errors, ask your teacher for help.

<!-- end list -->

4.  Use a multimeter to confirm that the voltage on pin 8 is 5V (or close to 5V). Connect the black lead to ground on your circuit and touch the red lead to pin 8 on your Metro Mini.

TEACHER CHECK \_\_\_\_\_

5.  Modify your code to set pin 8 to 0V (LOW).

<!-- end list -->

6.  Program your microcontroller and confirm with a multimeter.

TEACHER CHECK \_\_\_\_\_

7.  Modify your code to set pin 6 to 5V. Program and confirm with your multimeter.

TEACHER CHECK \_\_\_\_\_
