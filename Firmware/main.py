import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner
from kmk.extensions.rgb import RGB
from kmk.extensions.rgb import AnimationModes

keyboard = KMKKeyboard()

switch_pins = [
    board.GP9,
    board.GP10,
    board.GP11,
    board.GP6,
    board.GP7,
    board.GP8,
]

keyboard.matrix = KeysScanner(
    pins=switch_pins,
    value_when_pressed=False,
    pull=True
)

rgb = RGB(
    pixel_pin=board.GP5,
    num_pixels=2,
    rgb_order=(1, 0, 2),
    animation_mode=AnimationModes.STATIC,
    animation_speed=1,
)
keyboard.extensions.append(rgb)

keyboard.keymap = [
    [
        KC.LCTL(KC.C),
        KC.LCTL(KC.V),
        KC.LCTL(KC.Z),
        KC.LCTL(KC.S),
        KC.ESC,
        KC.SPC
    ]
]

def update_leds():
    rgb.pixels.fill((0,0,0))
    if not keyboard.matrix.pressed_keys[0]:
        rgb.pixels[0] = (0, 255, 0)
    if not keyboard.matrix.pressed_keys[1]:
        rgb.pixels[1] = (0, 0, 255)

keyboard.on_matrix_scan = update_leds

if __name__ == "__main__":
    keyboard.go()
