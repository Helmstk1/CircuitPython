# Write your code here :-)
import board
import neopixel
import pulseio
import time

# from digitalio import DigitalInOut, Direction, Pull

dot = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.1)
led = pulseio.PWMOut(board.D13)

print("Make it red!")

red = 0
blue = 85
green = 170


while True:

    red = red + 1
    blue += 1
    green += 1

    if red == 255:
        red = 0
    if blue == 255:
        blue = 0
    if green == 255:
        green = 0

    dot.fill((red, green, blue))
    time.sleep(.1)

    if led.duty_cycle + 655 >= 65535:
        led.duty_cycle = 0

    led.duty_cycle = led.duty_cycle + 655






