def invertir(a):
    b= list(a)
    c=b[::-1]
    r="".join(c)
    return r
def palindrom(a):
    c = invertir(a)
    x = 0 
    for i in range(len(a)):
        if a[i] != c[i]:
            x+=1
    if x == 0:
        return True
    else:
        return False
    
# PP
a = input("Introdueix un text: ")
if palindrom(a):
    print("És palindrom")
else:
    print("No és palindrom")