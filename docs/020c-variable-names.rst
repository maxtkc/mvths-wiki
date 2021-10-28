Variable Names
==============================

Overview
--------

There are many conventions for naming your variables, but the most important one is using a name that means something in your code. For example, if you are counting button presses
then the following might be appropriate.

.. code-block:: C
  
    int btnPresses;  //Count the number of times the button is pressed
    
It might be tempting to shorting the name to something like the following.

.. code-block:: C

  int btnPress;//Count the number of times the button is pressed

This though becomes less readable when you use the variable in your code as seen below.

.. code-block:: C

  if (btnPresses == 5) {
    //do something
    }

  if (btnPress == 5) {
    //do something
    }
    
In the first example, it is clear to anyone reading the code that you are counting the number of times a button was pressed. In the second example, someone reading the code might guess you were checking if the fifth button was pressed.

It is acceptable and often recommended to use multiple words in a variable name if it makes it more clear. The only important convention is that you separate the words with either capitalization, hypens or underscores. 
