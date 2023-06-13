import sys
import json

def extract_device_data():
  # Load devices from json file
  # Uses ./devices.json if no second argument is specified
  try:
    if len(sys.argv) >= 2:
      if sys.argv[-1].endswith('.json'):
        device_data_file = sys.argv[-1]
      else:
        device_data_file = './devices.json'
        
      with open(device_data_file) as f:
        devices = json.load(f)
  except FileNotFoundError as e:
    sys.stderr.write('The specified device data file could not be found.\n')
    sys.exit(1)

  if len(sys.argv) < 2:
    sys.stderr.write('Usage: python3 <script> <device_name> [device_data_file]\n')
    sys.exit(1)

  # Extract LIFX light data from device file
  selected = sys.argv[1].lower()
  if not (device_data := devices.get(selected)):
    sys.stderr.write(f'The specified device ({selected}) could not be found.\n')
    sys.exit(1)

  return device_data