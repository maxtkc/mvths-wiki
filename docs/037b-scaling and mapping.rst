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




produce more precision than the display it u

For example, if you wanted to convert the range of numbers 0 to 10 to the 
range 0 to 20, you would simply multiply the first set by 2. If the first set were represented by the variable x and the second y then if


