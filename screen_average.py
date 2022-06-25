from PIL import ImageGrab
import numpy as np
from lifxlan import Light
import colorsys
from time import sleep
import ctypes
from util import extract_device_data

# Size of primary monitor
SCREEN_WIDTH = ctypes.windll.user32.GetSystemMetrics(0)
SCREEN_HEIGHT = ctypes.windll.user32.GetSystemMetrics(1)
# HSBK maximum value
MAX_VALUE = 65535
# Behaviour configuration
SCALE_FACTOR = 50
INTERVAL = 0.05
DURATION_MS = 70
DEFAULT_KELVIN = 5000

# Extract light data and convert into LIFXLan Light object
device_data = extract_device_data()
device = Light(device_data['mac'], device_data['ip'])

# Get original power and colour of light
og_power = device.get_power()
og_colour = device.get_color()

try:
    # Toggle power if it is off
    if og_power == 0:
        device.set_power(1)

    while True:
        # Capture screenshot of screen
        img = ImageGrab.grab()
        # Resize image to be small for faster processing
        img = img.resize((SCREEN_WIDTH//SCALE_FACTOR, SCREEN_HEIGHT//SCALE_FACTOR))
        # Convert to numpy array and calculate averages for each colour channel
        img_mean = np.array(img).mean(axis=0).mean(axis=0).astype('uint8')

        # Convert RGB to HSV
        img_hsv = colorsys.rgb_to_hsv(*img_mean)
        img_hsv = np.multiply(img_hsv, MAX_VALUE)
        img_hsv[2] /= 255 if img_hsv[2] >= MAX_VALUE*0.1 else 255*2

        # Set light to be colour
        light_col = (*img_hsv, DEFAULT_KELVIN)
        device.set_color(light_col, duration=DURATION_MS, rapid=True)
        sleep(INTERVAL)

except KeyboardInterrupt:
    # Set light to original status
    device.set_power(og_power)
    device.set_color(og_colour)