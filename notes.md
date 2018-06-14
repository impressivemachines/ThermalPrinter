### Printer Information

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
