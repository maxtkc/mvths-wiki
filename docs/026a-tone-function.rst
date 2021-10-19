Tone Function
-------------

The tone function provides an easy way to send notes to a piezo speaker.
The tone function can be used to set which pin will produce the tone,
the frequency of the tone and duration of the tone. The last argument,
duration is optional.

tone(pin, frequency, duration);
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In addition, there is a notone function that can be used to produce no
sound. This function can be useful because sometimes even sending a
frequency of 0 will result in the processor making some sound.

        tone (pin);
~~~~~~~~~~~~~~~~~~~

Exercise:
~~~~~~~~~

Write a program to play a A4 (440Hz) for exactly half a second.

TEACHER CHECK \_\_\_\_

Exercise:
~~~~~~~~~

Search on the Internet to find software for the Arduino that can play a
popular song or theme using a piezo speaker. Download the software and
play the song for your teacher.

TEACHER CHECK \_\_\_\_
