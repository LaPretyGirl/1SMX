def llegir_numero():
    return(int(input("Numeros")))
def escriure_serie():
    suma = 0
    for i in range (a,1,-4):
        suma += i * 2
    print("La suma dels quadrats separats entre si de {} és {}".format(a,suma))                                                            

a = llegir_numero()
escriure_serie(a)