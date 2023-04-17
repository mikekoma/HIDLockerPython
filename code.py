#
# 1 Key Keyboard
#
# Circuit Diagram
#  XIAO SAMD21
#
#  +-------SW--------+
#  |  _____________  |
#  +--D0   USB   5V  |
#     D1        GND--+
#     D2        3V3
#     D3        D10
#     D4         D9
#     D5         D8
#     D6_________D7
#
# Circuit Python 8.0.5
# https://circuitpython.org/board/seeeduino_xiao/
#
# Adafruit_CircuitPython_Bundle 20230416
# After extracting the zip, copy lib/adafruit_hid to CIRCUITPY/lib
# https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases
#
# MIT Licence
# Copyright (c) 2023 Suns & Moon Laboratory
# https://opensource.org/licenses/mit-license.php

# Import the libraries
import time
import board
from digitalio import DigitalInOut, Direction, Pull
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import usb_hid

STT_L_KEY_HI = 1
STT_L_KEY_DOWN = 2
STT_L_KEY_LO = 3
STT_L_KEY_UP = 4

class LoKey:
		def __init__(self):
			self.state = STT_L_KEY_HI
		
		def update(self, keybit):
			if self.state == STT_L_KEY_HI:
				if keybit == 0:
					time.sleep(0.01)
					if keybit == 0:
						self.state = STT_L_KEY_DOWN
			elif self.state == STT_L_KEY_DOWN:
				kbd.send(Keycode.SHIFT)
				led.value = False # led on
				self.state = STT_L_KEY_LO
			elif self.state == STT_L_KEY_LO:
				if keybit == 1:
					self.state = STT_L_KEY_UP
			elif self.state == STT_L_KEY_UP:
				kbd.send(Keycode.GUI ,Keycode.L)
				led.value = True # led off
				self.state = STT_L_KEY_HI
			else:
				elifself.state = STT_L_KEY_HI

lokey = LoKey()

# define output LED
led = DigitalInOut(board.LED_INVERTED)
led.direction = Direction.OUTPUT

# led off
led.value = True

# configure device as keyboard
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

io_keysw = DigitalInOut(board.D0)
io_keysw.direction = Direction.INPUT
io_keysw.pull = Pull.UP

# loop forever
while True:
	lokey.update(io_keysw.value)
