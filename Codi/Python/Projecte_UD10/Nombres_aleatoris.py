
from os import system
system('clear')

def introduccio_ordenar_nombres():
        print("""
Introduzca numeros para ordenarlos.
Una vez hayas acabado de poner los numeros introduzca 'fi'.

            ________________________________
            """)
        
def ordenar_nombres():
    numeros = []
    x = True
    while x:
        a = input("""
Introdueix el nombre: """)
        if a.lower() == 'fi':
            x = False
        try:
            numero = float(a)
            numeros.append(numero)
        except ValueError:
            print("""

Introdueix un nombre, o si has acabat introdueix la paraula 'fi'.
""")

  
    numeros_ordenados = sorted(numeros)
    return numeros_ordenados

def menu_ordenar_nombres():
    print("""
_________________________________________

Menú:
        1. Tornar al programa principal.
        2. Tornar a començar.
    """)
    a = input("Que vols fer: ")
    return a

def cas_1():
    introduccio_ordenar_nombres()
    lista_ordenada = ordenar_nombres()
    system("clear")
    print("Nombres ordenats:", lista_ordenada)
    b = True
    while b:
        b = menu_ordenar_nombres()
        match b:
            case '1':
                system("clear")
                b = False
            case '2':
                system("clear")
                introduccio_ordenar_nombres()
                lista_ordenada = ordenar_nombres()
                system("clear")
                print("Nombres ordenats:", lista_ordenada)