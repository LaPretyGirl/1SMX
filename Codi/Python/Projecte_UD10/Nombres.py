import random
from os import system

def nombres_aleatoris():
    system("clear")
    inici = int(input("""
Ingresa nombre minim aleatori: """))
    fi = int(input("""
Ingresa nombre màxim aleatori: """))
    
    quantitat = int(input("""
Indica la quantitat de nombres aleatoris que vols: """))
    
    nombres = []
    for _ in range(quantitat):
        nombres.append(random.randint(inici, fi))  
    
    print("""

----- Nombres generats aleatoriament ----- 
""")
    print(nombres)
    
    nombres_ordenats = sorted(nombres)
    print("""

----- Nombres ordenats ----- 
""")
    print(nombres_ordenats)
    
    return nombres_ordenats

nombres_aleatoris()

