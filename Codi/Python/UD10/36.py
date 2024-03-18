def llegir_numero():
    return (int(input("Introdueix un valor: ")))
def llegir_numero_float():
    return(float(input("Introdueix un valor real: ")))
def Calcular_prestec (q,i,a):
    return (q*(1+i/100)**a)

q = llegir_numero()
i = llegir_numero_float()
a = llegir_numero()
c = Calcular_prestec(q,i,a)
print(" Si sol·licitud {} a un interés anual del {} a {} anys, al final pagaré {} euros".format(q,i,a,c))