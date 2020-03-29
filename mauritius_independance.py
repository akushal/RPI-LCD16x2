#!/usr/bin/python
# Example using a character LCD connected to a Raspberry Pi or BeagleBone Black.
import time

import Adafruit_CharLCD as LCD


from gpiozero import LED, PWMLED
from time import sleep

red = LED(12)
blue = PWMLED(16)
yellow = LED(20)
green = PWMLED(21)
green.value =  0.0
blue.value = 0.0

def off():
    red.off()
    blue.off()
    yellow.off()
    green.off()
    lcd.set_backlight(0)

def on():
    red.on()
    blue.value = 0.1
    yellow.on()
    green.value = 0.1
    lcd.set_backlight(1)

def flash():
    print("Flashing....")
    for i in range(4):
        off()
        sleep(0.5)
        on()
        sleep(1)
        off()



# Raspberry Pi pin configuration:
lcd_rs        = 25  # Note this might need to be changed to 21 for older revision Pi's.
lcd_en        = 24
lcd_d4        = 23
lcd_d5        = 17
lcd_d6        = 18
lcd_d7        = 22
lcd_backlight = 2

# BeagleBone Black configuration:
# lcd_rs        = 'P8_8'
# lcd_en        = 'P8_10'
# lcd_d4        = 'P8_18'
# lcd_d5        = 'P8_16'
# lcd_d6        = 'P8_14'
# lcd_d7        = 'P8_12'
# lcd_backlight = 'P8_7'

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Alternatively specify a 20x4 LCD.
# lcd_columns = 20
# lcd_rows    = 4

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           lcd_columns, lcd_rows, lcd_backlight)

lcd.set_backlight(1)
red.on()
# Print a two line message
lcd.message('Hello!')

# Wait 5 seconds
time.sleep(2.0)

#lcd.blink(True)
blue.value = 0.1
# Demo scrolling message right/left.
lcd.clear()
message ='M O R I S'
lcd.message(message)
time.sleep(2.0)
yellow.on()
for i in range(lcd_columns-len(message)):
    time.sleep(0.5)
    lcd.move_right()
for i in range(lcd_columns-len(message)):
    time.sleep(0.5)
    lcd.move_left()
green.value = 0.1
lcd.clear()
message ='Zwayer Lindependance'
lcd.message(message)
for i in range(len(message)):
    time.sleep(0.5)
    lcd.move_left()



# Turn backlight off.
#lcd.set_backlight(0)
time.sleep(2.0)
# Change message.
lcd.clear()
lcd.message('  51  ANS   ')
for i in range(len(message)):
   time.sleep(0.5)
   flash()
   lcd.move_right()
#Turn backlight on.
lcd.set_backlight(1)
#lcd.clear()
