#!/bin/bash
INSTALL_DIR="/home/pi/cpu_fan_control"
# Setting this env variable is required because the GPIO library will by
# default try to write to the caller directory which will fail when called from OctoPi.
# See https://github.com/gpiozero/gpiozero/discussions/1153#discussioncomment-13373112
export LG_WD=/tmp
python3 "${INSTALL_DIR}"/read_fan_speed.py