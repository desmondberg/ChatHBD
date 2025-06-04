#this code was made with the help of a a tutorial by RandomNerdTutortials: https://RandomNerdTutorials.com/raspberry-pi-dht11-dht22-python/

import board
import adafruit_dht
import time

# Sensor data pin is connected to GPIO 17
sensor = adafruit_dht.DHT22(board.D17)


def getTemperature():
    try:
        temperature = sensor.temperature
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
    except Exception as error:
        sensor.exit()
        raise error
    return temperature
    

def getHumidity():
    try:
        humidity = sensor.humidity
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
    except Exception as error:
        sensor.exit()
        raise error
    return humidity
