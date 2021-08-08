# Leafspa V2
The goal is to provide the optimal growing environment using sensors to monitor and.  
## Plant Growth Stages
Our plant's growth is broken into stages:
- Germination: seed to cotyledon _Note: We can successfully get to a cotyledon without a need for sensors or effectors at this stage._
- Seedling: First serrated leaf to 2-3 sets of serrated leaves.  At this stage, we need to start monitoring and effecting the envioronment.
- Vegetative: Until buds start to form.
- Flowering: Buds until harvest.

## Environmental Growth Factors
Environmental growth factors include:
- pH of the soil.  The pH of the soil should be between 5.5 and 6.5.
- An "ideal" wetness of the soil.  The "ideal" wetness will change as the plant grows into another growth stage.
- Quantity and quality of light.  Plants use the Photosynthesis process to grow.  This requires light within the PAR spectrum as well as the "ideal" amount of photons hitting the leaves during a daily photoperiod.
## Optimal Environmental Settings
Optimal Environmental Settings depends on the Growth stage the plant is in.  With that said, air should always be circulating to reduce the chance of mold and mildew.
### Seedling
- Temperature: 75F to 80F
- Humidity: 30 to 40 percent RH
- Light: 18 on / 6 off photoperiod, veg setting, PPFD starts during the first week at 200.  After that the PPFD will be set to 300. _Note: [source - Understanding Grow Light PAR, PPFD, Wattage and DLI (2021)](https://420expertguide.com/resource/grow-light-par-ppf-ppfd-values-decoded/)_
### Vegetative
### Flowering

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
