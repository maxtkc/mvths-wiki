# Modifying Example Code

## Overview

The purpose of example code is mostly to confirm that a new device works correctly. Once you know that the device works it is best to make a copy of the example code and modify it to suit your needs. In this lesson we will use the example code from the previous lesson a our model.

Exercise:

1.  Make a copy of the example file (MCP9808)  used above using Save As… I recommend calling it MCP9808-simple or something like this. You will make this conversion for lots of example code files and you need to use the “simple” version of the files often so it is good to save them in way that you can easily find them. Make sure you save it in the directory you are using to store all your code files.
2.  Modify the code so that it only displays the temperature in Celsius. In order to do this efficiently, you should need to [comment out](https://www.google.com/url?q=https://docs.google.com/document/d/1BmZbXzxnD2j17QToSZ9jeZmnP7burwfksfQq2v4zu-Y/edit%23heading%3Dh.yx113392uaik&sa=D&ust=1587613173973000) the lines of code you do not need.
3.  Make sure you remove ALL the code you do not need. Continue to cut code till it breaks, than comment the necessary code back into the file. If you do this carefully, you will be left with only the essential code for the required application.
4.  Add an LED to your board and modify the code so that the LED goes on when the temperature passes 26.25 degrees Celsius and turns off when the temperature is below 26 degrees. You might need to change this threshold depending on the temperature in the shop.

TEACHER CHECK \_\_\_\_

5.  Find an equation for converting Celsius to Fahrenheit and then use this equation to make the conversion in your code. Display a column of temperature values in Fahrenheit.

TEACHER CHECK \_\_\_\_
