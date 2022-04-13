import webbrowser
import serial
import random

ser = serial.Serial('/dev/cu.usbmodem142401', 9800, timeout = 1)

lofi = [
    'https://www.youtube.com/watch?v=1fueZCTYkpA',
    'https://www.youtube.com/watch?v=on9BTX6dHN0',
    'https://www.youtube.com/watch?v=aDZixwlho48',
    'https://www.youtube.com/watch?v=lf6refTxQs8',
]

#function to read rfid input
def rfid():
    RFID_data = ser.readline()
    if RFID_data:
        RFID_data = RFID_data.decode()
        return(RFID_data)

while True:
    data = rfid()
    print(data)
    if data == '0B0086059021':
        link = random.choice(lofi)
        webbrowser.open(link)