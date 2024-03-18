# Definición de funciones 
def gran_de_tres(x,y,z):
    a=x
    if(x>y):
        if(x>z):
            a = x
        elif (z>x):
            a = z
        else:
            a = x
    elif (y>x):
        if (y>z):
            a = y
        elif (z>y):
            a = z
        else:
            a = y
    else:
        if (x>z):
            a = x
        elif (z>x):
            a = z
        else: 
            a = x
    return a 

# Aplicación principal
a = int(input("Escriure el primer valor: "))
b = int(input("Escriure el segon valor: "))
c = int(input("Escriure el tercer valor: "))
d = gran_de_tres(a,b,c)
print("El mayor de ", a, ", ",b, ", ",c," es ", d)
