# Lcd Display Control

## Overview

In order to make the best use of your LCD display, it is important to know how to format text and ensure that the display is easily visible.

# Backlight

The LCD includes a backlight that makes it more visible in high light conditions. The trade off is that the backlight uses more power. Intelligent displays use a light sensor to turn on the backlight in high light conditions and off when the viewing environment is dark. The following is the command for turning the backlight on.

lcd.setBacklight(HIGH);

### Exercise:

Write a program that turns the backlight on and off every second on your LCD screen.

# LCD Cursor

The LCD cursor sets the location of the where any subsequent text command will print. As shown below the command takes two arguments.  The first argument sets the column of the screen. The first column is set to 0. The second argument sets the row of the screen, either 0 for the top row or 1 for the bottom row. The following command would set the cursor on the second row at the 6th column,

lcd.setCursor(6, 1);

### Exercise:

Write a program that prints your name on the second row and starting on the 3rd column.

 TEACHER CHECK \_\_\_\_

### Exercise:

Write a program that writes the word “Pies: “ on the first column and then after this word counts up from zero. You will need to create a variable and then increment that variable in a loop. You will also need to include a delay so the screen has time to update before printing each character.

 TEACHER CHECK \_\_\_\_

# LCD Clear

The following command will allow you to clear the entire LCD screen. This is particularly necessary when you have character overwrite.

lcd.clear();

## LCD Character Overwrite

Each time a character is printed to the screen it remains until it is overwritten. This may lead to unexpected results.

### Exercise:

Test the following code in your setup function.

lcd.setCursor(0, 0);

lcd.print("Watermelon");

lcd.setCursor(0, 0);

lcd.print("kiwi");

Notice that the word “kiwi” was printed over the word “watermelon” but “watermelon” was not erased.

Modify this code using a clear function so that the the word “watermelon” is erased before the word “kiwi’ is printed.

 TEACHER CHECK \_\_\_\_

### Exercise:

Write a program that prints the word “kiwi: “ and then prints a variable starting at 0 and counting up. Make sure to include a delay so that the LCD has time to update before printing each character.

 TEACHER CHECK \_\_\_\_

### Exercise:

Repeat the exercise above but initialize your variable as an uint8\_t (See variable types for more information). This will ensure that the variable only counts up to 255 before resetting to zero. Note that after the variable resets, the ‘55’ left from the ‘255’ remains.

 TEACHER CHECK \_\_\_\_

### Exercise:

Using the LCD clear function modify your code so that the trailing numbers do not appear after the variable resets to zero.

 TEACHER CHECK \_\_\_\_
