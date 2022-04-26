import webbrowser
import serial
import random
import pyautogui #for keyboard input thru python
import os
import sys
import time
import psutil

ser = serial.Serial('/dev/cu.usbmodem141401', 9800)

lofi = [
    'https://www.youtube.com/watch?v=1fueZCTYkpA',
    'https://www.youtube.com/watch?v=on9BTX6dHN0',
    'https://www.youtube.com/watch?v=aDZixwlho48',
    'https://www.youtube.com/watch?v=lf6refTxQs8',
    'https://www.youtube.com/watch?v=bp9QQJ9P6Oo',
    'https://www.youtube.com/watch?v=eMbgHd-9Y_0',
    'https://www.youtube.com/watch?v=TURbeWK2wwg',
    'https://www.youtube.com/watch?v=NEwx4rC6VBw',
]

classical = [
    'https://www.youtube.com/watch?v=NxHLSbHOkdc',
    'https://www.youtube.com/watch?v=BMuknRb7woc',
    'https://www.youtube.com/watch?v=aepIEsxlaXc',
    'https://www.youtube.com/watch?v=mIYzp5rcTvU',
    'https://youtu.be/4fezP875xOQ',
    'https://www.youtube.com/watch?v=jgpJVI3tDbY',
]

jazz = [
    'https://www.youtube.com/watch?v=Y-JQ-RCyPpQ',
    'https://www.youtube.com/watch?v=VMAPTo7RVCo',
    'https://www.youtube.com/watch?v=WgmCloGBBwY',
    'https://www.youtube.com/watch?v=iIuuMNbSjDE',
    'https://www.youtube.com/watch?v=neV3EPgvZ3g',
]

piano = [
    'https://www.youtube.com/watch?v=3NycM9lYdRI',
    'https://www.youtube.com/watch?v=OeHLHNKQCXA',
    'https://www.youtube.com/watch?v=MYTfTKGSRr8',
    'https://youtu.be/UWYPTui1wCc',
    'https://www.youtube.com/watch?v=p02aYkdc0a4',
    'https://www.youtube.com/watch?v=mzq1CJJjQ2g',
]

soundtrack = [
    'https://youtu.be/LKI9aczEL3g',
    'https://www.youtube.com/watch?v=6pDFAEHdi38',
    'https://www.youtube.com/watch?v=xV2O-xUyNH8',
    'https://www.youtube.com/watch?v=IqiTJK_uzUY',
    'https://www.youtube.com/watch?v=32oQrjSCUTw',
    'https://www.youtube.com/watch?v=q7nclADU6tU',
    'https://www.youtube.com/watch?v=K69tbUo3vGs',
]

unlocked = False

#function to read rfid input
def rfid():
    RFID_data = ser.readline()
    if RFID_data:
        RFID_data = RFID_data.decode()
        return(RFID_data)

def wake_up():
    #pyautogui.click()
    pyautogui.press('enter')
    pyautogui.write('hello0724')
    pyautogui.press('enter')
    #os.system("pmset sleepnow")

#main
while unlocked == False:
    data = rfid()
    if '05105405F026' in data:
        wake_up()
        unlocked = True

while unlocked:
    data = rfid()

    if '0B0086059021' in data:
        link = random.choice(lofi)
        webbrowser.open(link)

    if '0D21508201B' in data:
        link = random.choice(classical)
        webbrowser.open(link)

    if '0C21A0C301B' in data:
        link = random.choice(jazz)
        webbrowser.open(link)

    if '0E00E309001B' in data:
        link = random.choice(piano)
        webbrowser.open(link)

    if '0F00DC1C01B' in data:
        link = random.choice(soundtrack)
        webbrowser.open(link)
    