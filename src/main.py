#import keyboard  # using module keyboard
from time import sleep
import serial
ser = serial.Serial('/dev/ttyUSB0',38400)  # open serial port



def getCommand(com,datalen,data):
    cmd = b'<'
    cmd += bytes(chr(com),'ascii')
    cmd += bytes(chr(datalen),'ascii')
    cmd += b':'
    for char in data:
        cmd += bytes(char,'ascii')
        pass
    cmd += b'>'
    return cmd

print(ser.name)         # check which port was really used

count = 0
ctr = 0

sendstr = ''

while True:
    #print('asdasd')
    #Use this try except block to cancel the program
    if ser.in_waiting > 0:
        try:
            sendstr = ser.read(ser.in_waiting)
            print(sendstr)
        except serial.SerialException as e:
            print(e)
        pass
    
    count += 1
    if count > 100:
        msg = 'From serial debugger'
        cmd = getCommand(97,len(msg),msg)
        ser.write(cmd)
        print(cmd)
        count = 0
        ctr += 1
    sleep(0.02)     #20 Milliseconds


