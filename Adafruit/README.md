# Experiments with Adafruit thermal printer

The Adafruit printer is a small thermal printer that prints on 58mm receipt paper. It runs from 5-9V @ 2A and has 
a TTL serial interface at 19200 baud.


It has a print width of 48mm with 384 dots per line. The printer will print faster with a higher supply voltage
(up to 80mm/s at 8.5V). It does not have a paper cutter and the maximum roll diameter is 39mm which is pretty small.

The manual is useful because it contains many of the commands of the standard ESC/POS command set described in complete detail.
It also contains details of the code pages which are commonly use by these printers.

### Results

I connected this printer to the Mac via a standard USB to TTL serial interface. When enumerated by the Mac this appears as
`/dev/cu.SLAB_USBtoUART`. This can be written to by sending characters via the Python `serial` module. 

The main issue to understand with this method is that the flow control is problematic because the data is being sent over
a serial connection within a USB connection. This took a while to figure out. The printer would print one character and nothing
more. This is because the python implementation immediately sends the data to a buffer and then if the code then closes the 
interface and exits, nothing gets printed beyond the first character. The solution was to end the code with a few seconds of
sleep time to allow the data to get sent to the printer. I think the serial write will probably block once the buffer is full.
I tried a few tests to get it to block until printing had finishes but was not succesful. I forget if I tried the flush command,
but mostly likely I did.

This printer can print graphics and text with no problem. It just requires a serial adapter and the python `serial` module.
It would be the same funtionality from Linux.

