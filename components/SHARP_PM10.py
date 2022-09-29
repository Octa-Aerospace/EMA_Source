import os
import time
import serial


class SHARP:
    def __init__(self):
        os.system('sudo chmod 777 /dev/ttyS0')
        self.serialPort = serial.Serial(port = "/dev/ttyS0", baudrate=9600,
                           bytesize=8, timeout=1, stopbits=serial.STOPBITS_ONE)


        self.serialString = "" # Used to hold data coming over UART

    def read(self) -> str:
        os.system("sudo chmod 77 /dev/ttyS0")
        # Wait until there is data waiting in the serial buffer
        if(self.serialPort.in_waiting > 0):

            # Read data out of the buffer until a carraige return / new line is found
            self.serialString = self.serialPort.readline()

            # Print the contents of the serial data
            data = self.serialString.decode('Ascii')
            if data.strip() != "":
                try:
                    return round(float(data.strip()), 1)
                except:
                    return data.strip()
