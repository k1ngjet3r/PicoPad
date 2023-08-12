"""
    PicoPad-9

    Created by Gabbajoe

    To enable RGB function using KMK, adafruit_pixelbuf.mpy and neopixel.mpy were required to place in the lib folder.
    Both files can be download from https://learn.adafruit.com/circuitpython-essentials/circuitpython-neopixel. 
    Here multi layer example
"""

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers as _Layers
from kmk.extensions.rgb import RGB, AnimationModes
from kmk.handlers.sequences import simple_key_sequence, send_string
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.rgb import RGB, AnimationModes


keyboard = KMKKeyboard()

# GPIO_CONFIG
# key pins
KEY_COL_PINS = (board.GP3, board.GP4, board.GP5,)
KEY_ROW_PINS = (board.GP0, board.GP1, board.GP2,)
# encoder pins 
ENCODER_OUT_A = board.GP28
ENCODER_OUT_B = board.GP27
ENCODER_SWITCH = board.GP26
# led rgb pins
WS2812_PIN = board.GP22
WS2812_LED_COUNT = 3

# key config
keyboard.col_pins = KEY_COL_PINS
keyboard.row_pins = KEY_ROW_PINS
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# led setup
rgb = RGB(
    pixel_pin=WS2812_PIN,
    num_pixels=WS2812_LED_COUNT,
    rgb_order=(1, 0, 2),  # GRB WS2812
    animation_mode=AnimationModes.STATIC,
    hue_default=138,
    sat_default=255,
    val_default=200,
    )

keyboard.extensions.append(rgb)

# add led color change on layer change
class Layers(_Layers):
    last_top_layer = 0
    # blue, yellow, green, red
    hues = (138, 20, 69, 4)
    
    def after_hid_send(self, keyboard):
        if keyboard.active_layers[0] != self.last_top_layer:
            self.last_top_layer = keyboard.active_layers[0]
            rgb.set_hsv_fill(self.hues[self.last_top_layer], 255, 200)

#combo layer while holding mod 1 & 2 switch to layer 3
combo_layers = {
  (1, 2): 3,
}

my_layer = Layers(combo_layers)

keyboard.modules.append(my_layer)
keyboard.extensions.append(MediaKeys())

# key mapping
# launching Spotify
num_1 = simple_key_sequence([
        KC.LCTRL(KC.ESCAPE),
        KC.MACRO_SLEEP_MS(100),
        send_string('spotify'), 
        KC.ENTER 
        ])

num_2 = KC.MEDIA_PREV_TRACK
num_3 = KC.MPLY
num_4 = KC.MEDIA_NEXT_TRACK

# format document keycombo in VSCode
num_5 = simple_key_sequence([
        KC.LSHIFT(KC.LALT(KC.F)),
        ])

# launching VSCode
num_6 = simple_key_sequence([
        KC.LCTRL(KC.ESCAPE),
        KC.MACRO_SLEEP_MS(100),
        send_string('visual studio code'), 
        KC.ENTER 
        ])

# launching terminal
num_7 = simple_key_sequence([
        KC.LCTRL(KC.ESCAPE),
        KC.MACRO_SLEEP_MS(100),
        send_string('putty'), 
        KC.ENTER 
        ])

zoom_in = KC.LCTRL(KC.EQUAL)
zoom_out = KC.LCTRL(KC.MINUS)
zoom_rest = KC.LCTRL(KC.N0)

keyboard.keymap = [
    [ #Default
    num_5, num_6, num_7,
    num_2, num_3, num_4,
    KC.MO(1), num_1, KC.MO(2),
    ],
    [ #Layer 1
    KC.N1,    KC.N2, KC.N3,
    KC.N4,    KC.N5, KC.N6,
    KC.MO(1), KC.N7, KC.MO(2),
    ],
    [ #Layer 2
    KC.EXLM,  KC.AT,   KC.HASH,
    KC.DLR,   KC.PERC, KC.CIRC,
    KC.MO(1), KC.AMPR, KC.MO(2),
    ],
    [ #Layer 3
    KC.F1,    KC.F2, KC.F3,
    KC.F4,    KC.F5, KC.F6,
    KC.MO(1), KC.F7, KC.MO(2)
    ]
]

# Encoder setup
encoders = EncoderHandler()
OUT_A = ENCODER_OUT_A
OUT_B = ENCODER_OUT_B
SWITCH = ENCODER_SWITCH
encoders.pins = ((OUT_A, OUT_B, SWITCH),)

keyboard.modules = [my_layer, encoders]

encoders.map = [
    ((KC.VOLU, KC.VOLD, KC.MUTE),), # default
    ((zoom_out, zoom_in, zoom_rest),), # Layer 1
    ((KC.PGUP, KC.PGDOWN, KC.NO),), # Layer 2
    ((KC.VOLU, KC.VOLD, KC.MUTE),), # Layer 3
]

if __name__ == '__main__':
    keyboard.go()
