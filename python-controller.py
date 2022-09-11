import serial
import time
import keyboard

arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)
olddata = ''
text = ''
while(True):
    data = arduino.readline()
    try:
        data = str(data, 'utf-8')
        if('x' in data):
            if(int(data[1:]) > 1024/2 + 1024/4):
                keyboard.press('right')
                keyboard.release('left')
            elif(int(data[1:]) < 1024/2 - 1024/4):
                keyboard.press('left')
                keyboard.release('right')
            else:
                keyboard.release('left')
                keyboard.release('right')
        elif('y' in data):
            if(int(data[1:]) > 1024/2 + 1024/4):
                keyboard.press('up')
            elif(int(data[1:]) < 1024/2 - 1024/4):
                keyboard.press('down')
            else:
                keyboard.release('up')
                keyboard.release('down')
    except:
        pass
    if(keyboard.is_pressed('F6')):
        break
