def crear_llista_fitxer(fitxer):
with open(fitxer, 'r') as f:
  	 llista = f.readlines()
lparaules = [linea.rstrip('\n')for linea in llista] 
print(lparaules)
f.close()
		#Pprincipal
		crear_llista_fitxer('/home/professorat/AO/prova.txt')
