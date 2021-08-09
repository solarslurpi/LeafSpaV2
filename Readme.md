# Leafspa V2
<<<<<<< HEAD
Welcome plants to an environmentally controlled grow space.  
## Resources
[Common Cannabis Deficiencies](https://www.youtube.com/watch?v=ZTE-YCNWC8s)
## Journaling
I am journaling my successes/failures using DayOne on my iPhone.  DayOne is not available on Windows....

=======
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
- Temperature: 
  - (ref I didn't get link): 75F to 80F
  - [68-77F](https://www.ilovegrowingmarijuana.com/temperature/#effects)
- Humidity: 30 to 40 percent RH
- Light: 18 on / 6 off photoperiod, veg setting, PPFD starts during the first week at 200.  After that the PPFD will be set to 300. _Note: [source - Understanding Grow Light PAR, PPFD, Wattage and DLI (2021)](https://420expertguide.com/resource/grow-light-par-ppf-ppfd-values-decoded/)_
### Vegetative
- Temperature:
  - [68-77F](https://www.ilovegrowingmarijuana.com/temperature/#effects)
### Flowering
- Temperature:
  - [< 82F](https://www.ilovegrowingmarijuana.com/temperature/#effects)
>>>>>>> bc67a1490070b28e1f5f5b787c265f407da729ba

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
# Roots

![roots](images\roots.jpg)

## pH and EC
The pH and EC need to be right for the roots to be able to take up the nutrients.  pH and EC values can dramatically change based on minerals either in the water or uptake of nutrients.  Spot check and adjust each week using the [Pour Though Method](http://www.css.cornell.edu/courses/260/Media%20testing.pdf)
- pH should be between 5.5 and 6.5.
- [EC](https://www.cannaconnection.com/blog/1903-ideal-ec-range-plants#:~:text=An%20indicative%20EC%20range%20for,significantly%20different%20values%20of%20EC.)
... _An indicative EC range for cannabis plants is 0.8-1.3 for seedlings; 0.5-1.3 for clones; 1.3-1.7 under vegetative phase; 1.2-2 during flowering. Different varieties of cannabis might require significantly different values of EC._


## Light Level
- [ppfd to dli](https://youtu.be/tKzmx6XDOkE?t=330)
    - PPFD: One PAR reading at a specific time (photosynthetic photon flux density)
    - DLI: integrating readings across a time period (Daily Light Integral)

![ppfd to dli](images\PPFDvsDLI.jpg) 

- DLI (the total number of photons of PAR accumulated over one given hour, over a 24 hour period).  
- Typical photoperiods are 18 hour (long day plants) and 12 hour (short day plants).
```
DLI = PPFD ( in umol/m2/s) x 60 (minutes/hour) x 60 (seconds/minute) x photoperiod / 1,000,000 umol/mol
```
- Weekly Amounts

![AmountOfPPFD](images\AmountOfPPFDpergrowingCycle.jpg)

- Early growth and vegetative (Photoperiod = 18 hours):
    - First week: 200
    - Second week: 300
    - Third week: 400
    - Fourth and Fifth week: 600
- Moving to flower stage (Photoperiod = 12 hours):
    - Start at 650, increase 40 umols / day for first 10 days.
    - After 10 days, stay at 1000

## CO2 Level
During photosynthesis, plants take in CO2 and water.  Research (in my case Google searches) point out plants will give a 30% bigger yield if we increase the amount of CO2 to between 800 ppm and 1,200 ppm during photosynthesis.  Photosynthesis occurs when there is light.  So the additional CO2 is only needed when the grow lights are on.

## Watering
Because of high PPFD, I'll keep the soil moist (no dry out stress) using the Blumat irrigation.


