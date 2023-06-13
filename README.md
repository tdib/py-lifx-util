# lifx-util
Utility scripts to manipulate LIFX smart lights.

Note: For all scripts below, a `devices.json` file is required. An example structure of this format is given in [devices.example.json](./devices.example.json), and consists of a light name as the key, followed by the mac and ip addresses of that light. For the following scripts, the location of your devices file may optionally be added as a second argument, and if not provided, will default to `devices.json`. This file will be used to target the specified light name as provided by the user.



## [toggle.py](./toggle.py)
Toggle a given light on or off, specified by name.

Usage: `python toggle.py <light_name> <devices_file.json (optional)>`


## [toggle_http.py](./toggle_http.py)
Toggles a light via the http protocol and LIFX servers.

For this script, the device in the `devices.json` file does not not require the `ip` field. The script does, however, require a `.env` file containing a LIFX token. The example format can be found in [.env.example](./.env.example).

Note that since this method uses http, there may be some latency depending on your geographic location.

Usage: `python toggle_http.py <light_name> <devices_file.json (optional)>`

## [screen_average.py](./screen_average.py)
Make a given light change depending on the average colour of your screen.

Usage: `python screen_average.py <light_name> <devices_file.json (optional)>`

## [rainbow.py](./rainbow.py)
Cycle a light through the colours of a rainbow.

Usage: `python rainbow.py <light_name> <devices_file.json (optional)>`