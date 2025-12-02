import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner
from kmk.extensions.rgb import RGB
from kmk.extensions.rgb import AnimationModes
from kmk.modules.encoder import EncoderHandler
from digitalio import Pull

keyboard = KMKKeyboard()

# Add encoder module
encoder_handler = EncoderHandler()
keyboard.modules = [encoder_handler]

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

# Configure encoders
# First encoder: Volume control (GPIO 1 and 2)
# Second encoder: Brightness control (GPIO 3 and 4)
encoder_handler.pins = (
    (board.GP1, board.GP2, None, False),  # Volume encoder: pin_a, pin_b, button_pin, is_inverted
    (board.GP3, board.GP4, None, False),  # Brightness encoder
)

# Define encoder key mappings for each layer
encoder_handler.map = [
    (  # Layer 0 (base layer)
        (KC.VOLU, KC.VOLD),   # Volume encoder: clockwise = volume up, counter-clockwise = volume down
        (KC.BRIU, KC.BRID),   # Brightness encoder: clockwise = brightness up, counter-clockwise = brightness down
    ),
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