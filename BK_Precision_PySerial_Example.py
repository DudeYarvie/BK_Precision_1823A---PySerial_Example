#           BK_Precision_1823A_PySerial_Example.py
#Python Version: 2.7.18
#Date: 21-DEC-2021
#Author: Jarvis Hill (e-mail: hilljarvis@gmail.com)
#Purpose:  This code serves as a reference to control the BK Precision 1823A frequency counter
#using its RS-232 communications port.  It intends to supply the novice user with a clear usage of the
#instrument cmd syntax and not obscure it using class structure(s).
#
#References:
#BK Precision Model 1823A Insruction Manual 



##Modules##
import serial                                                       #Manages serial connectivity between PC and instrument  
import time                                                         #Implements delays



##Globals##

#Serial Parameters
instr_port = 'COM5'                                                 #COM port
instr_baud = 9600                                                   #Baud rate
bytesize = 8                                                        #Number of data bits
stopbits = 1                                                        #Number of stop bits
parity = 'N'                                                        #Disbale parity checking
timeout = 10                                                        #Set a read timeout value in seconds
xonxoff = False                                                     #Disbale software flow control.    
write_timeout =  None                                               #Set a write timeout value in seconds    
inter_byte_timeout = None                                           #Inter-character timeout
dtr_state = True                                                    #Set DTR state to logic HIGH
rts_state = False                                                   #Set RTS state to logic LOW


#Instrument Settings
Period = {0:'1s',1:'0.1s',2:'0.001s',3:'0.0001s'}


##Reads data from instrument##
def read_data(instr):
    data = ''
    while True:
        ch = instr.read()
        #print chr                                                   #Print read character for debugging 
        if ch == '\r': break
        data += ch
    return data


##Queries INSTR Data##
def GET_Data(instr):
    instr.write('D0\r')
    instr_data = read_data(instr)
    return instr_data


#Main Program#
def main():

    ##Intrument Serial Bus Configs 
    instr = serial.Serial()
    instr.port = instr_port
    instr.baudrate = instr_baud
    instr.bytesize = bytesize
    instr.partiy = parity
    instr.stopbits = stopbits
    instr.timeout = timeout
    instr.xonxoff = xonxoff
    instr.write_timeout = write_timeout
    instr.inter_byte_timeout = inter_byte_timeout
    instr.dtr = dtr_state                                                 
    instr.rts = rts_state


    ## Open Serial Connection
    instr.open()    
    time.sleep(0.5)                                                  #Delay 


    ##Instrument Config
    for setting in Period:                                           #Set Channel Period
        instr.write('F0\rG'+str(setting)+'\r')
        time.sleep(0.5)


    ##Query Freq Measurement
    for i in range(0,10):
        time.sleep(10)
        print ("Frequency: " + GET_Data(instr))                     #Queries instrument and prints out reading include units                         


    ##Close Serial Connection
    instr.close()                                                  






if __name__ == "__main__":
    main()
