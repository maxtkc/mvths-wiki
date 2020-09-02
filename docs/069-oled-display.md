# Oled Display

## Overview

OLED displays provide excellent contrast for small screens. The do not require much power but are a bit more complicated to use than other displays.

### Exercise:

Turn off the power to your circuit and connect the OLED as follows.

  - GND goes to ground
  - Vin goes to 5V
  - DATA to digital 9
  - CLK to digital 10
  - D/C to digital 11
  - RST to digital 13
  - CS to digital 12

 TEACHER CHECK \_\_\_\_

### Exercise:

Install the Arduino SSD1306 library. Enter and download the following sample code.

\#include \<SPI.h\>

\#include \<Wire.h\>

\#include \<Adafruit\_GFX.h\>

\#include \<Adafruit\_SSD1306.h\>

\#define OLED\_MOSI   9

\#define OLED\_CLK   10

\#define OLED\_DC    11

\#define OLED\_CS    12

\#define OLED\_RESET 13

Adafruit\_SSD1306 display(OLED\_MOSI, OLED\_CLK, OLED\_DC, OLED\_RESET, OLED\_CS);

void setup()   {

  display.begin(SSD1306\_SWITCHCAPVCC);

  display.clearDisplay();

  display.setTextSize(1);

  display.setTextColor(WHITE);

  display.setCursor(0, 0);

  display.println("Hello, world\!");

  display.display();

}

 TEACHER CHECK \_\_\_\_

### Exercise:

Modify your code to display your name on the OLED screen in a larger font.

 TEACHER CHECK \_\_\_\_

### Exercise:

Program your device using the sample code ssd1306\_128x64\_spi. This will provide an example of what sort of graphics are possible with the OLED screen.
