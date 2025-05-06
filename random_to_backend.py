import random
from time import sleep

import requests

url = "http://194.160.224.5:3000/message"
data_start = {
    "LON": random.randint(20, 25) * 100 / random.randrange(1, 5),
    "LAT": random.randint(20, 25) * 100 / random.randrange(1, 5),
    "ALT": random.randint(20, 25) * 100 / random.randrange(1, 5),
    "TVOC": random.randint(200, 2500),
    "AQI": random.randint(1, 5),
    "CO2": random.randint(1000, 50000),
    "PRESS": random.randint(1000, 500000),
    "ALT_P": random.randint(1000, 50000),
}
while True:
    data = {
        "LON": data_start["LON"] + (random.randint(20, 25)/10 * random.randint(-1, 1)),
        "LAT": data_start["LAT"] + (random.randint(20, 25)/10 * random.randint(-1, 1)),
        "ALT": data_start["ALT"] + (random.randint(20, 25)/10 * random.randint(-1, 1)),
        "TVOC": data_start["TVOC"] + (random.randint(20, 25)/10 * random.randint(-1, 1)),
        "AQI": data_start["AQI"] + (random.randint(20, 25)/10 * random.randint(-1, 1)),
        "CO2": data_start["CO2"] + (random.randint(20, 25)/10 * random.randint(-1, 1)),
        "PRESS": data_start["PRESS"] + (random.randint(20, 25)/10 * random.randint(-1, 1)),
        "ALT_P": data_start["ALT_P"] + (random.randint(20, 25)/10 * random.randint(-1, 1)),
    }
    request = requests.post(url, data)
    print(data)
    sleep(2)