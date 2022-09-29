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
		print("HOST: ", HOST)
		print("DB: ", DB)
		print("USER: ", USER)
		print("PWD: ", PWD)
		
		self.hdc1080 = SDL_Pi_HDC1080.SDL_Pi_HDC1080()
		try:
			self.connection = mysql.connector.connect(
				host=HOST,
				database=DB,
				user=USER,
				password=PWD
			)

		except Error as e:
			print("Error while connecting to MySQL", e)

		finally:
			if (self.connection.is_connected()):
				self.cursor.close()
				self.connection.close()
				print("MySQL connection is closed\n")


	# Getting temperature
	def HDCtemp(self, roundto) -> float:
		temperature = round(self.hdc1080.readTemperature(), roundto)

		if self.connection.is_connected():
			self.cursor = self.connection.cursor()
			self.cursor.execute(f"INSERT INTO HDC1080_TEMP (DATETIME, DATA) VALUES (NOW(), {temperature})")
			self.connection.commit()
			print("Temperature uploaded to database successfully")

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
