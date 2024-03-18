def paraula_mes_gran(a):
	sorted(a,key=lambda a:len(a))
	return a[len(a)-1]

# Programa principal
x = ["Hey" , "Esternocleidomastoideo" , "Electromagnetisme" , "Supercalifràgilisticuespialidoso"]
print("La paraula més llarga és: ", paraula_mes_gran(x))
