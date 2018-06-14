### Project Notes

The printer is an EPSON TM-T88IV USB POS printer which takes 80mm paper.
There are no ARM linux drivers for this printer. 
However POS printers typically use a standard command set called ESC/POS developed by EPSON.
Different printers support different subsets of the commands. The printer is recognized by the USB enumeration in
the R-Pi and can be commanded via python3 usb control, via the easy to use interface 
[python-escpos](https://github.com/python-escpos/python-escpos). 
This can be installed via pip3 according to the 
[documentation](http://python-escpos.readthedocs.io/en/latest/user/installation.html).

In order to get the right USB parameters you need the vendor ID (=0x04b8), product ID (=0x0202), 
OUT endpoint address (=0x01), and IN endpoint address (=0x82). 
The python-escpos library provides support for the TM-T88IV, however these POS printers use many of the same 
commands, you just need to be able to open the USB device and write and read data to the correct end point addresses.

You can get all the USB information about the printer when it is plugged in with the commands `sudo lsusb`, to show USB devices and their vendor and product IDs, and `sudo lsusb -vvv -d 04b8:0202` to get all the info for the specific device.

For some reason the supplied printer had the DIP switches set incorrectly. The factory default is to have all the DIP switches turned off except for Bank 2, Switch 8, which should be on. However the manual gives no reason for this default choice. The configuration that was present when the printer was supplied does not make any sense according to the printer manual. However I can see no functional difference between the two. Bank 2 Switches 3 and 4 select the print density, which defaults to light. This seems to be completely sufficient.

### Software Considerations

* This printer does not send a paper out indication, instead it goes off line when the paper runs out. The software should be checking this.
* Software should be robust to printer malfunctions and USB comms glitches.
* The running status of the software should be monitored with a cron job so that it gets restarted if it fails for some reason.
* For the random printing of info from each printer unit, each unit needs to start with a different random seed.
* Software should start running after boot and once the printer has been enumerated on the USB.
* I think that the software should print random bursts of tweets followed by a 30 second or so cool down period.
* The software should handle shutdown of the R-Pi on power fail.
* The software should not assume the printer is in a *nice* state on boot up, and should issue reset commands ESC-@.

