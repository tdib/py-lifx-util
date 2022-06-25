# lifx-util
Utility scripts to manipulate LIFX smart lights

## [toggle.py](./toggle.py)
Toggle a given light as specified by a `devices.json` file. An example structure of this format is given in [devices.example.json](./devices.example.json), and consists of a light name as the key, followed by the mac and ip addresses of that light. Optionally, the location of your devices file may be added as a second argument.

Usage: `python toggle.py <light_name> <devices_file.json (optional)>`