import os
from components.EMA import EMA

def write_error(e):
    with open("/home/pi/errors.txt", "a+") as file:
        file.write("{}\n".format(e))

if __name__ == "__main__":
    ema = EMA()
    while True:
        try:
            ema.start()
        except Exception as e:
            write_error(e)
            # os.system("sudo reboot")

