Modifying Example Code
======================

Overview
--------

The purpose of example code is mostly to confirm that a new device works correctly. Once you know that the device works it is best to make a copy
of the example code and modify it to suit your needs. The first step is to remove as much code as possible, until you have reduced it to "bare bones."
This will help you better understand the code and how modify it for your needs. In this lesson we will use the example code from the previous lesson a our model.

Exercise:

1. Using Save As to make a copy of the example file mcp9808test file used in the previous lesson.You can call it anything you want, 
   but it is good to use a name that means something to you such as MCP9808-simple. Make sure you save it in
   the directory you are using to store all your code files.
2. Modify the code so that it only displays the temperature in Celsius. This process can take some time, and some trial and error. The first step is to
   remove one small section of code that you don't think you need and then test the code to see if it works. If it does, repeat this step with 
   another line of code and test. The best way to remove sections of code is NOT to delete, but to comment out the code. Commenting out code does 
   not remove the code from your file, but makes temporarily unavailable.
   
.. code-block:: C
   
   digitalWrite(5, HIGH); //This line is in your code.
   //digitalWrite(5, HIGH); //This line is commented out of your code. Notice that it is grey.

3. Continue to comment out and test your code until you are left with just what you think you need to display just the temperature in a column in 
   your serial monitor window.
   
TEACHER CHECK \_\_\_\_
   
4. Add an LED to your board and modify the code so that the LED goes on
   when the temperature passes 26.25 degrees Celsius and turns off when
   the temperature is below 26 degrees. You might need to change this
   threshold depending on the temperature in the shop.

TEACHER CHECK \_\_\_\_

5. Find an equation for converting Celsius to Fahrenheit and then use
   this equation to make the conversion in your code. Display a column
   of temperature values in Fahrenheit.

TEACHER CHECK \_\_\_\_
