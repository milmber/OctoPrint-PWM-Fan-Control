#!/bin/bash
INSTALL_DIR="/home/pi/cpu_fan_control"
mkdir -p "${INSTALL_DIR}"
wget https://raw.githubusercontent.com/milmber/OctoPrint-PWM-Fan-Control/master/fan_control.py -O "${INSTALL_DIR}"/fan_control.py
wget https://raw.githubusercontent.com/milmber/OctoPrint-PWM-Fan-Control/master/read_fan_speed.py -O "${INSTALL_DIR}"/read_fan_speed.py
wget https://raw.githubusercontent.com/milmber/OctoPrint-PWM-Fan-Control/master/cpu_fan_control.service -O "${INSTALL_DIR}"/cpu_fan_control.service
sudo cp "${INSTALL_DIR}"/cpu_fan_control.service /lib/systemd/system/
sudo systemctl enable cpu_fan_control.service
sudo systemctl start cpu_fan_control.service
sudo systemctl status cpu_fan_control.service