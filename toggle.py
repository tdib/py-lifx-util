from lifxlan import Light
from util import extract_device_data

# Extract light data and convert into LIFXLan Light object
device_data = extract_device_data()
device = Light(device_data['mac'], device_data['ip'])

# Toggle light, attempting 5 times before exiting
attempts = 0
while attempts < 5:
  try:
    if device.get_power() == 0:
      device.set_power(1)
    elif device.get_power() != 0:
      device.set_power(0)
    # Device is at 0 brightness but not "off"
    elif device.get_color()[2] == 0:
      device.set_color((0, 0, 20000, 4000))
    break
  except:
    attempts += 1
    print("Attempt", attempts, "failed")
