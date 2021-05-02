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
    ser.write('flash all\n'.encode('utf-8'))
    #ser.flush()
    #write_flag =1
    time.sleep(0.5)
    #if write_flag == 1:
    line_count = 0
    while True:

        data = ser.readline()[:-2].decode('utf-8')
        print(data)
        line_count  += 1

        if line_count > 2:
            break

'''
    lan_mac = data.split('=')[-1]
    print(lan_mac)
    logging.warning('3')
    time.sleep(3)

'''
