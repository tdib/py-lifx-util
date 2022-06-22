import json
import sys
from lifxlan import Light

# Load devices from json file
# Uses ./devices.json if no second argument is specified
try:
  device_data_file = sys.argv[2] if len(sys.argv) > 2 else './devices.json'
  with open(device_data_file) as f:
    devices = json.load(f)
except FileNotFoundError as e:
  print('The specified device data file could not be found.')
  sys.exit(1)

# Load LIFXLan Light object from extracted data
selected = sys.argv[1]
if not (device_data := devices.get(selected)):
  sys.stderr.write(f'The specified device ({selected}) could not be found.\n')
  sys.exit(1)
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
