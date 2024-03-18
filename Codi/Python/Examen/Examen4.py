def menu():
    print(""""
    Calculadora de números enters:
    1. Sumar
    2. Restar
    3. Multiplicar
    4. Dividir
    5. Potència
    0. Sortir
    """)
    x = input("Introdueixi l'opció desitjada")
    return int(x)

def llegir_valors():
    a = input("Introdueix el primer valor: ")
    b = input("Introdueix el segon valor: ")
    return int(a), int(b)

#PP
opcio = 10
while opcio!=0:
    opcio = menu()
    if opcio!=0:
        match opcio:
            case 1:
                a,b = llegir_valors()
                c = a + b
                print("La suma de {} i {} és {}".format(a, b, c))
            case 2:
                a,b = llegir_valors()
                c = a - b
                print("La resta de {} i {} és {}".format(a, b, c))
            case 3:
                a,b = llegir_valors()
                c = a * b
                print("La multiplicació de {} i {} és {}".format(a, b, c))
            case 4:
                a,b = llegir_valors()
                c = a / b
                print("La divisió de {} i {} és {}".format(a, b, c))
            case 5:
                a,b = llegir_valors()
                c = a ** b
                print("La potència de {} i {} és {}".format(a, b, c))
            case other:
                print("Opció no vàlida")