Scaling and Mapping
==============

Overview
--------

Scaling is a simple way of converting one range of numbers to another range. As an example, a audio sensor might be able to measure the loudness of sound from 0dB to 120dB,
but the display that it is connected to might only have ten LED bars to represent loudness. In this case, 0db would correspond to no LED light bars and 120db would 
correspond to 10 LED bars. In order to make this conversion in software, you would need a conversion factor. This can be accomplished by simply 
dividing the target range by the source range as shown below::

 scale factor = target range / source range

Using the example above, the target range is 10 and the source range is 120. The scale factor (10/120) is .0834. Converting a source value to a target value is as simple
as multiplying the target value by the scale factor::

 source value = target value * scale factor

Note that if we recorde a value of 120dB, the top of the range for loudness, this converts to 10, the top of the LED range (120 * .0834 = 10). If we record a value of 60 dB, the
middle of the range for loudness, this converts to 5, the middle of LED range (60 * .0834 = 5). 

Exercise:
~~~~~~~~~

.. list-table:: Ohms Law
   :widths: 25 25 50
   :header-rows: 1

   * - Variable type
     - Lowest value
     - Highest value
   * - byte
     - 
     - 
   * - int
     - 
     - 
   * - unsigned int
     - 
     - 
   * - long
     - 
     - 
   * - unsigned long
     -
     - 



