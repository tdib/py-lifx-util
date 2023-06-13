from lifxlan import Light
from util import extract_device_data
import sys

# Extract light data and convert into LIFXLan Light object
device_data = extract_device_data()
device = Light(device_data['mac'], device_data['ip'])

# Default
percentage_change = 0.1

# Toggle light, attempting 5 times before exiting
attempts = 0
while attempts < 5:
  try:
    hsbk = list(device.get_color())

    device.set_color([1, 65535, 65535, 2500])


    # if device.get_power() != 0:
    #   device.set_power(False)
    # else:
    #   device.set_power(True)

    break
  except:
    attempts += 1
    print("Attempt", attempts, "failed")
