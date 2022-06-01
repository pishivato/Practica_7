
class Bird:

	def __init__(self, Nombre=None, Color=None, Poder=None, Tamano=None, Distancia=None):
		self.Nombre = Nombre
		self.Color = Color
		self.Poder = Poder
		self.Tamano = Tamano
		self.Distancia = Distancia
		

class Blue(Bird):

	def _getNombre(self):
		return self.Nombre

	def Ataque(self):
		print(f"{self.Nombre} ataco y se dividio en 3 <...> \n")

class Chuck(Bird):

	def _getNombre(self):
		return self.Nombre

	def Ataque(self):
		print(f"{self.Nombre} ataco y aumento su velocidad!!! \n") 

class Black(Bird):
	
	def _getNombre(self):
		return self.Nombre

	def Ataque(self):
		print(f"{self.Nombre} ataco y exploto! \n")


