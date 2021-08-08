# Leafspa V2
Welcome plants to an environmentally controlled grow space.  Where we make sure:

# Hardware
- [Rasp Pi Zero W](https://www.adafruit.com/product/3400) 
- [Power cord for Rasp Pi](https://www.adafruit.com/product/1995)
- [SD/MicroSD Card](https://www.adafruit.com/product/2693)
- [Rasp Pi Camera V2](https://www.adafruit.com/product/3099)
- [Rasp Pi Zero Camera Cable](https://www.adafruit.com/product/3157)
- [Adafruit SCD-30 - NDIR CO2 Temperature and Humidity Sensor](https://learn.adafruit.com/adafruit-scd30)
## Wiring
- Rasp Pi Camera: 
- SCD 30: I followed [Adafruit's wiring guide](https://learn.adafruit.com/adafruit-scd30/python-circuitpython#python-computer-wiring-3081030-6)

# Raspberry Pi
## Update the OS

As noted in [the documentation](https://www.raspberrypi.org/documentation/raspbian/updating.md), _First, update your system's package list by entering the following command:_
```
sudo apt update
```
_Next, upgrade all your installed packages to their latest versions with the following command:_
```
sudo apt full-upgrade

```
_Generally speaking, doing this regularly will keep your installation up to date for the particular major Raspberry Pi OS release you are using..._
## Install Circuit Python
Adafruit has [a web page](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi) that walked me through what commands need to be execuited on the raspberry pi.
## Install Library for SCD-30

## Install SMB Support
To view files (photos for example) on a Windows PC, I installed the SMB service following [these instructions](https://pimylifeup.com/raspberry-pi-samba/). 

# Photosynthesis
My job is to increase the photosynthetic process.  
![photosynthesis](images\photosynthesis.jpg)
I'll do this by optimizing these environmental factors:
- temperature
- humidity
- light level
- CO2 level
## CO2 Level
During photosynthesis, plants take in CO2 and water.  Research (in my case Google searches) point out plants will give a 30% bigger yield if we increase the amount of CO2 to between 800 ppm and 1,200 ppm during photosynthesis.  Photosynthesis occurs when there is light.  So the additional CO2 is only needed when the grow lights are on.
