from lifxlan import Light
from util import extract_device_data
from time import sleep

# Extract light data and convert into LIFXLan Light object
device_data = extract_device_data()
device = Light(device_data['mac'], device_data['ip'])

hue = 0
saturation = 1
brightness = 0.6
kelvin = 3500

startValue = 4000
time = 10

saturation *= 65535
brightness *= 65535
start = 5000
errCount = 0

try:
    while True:
        for i in range(start, 65535, 10):
            device.set_color((i,saturation,brightness,kelvin), rapid=True)
            sleep(time/100)
except Exception as e:
    errCount += 1
    print("Error", i)
    print(e)