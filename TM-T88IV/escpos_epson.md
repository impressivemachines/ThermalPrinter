# Overview of the valid ESC/POS commands for the TM-T88IV printer

The detail of the ESC/POS commands can be found at the [official site](https://reference.epson-biz.com/modules/ref_escpos/index.php?content_id=2#). On that site, once you select your printer model, it will provide additional implementation details associated with the printer type.

These are the non-deprecated commands for the printer.

* **HT** Horizontal tab (09)
* **LF** Print and line feed (0A)
* **FF (in Page mode)** Print and return to Standard mode (in Page mode) (0C)
* **CR** Print and carriage return (0D)
* **DLE EOT** Transmit real-time status (10 04 n) n: 01 get printer status, 02 get offline cause, 03 get error status, 04 get paper sensor status
* **DLE ENQ** Send real-time request to printer
* **DLE DC4 (fn=1)** Generate pulse in real-time
* **DLE DC4 (fn=2)** Execute power-off sequence
* **DLE DC4 (fn=8)** Clear buffer(s)
* **CAN** Cancel print data in Page mode
* **ESC FF** Print data in Page mode
* **ESC SP** Set right-side character spacing
* **ESC !** Select print mode(s)
* **ESC $** Set absolute print position
* **ESC %** Select/cancel user-defined character set
* **ESC &** Define user-defined characters
* **ESC \*** Select bit-image mode
* **ESC -** Turn underline mode on/off
* **ESC 2** Select default line spacing
* **ESC 3** Set line spacing
* **ESC =** Select peripheral device
* **ESC ?** Cancel user-defined characters
* **ESC @** Initialize printer
* **ESC D** Set horizontal tab positions
* **ESC E** Turn emphasized mode on/off
* **ESC G** Turn double-strike mode on/off
* **ESC J** Print and feed paper
* **ESC L** Select Page mode
* **ESC M** Select character font
* **ESC R** Select an international character set
* **ESC S** Select Standard mode
* **ESC T** Select print direction in Page mode
* **ESC V** Turn 90° clockwise rotation mode on/off
* **ESC W** Set print area in Page mode
* **ESC \\** Set relative print position
* **ESC a** Select justification
* **ESC c 3** Select paper sensor(s) to output paper-end signals
* **ESC c 4** Select paper sensor(s) to stop printing
* **ESC c 5** Enable/disable panel buttons
* **ESC d** Print and feed n lines
* **ESC p** Generate pulse
* **ESC t** Select character code table
* **ESC {** Turn upside-down print mode on/off
* **GS !** Select character size (1D 21 n)
* **GS $** Set absolute vertical print position in Page mode
* **GS ( A** Execute test print
* **GS ( D** Enable/disable real-time command
* **GS ( E** Set user setup commands
* **GS ( E \<fn=1\>** Change into the user setting mode
* **GS ( E \<fn=2\>** End the user setting mode session
* **GS ( E \<fn=5\>** Set the customized setting values
* **GS ( E \<fn=6\>** Transmit the customized setting values
* **GS ( E \<fn=11\>** Set the configuration item for the serial interface
* **GS ( E \<fn=12\>** Transmit the configuration item for the serial interface
* **GS ( H** Request transmission of response or status
* **GS ( H \<fn=48\>** Specifies the process ID response
* **GS ( K** Select print control method(s)
* **GS ( K \<fn=50\>** Select the print speed
* **GS ( K \<fn=97\>** Select the number of parts for the thermal head energizing
* **GS ( L / GS 8 L** Set graphics data
* **GS ( L \<fn=48\>** Transmit the NV graphics memory capacity
* **GS ( L \<fn=50\>** Print the graphics data in the print buffer
* **GS ( L \<fn=51\>** Transmit the remaining capacity of the NV graphics memory
* **GS ( L \<fn=64\>** Transmit the key code list for defined NV graphics
* **GS ( L \<fn=65\>** Delete all NV graphics data
* **GS ( L \<fn=66\>** Delete the specified NV graphics data
* **GS ( L / GS 8 L \<fn=67\>** Define the NV graphics data (raster format)
* **GS ( L \<fn=69\>** Print the specified NV graphics data
* **GS ( L / GS 8 L \<fn=112\>** Store the graphics data in the print buffer (raster format)
* **GS ( N** Select character effects
* **GS ( N \<fn=48\>** Select character color
* **GS ( k** Set up and print the symbol
* **GS ( k \<fn=165\>** QR Code: Select the model
* **GS ( k \<fn=167\>** QR Code: Set the size of module
* **GS ( k \<fn=169\>** QR Code: Select the error correction level
* **GS ( k \<fn=180\>** QR Code: Store the data in the symbol storage area
* **GS ( k \<fn=181\>** QR Code: Print the symbol data in the symbol storage area
* **GS ( k \<fn=182\>** QR Code: Transmit the size information of the symbol data in the symbol storage area
* **GS :** Start/end macro definition
* **GS B** Turn white/black reverse print mode on/off
* **GS H** Select print position of HRI characters
* **GS I** Transmit printer ID
* **GS L** Set left margin
* **GS P** Set horizontal and vertical motion units
* **GS V** Select cut mode and cut paper
* **GS W** Set print area width
* **GS \*** Set relative vertical print position in Page mode
* **GS ^** Execute macro
* **GS a** Enable/disable Automatic Status Back (ASB)
* **GS b** Turn smoothing mode on/off
* **GS f** Select font for HRI characters
* **GS g 0** Initialize maintenance counter
* **GS g 2** Transmit maintenance counter
* **GS h** Set barcode height
* **GS k** Print barcode
* **GS r** Transmit status
* **GS w** Set barcode width
