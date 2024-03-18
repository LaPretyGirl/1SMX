def invertir(a):
    b= list(a)
    c=b[::-1]
    r="".join(c)
    return r

a=input("Insereix text: ")
print(invertir(a))