from lifxlan import Light
import sys
from util import extract_device_data

# Extract light data and convert into LIFXLan Light object
device_data = extract_device_data()
device = Light(device_data['mac'], device_data['ip'])

if len(sys.argv) < 5:
    sys.stderr.write('Usage: python3 <script> <device_name> <brightness 0-100> <temp 0-9000> <hue 0-65535> [device_data_file]\n')
    sys.exit(1)

# value between 0 and 100
brightness = int(sys.argv[2])
# value between 0 and 9000
temp = int(sys.argv[3])
# value between 0 and 65535
hue = int(sys.argv[4])

if hue != 0:
    sat = 65535
else:
    sat = 0

if brightness > 0 and brightness < 100:
    brightness = brightness * 655.35
elif brightness >= 100:
    brightness = 65535
elif brightness <= 0:
    brightness = 0

if hue <= 65535 or hue >= 0:
    device.set_color((hue, sat, brightness, temp), 250, rapid=True)
elif hue > 65535 or hue < 0:
    device.set_color((1, sat, brightness, temp), 250, rapid=True)

if device.get_power() == 0:
    device.set_power(1, rapid=True)
