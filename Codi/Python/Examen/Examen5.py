def llegir():
    a = 'b'
    l = []
    while a !='.':
        a = input("Introdueix una paraula: ")
        if a!='.':
            l.append(int(a))
    return l

#PP
x = llegir()
a = input("Introdueixi la longitud màxima de les paraules a mostrar: ")
for e in x:
    if len(e)>a:
        print(e)