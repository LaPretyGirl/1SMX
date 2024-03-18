from os import system
import random
system("clear")

def penjat(palabra_secreta, letras_correctas):
   # Mostrar el tablero con las letras adivinadas y los espacios en blanco para las letras desconocidas
   tablero = ""
   for letra in palabra_secreta:
       if letra in letras_correctas:
           tablero += letra + " "
       else:
           tablero += "_ "
   return tablero

def joc():
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
    print(penjat(palabra_secreta, letras_correctas))

    while True:
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
                time.sleep(4), system('clear'),llista_cançons()
        else:
            letras_correctas.append(letra)

            if len(letras_correctas) == len(set(palabra_secreta)):
                print("""
¡Felicitats! ¡Has guanyat! La paraula secreta és: {}""".format(palabra_secreta))
                time.sleep(4), system('clear'),joc()

        print("""
Intents restants: {}""".format (intentos_restantes))
        print(penjat(palabra_secreta, letras_correctas))

joc()
