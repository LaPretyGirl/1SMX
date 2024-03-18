def llegir():
    a = 'b'
    l = []
    while a !='.':
        a = input("Introdueix un número: ")
        if a!='.':
            l.append(int(a))
    return l
def comparar(a,c):
    for e in a:
        if e > c:
            print(e)
#PP
x = llegir()
y = input("Introdueix el número a comparar: ")
comparar(x,y)
