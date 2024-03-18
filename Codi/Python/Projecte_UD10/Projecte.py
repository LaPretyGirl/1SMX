from os import system
import time 
import random
import Transports as t
import Llibreries as m

def menu_principal():
    system("clear")
    print("""
Menú:
        1. Ordenar nombres.
        2. Llista de cançons.
        3. Penjat.
        4. Informació sobre el transport.
        5. Marvel.
        6. Chat.
        0. Sortir
    """)
    a = input("Elegeix l'opció que vulguis: ")
    return a

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

def llista_cançons():
    system("clear")
    canciones = []
    x = True
    while x: 
        print(""" 


Menú:
        1. Afegir cançons.
        2. Eliminar cançons.
        3. Cambiar informació de les cançons.
        4. Mostrar llista.
        0. Sortir
        """)
        opcio=int(input("""Seleccioni l'opcció que vulgui: """))
        match opcio:
            case 1:
                titulo = input("""
Ingresa el titol de la cançó: """)
                artista = input("""
Ingresa el nom de l'artista o del grup: """)
                cancion = (titulo, artista)
                canciones.append(cancion)
                print("""
¡Cançó afegida amb exit!""")
                print(canciones)
                time.sleep(4), system('clear'),
                        
            case 2:
                if len(canciones) == 0:
                    print("""
La llista de cançons esta buida.""")
                    time.sleep(4), system('clear'),llista_cançons()
                else:
                    titulo = input("""
Ingresa el titol de la cançó que vols eliminar: """)
                    artista = input("""
Ingresa el nom de l'aritsta o del grup: """)
                    cancion = (titulo, artista)
                if cancion in canciones:
                    canciones.remove(cancion)
                    print("""
¡Cançó eliminada amb exit! """)
                    time.sleep(4), system('clear'),llista_cançons()
                else:
                    print("""
La cançó no és troba a la llista.""")
                    time.sleep(4), system('clear'),llista_cançons()
                        
            case 3:
                if len(canciones) == 0:
                    print("""
La llista de cançons esta buida.""")
                    time.sleep(4), system('clear'),llista_cançons()
                else:
                    titulo = input("""
Ingresa el titol de la cançó que vols modificar: """)
                    artista = input("""
Ingresa el nom de l'artista o del grup: """)
                    cancion = (titulo, artista)
                if cancion in canciones:
                    nuevo_titulo = input("""
Ingresa el titol de la cançó: """)
                    nuevo_artista = input("""
Ingresa el nou nom de l'artista o del grup: """)
                    nuevo_cancion = (nuevo_titulo, nuevo_artista)
                    index = canciones.index(cancion)
                    canciones[index] = nuevo_cancion
                    print("""
¡Informació de la cançó modificada amb exit!""")
                    time.sleep(4), system('clear'),llista_cançons()
                else:
                    print("""
La cançó no és troba.""")
                    time.sleep(4), system('clear'),llista_cançons()
                        
            case 4:
                if len(canciones) == 0:
                    print("""
La lista de canciones está vacía.""")
                    time.sleep(4), system('clear'),llista_cançons()
                else:
                    print("""

--- LLISTA DE CANÇONS ---
                    """)
                for i, cancion in enumerate(canciones, start=1):
                    titulo, artista = cancion
                    print("{}. Titol: {} - Artista: {}".format(i, titulo, artista))
            case 0:
                x=False

def tablero_penjat(palabra_secreta, letras_correctas):
   tablero = ""
   for letra in palabra_secreta:
       if letra in letras_correctas:
           tablero += letra + " "
       else:
           tablero += "_ "
   return tablero

def penjat():
    palabras = ["python", "programacio", "joc", "penjat", "ordinador", "lletuga", "electricitat", "pendrive", "tecles", "tomatic", "nispru", "mandarina", "freses", "cireres", "sindria", "melo", "pantalla", "disc", "ruc", "periferic", "funda", "bocata", "estrelles", "boligraf", "verd", "vermell", "lila"]
    palabra_secreta = random.choice(palabras)
    letras_correctas = []
    intentos_restantes = 5

    print("""¡Benvinguts al joc del penjat!

        ----- Normes -----
    - No hi ha accents.
    - No hi ha mayúscules.
    - No hi ha caracters especials.
    """)
    print(tablero_penjat(palabra_secreta, letras_correctas))
    x=True
    while x:
        letra = input("""
Adivina una lletra: """).lower()

        if len(letra) != 1:
            print("""
Per favor, introdueix només una lletra.""")
            continue

        if letra in letras_correctas:
            print("""
Ja has adivinat aquella lletra. """)
            continue

        if letra not in palabra_secreta:
            print("""
La lletra no està a la paraula secreta""")
            intentos_restantes -= 1

            if intentos_restantes == 0:
                print("""
!Has perdut¡ La paraula secreta era: {}.""".format (palabra_secreta))
                time.sleep(4), system('clear')
                x=False
        else:
            letras_correctas.append(letra)

            if len(letras_correctas) == len(set(palabra_secreta)):
                print("""
¡Felicitats! ¡Has guanyat! La paraula secreta és: {}""".format(palabra_secreta))
                time.sleep(4), system('clear')
                x=False
        print("""
Intents restants: {}""".format (intentos_restantes))
        print(tablero_penjat(palabra_secreta, letras_correctas))

def cas1():
    nombres_aleatoris()
    print("""

__________________________________

De qui 10 segons tornaras al menú.""")
    time.sleep(10), system('clear')

def Herencia():
    system("clear") 
    f = [t.Transport("Presentació", 4, "Planeta terra"), t.Coche("Terra", 4, "Carretera"), t.Bus("Terra", 4, "Carretera"), t.Mini_bus("Terra", 4, "Carretera", ["Negre", "Blanc"]), t.Limusina("Terra", 4, "Carretera"), t.Tot_terreny("Terra", 4, "Terra"), t.Vaixell("Navega", "No en te", "Mar"), t.Avió("Vola", 12, "Cel"), t.Nau("Vola i navega", 12, "Cel i mar")]
    for e in f:
        e.presentacio()
        e.moure()
        e.rodes()
        e.lloc()
        if type(e)==t.Mini_bus:
            e.rcolor()
    print("""

_____________________________


De qui 10 segons tornara al menú""")
    time.sleep(10), system('clear'),

def Llibreria():
    system("clear")
    ts=1
    public_key = "74fa62381ab90791437b2c1da6003dfc"
    hash1 = "d92cc884b914834ee8690f75b34e7ac1"
    character_name = "Spider-Man (Peter Parker)"

    personaje = m.obtener_personaje_marvel(ts, public_key, hash1, character_name)
    if personaje:
        for i,e in enumerate(personaje):
            print(e['name'])
            print(e['description'])
            print("""

__________________________________


De qui 10 segons sortiras al menú.""")
            time.sleep(10), system('clear')

    else:
        print("Personaje no encontrado.")
        print("""

__________________________________


De qui 10 segons sortiras al menú.""")        
        time.sleep(10), system('clear')



#Programa Principal

a = True
while a:
    a = menu_principal()
    match a:
        case '0':
            a = False
        case '1':
            system("clear")  
            cas1()
        case '2':
            system("clear")
            llista_cançons()
        case '3':
            system("clear")
            penjat()
        case '4':
            Herencia()
        case '5':
            Llibreria()
        case default:
            print("Opció no valida.")
        