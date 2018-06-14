# ThermalPrinter
An automated system to print items to an EPSON TM-T88IV POS thermal printer from the Raspberry PI.

This project requires a thermal printer to print out information automatically and not to require much maintenance. It must print from a cheap Raspberry Pi Zero W onto an EPSON point-of-sale (POS) printer (TM-T88IV). Annoyingly there is no Linux driver for this printer, however it can be fairly easily driven by ESC/POS commands via raw USB comms.

Another requirement is that the printer plus Pi must be able to withstand power on and power off and automatically be ready to print after power on, and not to corrupt the Pi file system on power down. This requires some kind of un-interruptible PSU that can give the Pi about 30 seconds of shut down time on power loss.

To get a back-up printer working an Adafruit serial printer was connected to a Mac and experiments were carried out to test this using python and to understand the ESC/POS interface.

### Contents of this repository:

* Experiments to print using the ESC/POS interface on a small serial Adafruit thermal printer using python from the Mac are in the folder `Adafruit`.

* Documentation on the EPSON TM-T88IV printer is in folder `TM-T88IV`.

* Also see [Notes](notes.md).
