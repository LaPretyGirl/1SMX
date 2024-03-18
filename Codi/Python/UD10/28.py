def mostrar_majors_que(t,nreferencia):
	print("Tots els números majors de {} són: ".format(nreferencia))
	for e in t:
		if e>nreferencia:
			print("{} ".format(e))
       	 
def llegir_tupla():
	a = []
	i=0
	print("Introdueixi tots els números que vulguis. Per aturar posi -1: ")
	while i>-1:
	    c =input("Introdueixi un número: ") 
	    if a[i]!="-1":
        	a.append("-1")
        	i=-2
    	i +=1
	return a

#Programa principal
i = input("Introdueixi el número que voleu comparar: ")
x = llegir_tupla()
a = tuple(x)
mostrar_majors_que(a, i)
