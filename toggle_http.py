import requests
import json
import sys
import os
from dotenv import load_dotenv

# Load devices from json file
# Uses ./devices.json if no second argument is specified
try:
  device_data_file = sys.argv[2] if len(sys.argv) > 2 else './devices.json'
  with open(device_data_file) as f:
    devices = json.load(f)
except FileNotFoundError as e:
  print('The specified device data file could not be found.')
  sys.exit(1)

# Load formatted mac address/light selector from extracted data
selected = sys.argv[1].lower()
if not (device_data := devices.get(selected)):
  sys.stderr.write(f'The specified device ({selected}) could not be found.\n')
  sys.exit(1)
device_mac = device_data['mac'].replace(':', '')

# Load token from .env
load_dotenv()
token = os.getenv('LIFX_TOKEN')

# Post request to LIFX servers to toggle lights
headers = {
    'Authorization': f'Bearer {token}',
    'Selector': device_mac
}
response = requests.post(f'https://api.lifx.com/v1/lights/id:{device_mac}/toggle', headers=headers)