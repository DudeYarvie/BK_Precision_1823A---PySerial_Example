# BK_Precision_1823A---PySerial_Example
Python example for controlling the BK Precision 1823A Frequency Counter. The Python script communicates to the instrument via the serial interface accesible through the RS-232 port.  

# File Descriptions
*BK_Precision_1823A_PySerial_Example.py* provides the example for using PySerial to control the BK Precision 1823A
*BK_1823A_Instruction_Manual.pdf* provides instrument performance and electrical specifications and control command set

# Usage
1. Download Python v2.7.18 (choose 32 or 64 bit based on the your OS bitness) on a PC.  Other versions of Python might work with this code but they have not been tested.
2. Build or obtain an RS-232 serial cable or USB to RS232 converter that matches the standard RS-232 pinout.
3. Connect the serial cable or converter to the RS-232 port on the counter and the other end to the PC running Python. 
4. Connect an appropriate signal to CHA of the counter.  This signal needs to be within the max/min voltage levels of the counter.
5. Run the Python script provided.
