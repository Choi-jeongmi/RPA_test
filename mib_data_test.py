import RPi.GPIO as GPIO
import serial
import time
import logging 
from datetime import datetime
import sys

DEVICE = "/dev/ttyS0"
BAUDRATE = 38400
ser = serial.Serial(DEVICE,BAUDRATE,timeout=10)
#ser.flushOutput()

logging.basicConfig(format='%(asctime)s %(message)s')
logging.warning(' ')
lan_flag = 0
wan_flag = 0
write_flag = 0
while True:
    ser.flushInput()
    ser.flushOutput()
    logging.warning('0')
    ser.write('flash get HW_NIC0_ADDR\n'.encode('utf-8'))
    #ser.flush()
    #write_flag =1
    logging.warning('1')
    time.sleep(0.5)
    #if write_flag == 1:
    logging.warning('2')
    line_count = 0
    while True:

        data = ser.readline()[:-2].decode('utf-8')
        print(data)
        line_count  += 1

        if line_count >= 2:
            break

    lan_mac = data.split('=')[-1]
    print(lan_mac)
    logging.warning('3')
    time.sleep(3)
'''    
   while True:

        data = ser.readline()[:-2].decode('utf-8')
        lan_mac = data.split('=')[-1]
        print(lan_mac)
        lan_flag = 1
        logging.warning('lan_flag')
        #ser.flushOutput()
        time.sleep(5)

        if lan_flag == 1:
            ser.write('flash get HW_NIC1_ADDR\n'.encode('utf-8'))
            print(data)

            wan_mac = data.split('=')[-1]
            print(wan_mac)
            wan_flag = 1
            logging.warning('wan_flag')
            #ser.flushOutput()
            time.sleep(5)

            if wan_flag == 1:
        
                ser.write('reboot\n'.encode('utf-8'))
                logging.warning('reboooooting......')

                time.sleep(120)
                ser.write('flash get HW_NIC0_ADDR\n'.encode('utf-8'))
        
                if data.split('=')[-1] == lan_mac:
                    continue
                else:
                    logging.warning('============MIB DATA CHANGED!!!!============')

'''
