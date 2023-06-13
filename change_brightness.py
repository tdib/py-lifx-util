from lifxlan import Light
from util import extract_device_data
import sys

# Extract light data and convert into LIFXLan Light object
device_data = extract_device_data()
device = Light(device_data['mac'], device_data['ip'])

if len(sys.argv) < 3:
  sys.stderr.write('Usage: python3 change_brightness.py <increase/decrease>\n')
  sys.exit(1)

if sys.argv[2] == 'increase':
  increase = True
elif sys.argv[2] == 'decrease':
  increase = False

# Default
percentage_change = 0.1
increment_value = percentage_change * 65535

# Toggle light, attempting 5 times before exiting
attempts = 0
while attempts < 5:
  try:
    curr_hsbk = list(device.get_color())
    new_hsbk = list(curr_hsbk)
    if increase:
      # Cap the brightness at 100%
      new_hsbk[2] = min(curr_hsbk[2] + increment_value, 65535)
    else:
      # Cap the brightness at 100%
      new_hsbk[2] = max(curr_hsbk[2]- increment_value, 0)
    device.set_color(new_hsbk, 150)
    break
  except:
    attempts += 1
    print("Attempt", attempts, "failed")
