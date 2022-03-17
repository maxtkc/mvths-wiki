Modifying Example Code
======================

Overview
--------

One of the purposes of example code is to confirm that a new device works correctly. Once you know that the device works, you may want to make a copy of the example code and modify it to suit your needs. The first step in modifying example code is to try to reduce the example code to its "bare bones". That is just enough code to communicate with the device. The best way to do this is to comment out lines of code one at a time. After commenting out a line, test the code to make sure you did not break anything important. 

Exercise:

#. Open the example code you used in the previous lesson and Save As to make a copy. You can call it anything you want, but it is good to use a name that means something to you such as MCP9808-simple. Make sure you save it in the directory you are using to store all your code files.
#. Comment out as lines of code until you can just see the temperature in Celsius in your terminal window. Make sure to check your code after commenting out each line of code. This way you will know exactly what lines you need and what lines you don't.
#. Continue to comment out lines of code until only what you need to display the temperature remains.

   As reminder, commenting out a line of code only removes it temporarily from you code. You can easily return it to your code by removeing the comments.
   
.. code-block:: C
   
   digitalWrite(5, HIGH); //This line is in your code.
   //digitalWrite(5, HIGH); //This line is commented out of your code. Notice that it is grey.
   
   TEACHER CHECK \_\_\_\_
   
#. Add an LED to your board and modify the code so that the LED goes on when the temperature passes 26.25 degrees Celsius and turns off when the temperature is below 26 degrees. You might need to change this threshold depending on the temperature in the shop.

   TEACHER CHECK \_\_\_\_

#. Find an equation for converting Celsius to Fahrenheit and then use this equation to make the conversion in your code. Display a column of temperature values in Fahrenheit.

   TEACHER CHECK \_\_\_\_
