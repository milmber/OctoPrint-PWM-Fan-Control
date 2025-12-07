# Raspberry Pi PWM Fan Control

Fork of https://github.com/DriftKingTW/Raspberry-Pi-PWM-Fan-Control to allow using
a Noctua NF-A4x10 5V PWM fan with a Raspberry Pi and the [OctoPrint Top Temp](https://github.com/LazeMSS/OctoPrint-TopTemp) plugin for [OctoPrint](https://octoprint.org/)

See the original documentation for wiring the PWM fan to the Pi [Using Raspberry Pi to Control a PWM Fan and Monitor its Speed](https://blog.driftking.tw/en/2019/11/Using-Raspberry-Pi-to-Control-a-PWM-Fan-and-Monitor-its-Speed/)

# Installation

1. Download the [install_cpu_fan_control.sh](install_cpu_fan_control.sh) script to your OctoPrint Raspberry Pi.
2. Configure the `INSTALL_DIR` variable inside the script to your desired installation directory.
3. Run the script with `sudo bash install_cpu_fan_control.sh`.
4. Install the [OctoPrint Top Temp](https://github.com/LazeMSS/OctoPrint-TopTemp) plugin via the OctoPrint Plugin Manager.
5. Configure the [OctoPrint Top Temp](https://github.com/LazeMSS/OctoPrint-TopTemp) plugin to use the CPU temperature sensor using `Command` type with the command:
   ```
   /usr/bin/bash /home/pi/cpu_fan_control/read_fan_speed.sh
   ```