
class Transport:
	def __init__(self, com_es_mou, per_on_va, quantitat_rodes):
		self.com_es_mou = com_es_mou
		self.per_on_va = per_on_va
		self.quantitat_rodes = quantitat_rodes
	def presentacio(self):
		print("""

Hola, en el següent text, os don informació sobre els tipus de transports que hi ha
	
	""")
	def moure(self):
		pass
	def rodes(self):
		pass
	def lloc(slef):
		pass

class Coche(Transport):
	def presentacio(self):
		print("""
----- COCHE -----

Hola sóc un coche""")
	def moure(self):
		print("Circul per la terra")
	def rodes(self):
		print("Tinc 4 rodes")
	def lloc(self):
		print("I hem moc per la carretera")

class Bus(Transport):
	def presentacio(self):
		print("""
----- BUS -----

Hola sóc un bus""")
	def moure(self):
		print("Circul per la terra")
	def rodes(self):
		print("Tinc entre 4 y 12 rodes")
	def lloc(self):
		print("I hem moc per la carretera")

class Mini_bus(Bus):
	def __init__(self, com_es_mou, quantitat_rodes, per_on_va, color):
		super().__init__(com_es_mou, quantitat_rodes, per_on_va)
		self.color = color
	def presentacio(self):
		print("""
----- MINI BUS -----

Hola sóc un mini bus""")
	def rodes(self):
		print("Tinc 4 rodes")
	def rcolor(self):
		print("El meu color pot ser {} o {} entre molts altres".format(self.color[0], self.color[1]))

class Limusina(Transport):
	def presentacio(self):
		print("""
----- LIMUSINA -----

Hola sóc una limusina""")
	def moure(self):
		print("Circul per la terra")
	def rodes(self):
		print("Tinc entre 4 i 24 rodes")
	def lloc(self):
		print("I hem moc per la carretera")

class Tot_terreny(Transport):
	def presentacio(self):
		print("""
----- TOT TERRENY -----

Hola sóc un tot terreny""")
	def moure(self):
		print("Circul per la terra")
	def rodes(self):
		print("Tinc 4 rodes grans")
	def lloc(self):
		print("I hem moc per la terra")

class Vaixell(Transport):
	def presentacio(self):
		print("""
----- VAIXELL -----

Hola sóc un vaixell""")
	def moure(self):
		print("Naveg per el mar")
	def rodes(self):
		print("No tinc rodes")
	def lloc(self):
		print("I hem moc per la mar")

class Avió(Transport):
	def presentacio(self):
		print("""
----- AVIÓ -----

Hola sóc un avió""")
	def moure(self):
		print("Vol per el cel")
	def rodes(self):
		print("Tinc entre 12 i 32 rodes")
	def lloc(self):
		print("I hem moc pel cel")

class Nau(Avió, Vaixell):
	def presentacio(self):
		print("""
----- NAU -----

Hola sóc un avió, que pot navegar""")
	def moure(self):
		print("Vol pel cel i naveg per el mar")
	def rodes(self):
		print("Tinc 12 rodes")
	def lloc(self):
		print("I hem moc tant pel cel com per la mar")

