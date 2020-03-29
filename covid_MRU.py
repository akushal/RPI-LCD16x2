#!/usr/bin/python
# Example using a character LCD connected to a Raspberry Pi or BeagleBone Black.
import time
import requests
import Adafruit_CharLCD as LCD


from gpiozero import LED, PWMLED
from time import sleep

#Get Data from API for covid on MRU
response = requests.get("https://coronavirus-tracker-api.herokuapp.com/v2/locations?country_code=MU")
#Convert Output to json
outputjson = response.json()
#print (outputjson)

print ("Confirmed cases : " + str(outputjson['latest']['confirmed']))
print ("Death: " + str(outputjson['latest']['deaths']))
print ("Recovered: " + str(outputjson['latest']['recovered']))
# Raspberry Pi pin configuration:
lcd_rs        = 25  # Note this might need to be changed to 21 for older revision Pi's.
lcd_en        = 24
lcd_d4        = 23
lcd_d5        = 17
lcd_d6        = 18
lcd_d7        = 22
lcd_backlight = 2

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

# Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           lcd_columns, lcd_rows, lcd_backlight)

lcd.clear()
lcd.message(" Hello Moris, ")
time.sleep(4)
lcd.clear()

confirmed = "Confirmed Cases: " \
        "\n       " + str(outputjson['latest']['confirmed']) 


lcd.set_backlight(1)
lcd.message(confirmed) 

time.sleep(4)

lcd.clear()

recovered = "Recovered Cases: " + "\n       " + str(outputjson['latest']['recovered'])

lcd.message(recovered)

time.sleep(4)

death = "Deaths: \n       " + str(outputjson['latest']['deaths'])

lcd.clear()

lcd.message(death)

time.sleep(3)

lcd.clear()

lcd.message("#StayHome")

time.sleep(4)

lcd.set_backlight(0)
lcd.clear()
