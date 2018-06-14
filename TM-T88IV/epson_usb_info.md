# Information about the USB configuration of the printer

To obtain this information one must use `lsusb` to find the printer vendor and product codes of the printer that is plugged in. This works without a 
printer driver. For this printer the codes are 0x04b8 and 0x0202. After that run the command with `lsusb -vvv -d 04b8:0202` to get all the nice
USB details.

### USB details obtained:

* Bus 001 Device 007: ID 04b8:0202 Seiko Epson Corp. Receipt Printer M129C/TM-T70  
* Device Descriptor:  
  * bLength                18  
  * bDescriptorType         1  
  * bcdUSB               1.10  
  * bDeviceClass            0 (Defined at Interface level)  
  * DeviceSubClass         0  
  * bDeviceProtocol         0  
  * bMaxPacketSize0         8  
  * idVendor           0x04b8 Seiko Epson Corp.  
  * idProduct          0x0202 Receipt Printer M129C/TM-T70  
  * bcdDevice            2.00  
  * iManufacturer           1 EPSON  
  * iProduct                2 EPSON UB-U03II  
  * iSerial                 3 20160106002437453M02C  
  * bNumConfigurations      1  
  * Configuration Descriptor:  
    * bLength                 9  
    * bDescriptorType         2  
    * wTotalLength           32  
    * bNumInterfaces          1  
    * bConfigurationValue     1  
    * iConfiguration          0  
    * bmAttributes         0xc0  
      * Self Powered  
    * MaxPower               10mA  
    * Interface Descriptor:  
      * bLength                 9  
      * bDescriptorType         4  
      * bInterfaceNumber        0  
      * bAlternateSetting       0  
      * bNumEndpoints           2  
      * bInterfaceClass       255 Vendor Specific Class  
      * bInterfaceSubClass    255 Vendor Specific Subclass  
      * bInterfaceProtocol      2  
      * iInterface              0  
      * Endpoint Descriptor:  
        * bLength                 7  
        * bDescriptorType         5  
        * bEndpointAddress     0x01  EP 1 OUT  
        * bmAttributes            2  
          * Transfer Type            Bulk  
          * Synch Type               None  
          * Usage Type               Data  
        * wMaxPacketSize     0x0008  1x 8 bytes  
        * bInterval               0  
      * Endpoint Descriptor:  
        * bLength                 7  
        * bDescriptorType         5  
        * bEndpointAddress     0x82  EP 2 IN  
        * bmAttributes            2  
          * Transfer Type            Bulk  
          * Synch Type               None  
          * Usage Type               Data  
        * wMaxPacketSize     0x0040  1x 64 bytes  
        * bInterval               0  
* Device Status:     0x0001  
  * Self Powered  

