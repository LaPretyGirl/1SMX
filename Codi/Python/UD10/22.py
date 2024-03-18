def gran_llista(a):
    b=[]
    for e in a:
        b.append(e)
    b.sort()
    return b[::-1]

# Programa principal 
a = [1684, 9481, 314, 5, 695841, 698514,]
c = gran_llista(a)
print(c[0])
