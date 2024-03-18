from os import system
import time 

def llista_cançons():
    system("clear")
    canciones = []
    x = True
    while (x!="0"): 
        print(""" 


Menú:
        1. Afegir cançons.
        2. Eliminar cançons.
        3. Cambiar informació de les cançons.
        4. Mostrar llista.
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
¡Cançó anyadida amb exit!""")
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