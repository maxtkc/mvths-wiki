Conversion Factors
==============

Overview
--------

In order to convert one range of numbers to another range you need to determine a conversion factor. As an example, a audio sensor might be able to measure the loudness of sound from 0dB to 120dB, but the display that it is connected to might only have ten LED bars to represent loudness. In this case, you would want 0db to correspond to no LED light bars and 120db to correspond to 10 LED bars. In order to make this conversion in software, you would need a conversion factor. This can be accomplished by simply dividing the target range by the source range as shown below::

 conversion factor = target range / source range

Using the example above, the target range is 10 and the source range is 120. The scale factor (10/120) is .0834 rounded to the nearest ten thousandth. Converting a source value to a target value is as simple as multiplying the source value by the conversion factor::

 target value = source value * conversion factor
 
For example, if you wanted to know how many bars would be represented by 60dB you would just need to multiply 60dB by .0834 which results in 5.004. Since there are no fractional bars, the display would show 5 or 6 lights depending on how you wrote the code. This also confirms that your conversion factor is correct, since 60dB and 5 are both the middle of the range of each range.

Exercise:
~~~~~~~~~

#. Find the conversion factor for each of the ranges listed below. Round your answer to the nearest 100th. Complete the table in your notebook.

   .. list-table:: 
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

#. Find the converstion factors for the ranges listed below. Round to the nearest hundreth. Note that in the following table, the ranges do not begin with zero as they do in the table above. Finding the conversion factor simply means taking the difference between start and end points in each range. For example, using a source range of 10 to 50 and target to a range of 0 to 90, you would use 40 for the source range and 90 for the target range.  Therefore the scale factor equals 90 divided by 40 or 2.25. 

   .. list-table::
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

#. Use the *map()* function to make a conversion. The map() function provided in the Arduino library allows you to easily map between two ranges. Below shows how the function interprets the values of each range.

   .. code-block:: C

      map(value, fromLow, fromHigh, toLow, toHigh);

   Below is an example of the function mapping the source range (1 to 50) to (50 to 1). The value x from the source range is mapped to the value y in the target range.

   .. code-block:: C

      y = map(x, 1, 50, 50, 1);
