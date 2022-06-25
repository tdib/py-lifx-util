# lifx-util
Utility scripts to manipulate LIFX smart lights

## [toggle.py](./toggle.py)
Toggle a given light as specified by a `devices.json` file. An example structure of this format is given in [devices.example.json](./devices.example.json), and consists of a light name as the key, followed by the mac and ip addresses of that light. Optionally, the location of your devices file may be added as a second argument.

Usage: `python toggle.py <light_name> <devices_file.json (optional)>`


## [toggle_http.py](./toggle_http.py)
Toggles a light via the http protocol and LIFX servers.

Requires a `devices.json` file containing a label for your light (key value) and mac address. An example format of this file can be found in [devices.example.json](./devices.example.json). This does not require the `ip` field.

Also Requires a `.env` file containing a LIFX token which can be found in [.env.example](./.env.example).

Note that since this method uses http, there may be some latency depending on your geographic location.

Usage: `python toggle_http.py <light_name> <devices_file.json (optional)>`