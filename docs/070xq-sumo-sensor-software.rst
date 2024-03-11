STEP NINE: Sumo Line Software
======================

Overview
--------

In the next three lessons, you will learn about three alternative schemes for controlling your line sensors. One is using the analog port, the second is using a digital port, the third is using an external comparitor. Each method is described below and their pros and cons.

**Analog**: Since this sensor produces an analog signal, you can read the output on any analog port which will provide a reading from 0 to 1023. Reading the value on an analog port provides an easy way to set and adjust the exact threshold for sensing a line. The downside of the using the analog port is that reading values is slow and you can not easily integrate an interrupt. 

**Digital**: This method relies on the internal comparator on each of the digital pins. Since you can not adjust the threshold in software you must rely on setting the correct height to get the results you want. The advantage of this method is that it is fast and can be used with interrupts.

**Comparator**: This is method provides the most accurate results and allows you to adjust easily for changes in ambient light or changes in the surface you are detecting. It also allows you to use interrupts in your code. The downside is that it requires a more complex circuit. 

