from time import sleep
from components.HDC_1080 import HDC
from components.SHARP_PM10 import SHARP
from components import i2c_lcd

class EMA:
    def __init__(self) -> None:
        self.hdc1080 = HDC()
        self.sharp_pm10 = SHARP()
        self.lcd = i2c_lcd.lcd()

        self.lcd.lcd_clear()
        self.lcd.lcd_display_string(" - - EMA - - ", 1)
        self.lcd.lcd_display_string("OCTA AEROSPACE", 2)
        sleep(5)
        self.lcd.lcd_clear()

    def read(self) -> str:
        message = \
            f"\n[ ! ] Temperatura: {self.hdc1080.HDCtemp(2)} ºC\n" \
            f"[ ! ] Humedad: {self.hdc1080.HDChum(2)} %\n" \
            f"[ ! ] PM10: {self.sharp_pm10.read()}\n"
        self.lcd.lcd_display_string(message)
        return message 

    def start(self) -> dict:
        data = {
            'temperature': self.hdc1080.HDCtemp(1),
            'humidity': self.hdc1080.HDChum(1),
            'pm10': self.sharp_pm10.read()
        }
        print(data["pm10"])
        self.lcd.lcd_clear()
        self.lcd.lcd_display_string(f"TEMP: {data['temperature']} C", 1)
        self.lcd.lcd_display_string(f"HUM: {data['humidity']} %", 2)
        sleep(5)
        self.lcd.lcd_clear()
        self.lcd.lcd_display_string(f"PM10: {data['pm10']} ug/m3", 1)
        sleep(5)
        return data

    def exit(self) -> None:
        self.lcd.lcd_clear()
        self.lcd.lcd_display_string("APAGANDO EMA.", 1)
        self.lcd.lcd_display_string("REINICIO REQUERIDO", 2)
        sleep(2)
        self.lcd.lcd_clear()

