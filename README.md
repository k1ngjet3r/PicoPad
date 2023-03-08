# PicoPad Macropad

![PicoPad_9](https://user-images.githubusercontent.com/43425262/223685391-7d864d46-0484-43e5-ab71-be16c9c71b6b.jpg)

Firmware for PicoPad-9. To use the code I wrote for the PicoPad, simply download a copy of `code.py` under src/PicoPad_9/ directory and place into the root directory of CIRCUITPY.

## Dependency

1. Install CircuitPython on Raspberry Pi Pico [Guide](https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython)

2. A copy KMK from [KMKfw/kmk_firmware](https://github.com/KMKfw/kmk_firmware/). Mount the board and place the kmk folder in the root directory.

3. In order to use the LED sript, `adafruit_pixelbuf.mpy` and `neopixel.mpy` are required. Both of the files can be obtained from the Adafruit site. [LINK](https://learn.adafruit.com/circuitpython-essentials/circuitpython-neopixel) Both file needs to be placed in the lib folder in the root directory.


## Customization

* Key Configuration:
  * [Keys Overview](http://kmkfw.io/docs/keycodes)
  * [Media Keys](http://kmkfw.io/docs/media_keys)

* RGB light stript:
  * [RGB/Underglow/NeoPixel](http://kmkfw.io/docs/rgb)
  
  
## 3D Model:
  * [Printable](https://www.printables.com/model/417351-picopad-9-macropad)
