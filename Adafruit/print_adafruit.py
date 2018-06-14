import serial
import time
import sys
import os.path

if len(sys.argv)!=2:
    print("Error: missing file name")
    exit(1)
    
filename = sys.argv[1]
if not os.path.isfile(filename):
    print("Error: file not found")
    exit(1)
    
ser = serial.Serial('/dev/cu.SLAB_USBtoUART', 19200)
with open(filename, "r") as fp:
    for fline in fp:
        ser.write(fline.encode('latin-1'))
        
ser.write(b"\n\n\n")
time.sleep(2)
ser.close()


