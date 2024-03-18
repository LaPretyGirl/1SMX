def any_traspas(any):
	if (any % 4==0) and (any%100>0 or any%400==0):
    		print("L'any {} és de traspàs".format(any))
	else:
    		print("L'any {} no és de traspàs".format(any))
    
#Programa principal
a = input("Indiqui un any amb 4 xifres (aaaa): ")
any_traspas(int(a))
