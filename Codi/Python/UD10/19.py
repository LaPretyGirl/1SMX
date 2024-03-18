def crear_repetits(a,b):
    c = b*int(a)
    return c

# PP
x = input("Introdueix numero de repeticions: ")
y = input("Introdueix un caracter a repetir: ")
print ("El caracter ", y, " repetit ",x,"-vegades, és: ", crear_repetits(x,y))