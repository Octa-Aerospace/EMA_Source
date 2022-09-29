# import os
from components.EMA import EMA

if __name__ == "__main__":
    ema = EMA()
    while True:
        try:
            ema.start()
        except KeyboardInterrupt:
            ema.exit()
            print("\n")
            break
            # os.system("sudo poweroff")

        except Exception as e:
            print(e)
            # os.system("sudo reboot")

