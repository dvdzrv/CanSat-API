import serial
import requests

url = "194.160.224.5:3000/message"


ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=115200,
)

while True:
    read = ser.readline()
    print(read)
    request = requests.post(url, read)
