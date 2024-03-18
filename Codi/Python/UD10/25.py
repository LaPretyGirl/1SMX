def num_majuscules(s):
	mayúscules = sum(c.isupper() for c in s)
	minuscules = sum(c.islower() for c in s)
	numeros	= sum(c.isdigit() for c in s)
	caracters_especials = len(s)-(mayúscules+minuscules+numeros)
	return mayúscules, minuscules, numeros, caracters_especials;
    
# Programa principal
a = input("Indicar una paraula o una cadena de paraules: ")
nMaj, nMin, nNum, NCE = num_majuscules(a)
print("La paraula o cadena introduïda: ", a, " té:\n",
	nMaj, " Majúscules \n",
	nMin, " Minúscules \n",
	nNum,  "Números \n",
	NCE, " Caràcters especials")