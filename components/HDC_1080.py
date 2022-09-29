import os, sys
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
load_dotenv()
#
from components import SDL_Pi_HDC1080


HOST = os.getenv("HOST")
DB = os.getenv("DB")
USER = os.getenv("USER")
PWD = os.getenv("PWD")

# Setting main path to HDC1080
class HDC:
	def __init__(self) -> None:
		sys.path.append('./SDL_Pi_HDC1080_Python3')
		self.hdc1080 = SDL_Pi_HDC1080.SDL_Pi_HDC1080()


	# Getting temperature
	def HDCtemp(self, roundto) -> float:
		temperature = round(self.hdc1080.readTemperature(), roundto)

		try:
			connection = mysql.connector.connect(
				host=HOST,
				database=DB,
				user=USER,
				password=PWD
			)

			if connection.is_connected():
				cursor = connection.cursor()
				cursor.execute(f"INSERT INTO HDC1080_TEMP (DATETIME, DATA) VALUES (NOW(), {temperature})")
				connection.commit()
				print("Temperature uploaded to database successfully")

		except Error as e:
			print("Error while connecting to MySQL", e)

		finally:
			if (connection.is_connected()):
				cursor.close()
				connection.close()
				print("MySQL connection is closed\n")

			return temperature

	# Getting humidity
	def HDChum(self, roundto) -> float:
		humidity = round(self.hdc1080.readHumidity(), roundto)
		return humidity

if __name__ == "__main__":
	hdc = HDC()
	message = \
		f"\n[ ! ] Temperatura: {hdc.HDCtemp(2)} ºC\n" \
		f"[ ! ] Humedad: {hdc.HDChum(2)} %\n"
	print(message)
