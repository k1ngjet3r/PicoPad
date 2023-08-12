"""
    PicoPad-9

    Created by K1NGJET3R

    To enable RGB function using KMK, adafruit_pixelbuf.mpy and neopixel.mpy were required to place in the lib folder.
    Both files can be download from https://learn.adafruit.com/circuitpython-essentials/circuitpython-neopixel. 
"""

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.handlers.sequences import simple_key_sequence, send_string
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.rgb import RGB, AnimationModes


# GPIO_CONFIG
# key pins
KEY_COL_PINS = (board.GP0, board.GP1, board.GP2,)
KEY_ROW_PINS = (board.GP3, board.GP4, board.GP5,)

# encoder pins 
ENCODER_OUT_A = board.GP27
ENCODER_OUT_B = board.GP26
ENCODER_SWITCH = board.GP28

# rgb pins
WS2812_PIN = board.GP22
WS2812_LED_COUNT = 3


keyboard = KMKKeyboard()
keyboard.extensions.append(MediaKeys())


# key config & mapping
keyboard.col_pins = KEY_COL_PINS
keyboard.row_pins = KEY_ROW_PINS
keyboard.diode_orientation = DiodeOrientation.COL2ROW

num_1 = KC.MEDIA_PREV_TRACK
num_2 = KC.MPLY
num_3 = KC.MEDIA_NEXT_TRACK

num_4 = KC.BRIGHTNESS_DOWN

# launching Spotify
num_5 = simple_key_sequence([
        KC.LCTRL(KC.SPACE),
        KC.MACRO_SLEEP_MS(100),
        send_string('spotify'), 
        KC.ENTER 
        ])

num_6 = KC.BRIGHTNESS_UP

# for using peek definition function in VSCode
num_7 = simple_key_sequence([
        KC.LALT(KC.F12),
        ])

# Launching VSCode
num_8 = simple_key_sequence([
        KC.LCTRL(KC.SPACE),
        KC.MACRO_SLEEP_MS(100),
        send_string('visual studio code'), 
        KC.ENTER 
        ])

# Launching iTerm
num_9 = simple_key_sequence([
        KC.LCTRL(KC.SPACE),
        KC.MACRO_SLEEP_MS(100),
        send_string('iTerm'), 
        KC.ENTER 
        ])

keyboard.keymap = [
    [
    num_7, num_8, num_9,
    num_4, num_5, num_6,
    num_1, num_2, num_3,
    ]
]


# Encoder setup
encoders = EncoderHandler()
OUT_A = ENCODER_OUT_A
OUT_B = ENCODER_OUT_B
SWITCH = ENCODER_SWITCH
encoders.pins = ((OUT_A, OUT_B, SWITCH),)

keyboard.modules = [encoders]

encoders.map = [((KC.VOLU, KC.VOLD, KC.MUTE),)]


# setup for ws2812 led strip
rgb_ext = RGB(
        pixel_pin=WS2812_PIN,
        num_pixels=WS2812_LED_COUNT,
        rgb_order=(1, 0, 2),  # GRB WS2812
        animation_speed=1,
        animation_mode=AnimationModes.RAINBOW,
        refresh_rate=60,
        )

keyboard.extensions.append(rgb_ext)


if __name__ == '__main__':
    keyboard.go()
