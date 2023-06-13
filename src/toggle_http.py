import requests
import os
from dotenv import load_dotenv
from util import extract_device_data

# Extract light mac address
device_data = extract_device_data()
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