def llegir():
    l=[]
    a='a'
    while(a!='.'):
        a=input("Posa el nom: ")
        if a!='.':
            l.append(a)
    return l

def ncp(l,c):
    p=[]
    x=0
    for e in l:
        if e[0]==c:
            x +=1
            p.append(e)
    print("El numero de paraules que comencen per {} són {} i són {}".format (c,x,p))

## PP
a=llegir()
c=input("Introdueix el caracter que voleu cercar ")
ncp(a,c)