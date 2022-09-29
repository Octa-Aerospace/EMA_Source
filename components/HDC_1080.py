import sys
from components import SDL_Pi_HDC1080

# Setting main path to HDC1080
class HDC:
	def __init__(self) -> None:
		sys.path.append('./SDL_Pi_HDC1080_Python3')
		self.hdc1080 = SDL_Pi_HDC1080.SDL_Pi_HDC1080()

	# Getting temperature
	def HDCtemp(self, roundto) -> float:
		temperature = round(self.hdc1080.readTemperature(), roundto)

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
