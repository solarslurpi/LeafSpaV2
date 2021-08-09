###############################################################################
# The leafspa module is used to maintain a consistent and pleasent environment
# for the plants in the grow tent.
#
# Author: happyday, 2021
###############################################################################
import json
import csv
from threading import Thread
import time
from datetime import datetime
import board
import adafruit_scd30
# See SO https://stackoverflow.com/questions/33019698/how-to-properly-round-up-half-float-numbers
from decimal import localcontext, Decimal, ROUND_HALF_UP


class LeafSpa:

    def __init__(self, json_params_file="config.json"):
        self.params = None
        self._get_settings(json_params_file)
        # TODO: Validate params
        i2c = board.I2C()   # uses board.SCL and board.SDA
        self.scd = adafruit_scd30.SCD30(i2c)
        self.sensors_thread = None
        self.header = ["Date/Time", "CO2", "Temperature", "Humidity"]
        self.stop_threads = False

    def _get_settings(self, json_params_file):
        with open(json_params_file) as f:
            self.params = json.load(f)

# See SO https://stackoverflow.com/questions/33019698/how-to-properly-round-up-half-float-numbers
    def _to_int(self, float_num):
        with localcontext() as ctx:
            ctx.rounding = ROUND_HALF_UP
            n = Decimal(float_num)
            return(n.to_integral_value())

    def _write_csv_line(self, header=False):
        open_file_for_write = 'a'
        if header is True:
            open_file_for_write = 'w'
        with open(self.params["filename"], open_file_for_write) as sensor_readings:
            sensor_write = csv.writer(sensor_readings, delimiter=',')
            if header is True:
                sensor_write.writerow(self.header)
            else:
                temp_F = 9./5. * self.scd.temperature + 32
                sensor_write.writerow([datetime.today().strftime('%Y-%m-%d %H:%M:%S'), self._to_int(self.scd.CO2), self._to_int(temp_F), self._to_int(self.scd.relative_humidity)])

    def _adjust_CO2(self):
        """During photosynthesis, the CO2 level should be about 1,000 ppm. 
           This way, energy conversion is accelerated.
        """
        pass

    def _check_environment(self):
        """ Take Readings, write readings to a file, adjust environment if readings
            suggest the environment is out of range.  The parameter 
            'time_between_readings' sets how often the readings are taken.
        """
        while True:
            # Get a reading for temperature, humidity, and CO2
            if self.stop_threads:
                break
            if self.scd.data_available:
                self._write_csv_line()
            # I use a photoresistor to determine if the LEDs are on.  This way,
            # if the times change for LED on/off, the photoresister will allow me
            # to detect the change without modifying parameters.
            if self.photoresistor.on:
                self._adjust_CO2()
            time.sleep(self.params['time_between_readings'])

    def _take_picture(self):
        while True:
            if self.stop_threads:
                break
            print("SNAP!")
            time.sleep(self.params['time_between_pictures'])

    def start(self):
        """start is used to start taking pictures, reading measurements, and adjusting the environment.
        """
        self.sensors_thread = Thread(target=self._check_environment)
        if self.params["overwrite_readings"] is True:
            self._write_csv_line(header=True)
        self.sensors_thread.start()
        self.camera_thread = Thread(target=self._take_picture)
        self.camera_thread.start()

    def stop(self):
        self.stop_threads = True
        print("BEFORE")
        print("sensors thread is alive: {}".format(self.sensors_thread.is_alive()))
        print("camera thread is alive: {}".format(self.camera_thread.is_alive()))
        self.sensors_thread.join()
        self.camera_thread.join()
        print("AFTER")
        print("sensors thread is alive: {}".format(self.sensors_thread.is_alive()))
        print("camera thread is alive: {}".format(self.camera_thread.is_alive()))
