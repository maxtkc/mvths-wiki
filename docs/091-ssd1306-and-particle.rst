Ssd1306 And Particle
====================

YOU MUST CONNECT MOSI (DATA) and CLK

| // use hardware SPI
| // OLED\_D0 -> A3 (SPI CLK)
| // OLED\_D1 -> A5 (SPI MOSI)
| #define OLED\_DC     D3
| #define OLED\_CS     D4
| #define OLED\_RESET  D5

You must remove this function

| int random(int maxRand) {
|    return rand() % maxRand;
| }
