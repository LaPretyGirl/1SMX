# Definición de longitud
def longitut(a):
    contador=0
    for i in a:
        contador+=1
    return contador

# Programa principal
b=[1,"a",[3,4],5,6]
print(longitut(b))
