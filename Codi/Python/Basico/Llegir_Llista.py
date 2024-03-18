# 1. Llegir una llista d'elements, en el nostre cas enters.
def llegir_llista():
    l=[]
    for i in range(10): # Feim un bucle de 10 elements
        l.append(input())   # Append = Afegir al final de la llista       
                            # Input = Llegim del teclat
                            # Input = Sempre retorna una cadena de caracter 
    return l

# 2. Sumar elements
    # PP = Programa Principal

x=llegir_llista()
suma=0
for e in x:
    suma += int(e)  # int = ho pasa a nombre (compta els caractes)
print("La suma és: " ,suma,"")