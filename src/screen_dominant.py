from PIL import ImageGrab
import numpy as np
from lifxlan import Light
import colorsys
from time import sleep
import ctypes
import scipy.cluster
from util import extract_device_data

SCREEN_WIDTH = ctypes.windll.user32.GetSystemMetrics(0)
SCREEN_HEIGHT = ctypes.windll.user32.GetSystemMetrics(1)
SCALE_FACTOR = 25
INTERVAL = 0.05
DURATION_MS = 200
DEFAULT_KELVIN = 5000
MAX_VALUE = 65535
NUM_CLUSTERS = 8


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
        img = img.resize((SCREEN_WIDTH//SCALE_FACTOR, SCREEN_HEIGHT//SCALE_FACTOR))
        img_arr = np.asarray(img)
        shape = img_arr.shape
        img_arr = img_arr.reshape(np.product(shape[:-1]), shape[-1]).astype(float)

        codes, _ = scipy.cluster.vq.kmeans2(img_arr, NUM_CLUSTERS, minit='points', seed=42)

        # Convert RGB to HSV
        img_hsv = list(colorsys.rgb_to_hsv(*codes[0]))
        hue = img_hsv[0] * MAX_VALUE
        saturation = img_hsv[1] * MAX_VALUE
        brightness = img_hsv[2]/255 * MAX_VALUE

        # Convert HSV to HSBK (for LIFX compatibility)
        if img_hsv[2] < 50 and img_hsv[2] > 25:
            img_hsv[2] /= 2
        elif img_hsv[2] < 25:
            img_hsv[2] = 0 

        if brightness < MAX_VALUE*0.1:
            brightness /= 2
        light_col = (hue, saturation, brightness, DEFAULT_KELVIN)

        # Set light to be colour
        device.set_color(light_col, duration=DURATION_MS, rapid=True)
        sleep(INTERVAL)

except KeyboardInterrupt:
    # Set light to original status
    device.set_power(og_power)
    device.set_color(og_colour)