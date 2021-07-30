###############################################################################
# The leafspa module is used to maintain a consistent and pleasent environment
# for the plants in the grow tent.
#
# Author: happyday, 2021
###############################################################################
import json
from threading import Thread
import time
import board
import adafruit_scd30


class LeafSpa:

    def __init__(self, json_params_file="config.json"):
        self.params = None

        self._get_settings(json_params_file)
        i2c = board.I2C()   # uses board.SCL and board.SDA
        self.scd = adafruit_scd30.SCD30(i2c)

    def _get_settings(self, json_params_file):
        with open(json_params_file) as f:
            self.params = json.load(f)
            print(self.params["temp_settings"]["min_veg_temp"])

    def _check_environment(self):
        while True:
            if self.scd.data_available:
                print("Data Available!")
                print("CO2:", self.scd.CO2, "PPM")
                print("Temperature:", self.scd.temperature, "degrees C")
                print("Humidity:", self.scd.relative_humidity, "%%rH")
                print("")
                print("Waiting for new data...")
                print("")
            time.sleep(int(self.params['time_between_readings']))

    def start(self):
        thread = Thread(target=self._check_environment)
        thread.start()

