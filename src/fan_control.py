import RPi.GPIO as GPIO
import time
import signal
import sys
import logging
import os

# Configuration
FAN_PIN = 18            # BCM pin used to drive PWM fan
WAIT_TIME = 1           # [s] Time to wait between each refresh
PWM_FREQ = 25           # [kHz] 25kHz for Noctua PWM control

# Configurable temperature and fan speed
MIN_TEMP = 40
MAX_TEMP = 70
FAN_LOW = 40
FAN_HIGH = 100
FAN_OFF = 0
FAN_MAX = 100

# Get CPU's temperature
def get_cpu_temperature():
    res = os.popen('vcgencmd measure_temp').readline()
    temp =(res.replace("temp=","").replace("'C\n",""))
    logging.debug("temp is {0}".format(temp))
    return temp

# Set fan speed
def set_fan_speed(speed):
    fan.start(speed)
    return()

# Handle fan speed
def handle_fan_speed():
    temp = float(get_cpu_temperature())
    # Turn off the fan if the temperature is below MIN_TEMP
    if temp < MIN_TEMP:
        set_fan_speed(FAN_OFF)
        logging.debug("Fan OFF")
    # Set fan speed to MAXIMUM if the temperature is above MAX_TEMP
    elif temp > MAX_TEMP:
        set_fan_speed(FAN_MAX)
        logging.debug("Fan MAX")
    # Calculate dynamic fan speed
    else:
        step = (FAN_HIGH - FAN_LOW)/(MAX_TEMP - MIN_TEMP)
        temp -= MIN_TEMP
        set_fan_speed(FAN_LOW + (round(temp) * step))
        logging.debug(FAN_LOW + ( round(temp) * step ))
    return ()

try:
    # Setup GPIO pin
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(FAN_PIN, GPIO.OUT, initial=GPIO.LOW)
    fan = GPIO.PWM(FAN_PIN,PWM_FREQ)
    set_fan_speed(FAN_OFF)
    # Handle fan speed every WAIT_TIME sec
    while True:
        handle_fan_speed()
        time.sleep(WAIT_TIME)

except KeyboardInterrupt: # trap a CTRL+C keyboard interrupt
    set_fan_speed(FAN_HIGH)
    #GPIO.cleanup() # resets all GPIO ports used by this function