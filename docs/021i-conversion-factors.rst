Conversion Factors
==============

Overview
--------

In order to convert one range of numbers to another range you need to determine a conversion factor. As an example, a audio sensor might be able to measure the loudness of sound from 0dB to 120dB, but the display that it is connected to might only have ten LED bars to represent loudness. In this case, 0db would correspond to no LED light bars and 120db would correspond to 10 LED bars. In order to make this conversion in software, you would need a conversion factor. This can be accomplished by simply dividing the target range by the source range as shown below::

 conversion factor = target range / source range

Using the example above, the target range is 10 and the source range is 120. The scale factor (10/120) is .0834. Converting a source value to a target value is as simple
as multiplying the target value by the conversion factor::

 source value = target value * conversion factor

Note that if we recorde a value of 120dB, the top of the range for loudness, this converts to 10, the top of the LED range (120 * .0834 = 10). If we record a value of 60 dB, the
middle of the range for loudness, this converts to 5, the middle of LED range (60 * .0834 = 5). 

Exercise:
~~~~~~~~~

Complete the following table in your notebook.

.. list-table:: Conversion Factor
   :widths: 25 25 50
   :header-rows: 1

   * - Source Range
     - Target Range
     - Conversion Factor
   * - 0 to 180
     - 0 to 65
     - 
   * - 0 to 45
     - 0 to 220
     - 
   * - 0 to 100
     - 0 to 10
     - 
 
| **Complex Conversions**
In addition to creating a conversion factor for ranges that begin with zero it is possible to create scales for ranges that do not begin with zero. For example, let’s start with a source range of 10 to 50 and scale to a range of 0 to 90. You can find the scale factor using the same equation you used above, but instead of using the 50 for the initial range, you would use 40 or the difference between the start of the range 10 and the end of therange 50.  Therefore the scale factor equals 90 divided by 40 or 2.25. 

Complete the following table in your notebook.

.. list-table:: Complex Conversions
   :widths: 25 25 50
   :header-rows: 1

   * - Source Range
     - Target Range
     - Conversion Factor
   * - 10 to 180
     - 0 to 65
     - 
   * - 5 to 45
     - 0 to 220
     - 
   * - 40 to 100
     - 0 to 10
     - 

| **Map Function**

It is also possible to use a map function provided in the Arduino library to easily map between two ranges. Below shows how the function interprets the values of each range.

.. code-block::

 map(value, fromLow, fromHigh, toLow, toHigh)

Below is an example of the function mapping the source range (1 to 50) to (50 to 1). The value x from the source range is mapped to the value y in the target range.

.. code-block::

 y = map(x, 1, 50, 50, 1);
