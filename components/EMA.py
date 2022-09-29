import os
from time import sleep
import mysql.connector
from dotenv import load_dotenv
load_dotenv()
#
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
        # sleep(5)
        self.lcd.lcd_clear()

        self.HOST = os.getenv("MYSQL_HOST")
        self.DB = os.getenv("MYSQL_DB")
        self.USER = os.getenv("MYSQL_USER")
        self.PASSW = os.getenv("MYSQL_PWD")

        self.connection = mysql.connector.connect(
            host=self.HOST,
            database=self.DB,
            user=self.USER,
            password=self.PASSW
        )

        if self.connection.is_connected():
            self.cursor = self.connection.cursor()
            self.cursor.execute("SELECT VERSION()")
            self.record = self.cursor.fetchone()
            print(f"Connected to database: {self.record}")


    # def read(self) -> str:
    #     message = \
    #         f"\n[ ! ] Temperatura: {self.hdc1080.HDCtemp(2)} ºC\n" \
    #         f"[ ! ] Humedad: {self.hdc1080.HDChum(2)} %\n" \
    #         f"[ ! ] PM10: {self.sharp_pm10.read()}\n"
    #     self.lcd.lcd_display_string(message)

    #     return message 

    def start(self) -> dict:
        data = {
            'temperature': self.hdc1080.HDCtemp(2),
            'humidity': self.hdc1080.HDChum(2),
            'pm10': self.sharp_pm10.read()
        }
        
        self.cursor.execute(f"""
            INSERT INTO HDC1080 (datetime, temperature, relative_humidity)
            VALUES (NOW(), {data['temperature']}, {data['humidity']})
        """)
        self.cursor.execute(f"INSERT INTO SHARP (datetime, pm10) VALUES (NOW(), {data['pm10']})")
        self.connection.commit()
        print(f"Data inserted into db: {data['temperature']} ºC, {data['humidity']} %, {data['pm10']}")

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

        if (self.connection.is_connected()):
            self.cursor.close()
            self.connection.close()
            print("Database connection closed.")

        sleep(2)
        self.lcd.lcd_clear()

