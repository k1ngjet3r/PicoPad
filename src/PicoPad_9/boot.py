import board
from kmk.bootcfg import bootcfg

# http://kmkfw.io/docs/boot/
# deactivates bootcfg by holding down left down key
bootcfg(
    sense=board.GP3,  # column
    source=board.GP2, # row
    cdc=True,         # disable com port
    midi=False,       # disable midi device
    mouse=False,      # disable mouse
    storage=True,     # disable usb storage
    usb_id=('PicoPad 9', 'Custom Keypad with 9 buttons'),
)
