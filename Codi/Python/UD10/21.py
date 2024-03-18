def menu():
    print("""
    Menu:
        1. Dibuix 1
        2. Dibuix 2
        3. Dibuix 3
        4. Sortir
    """)
    opcio=input("Seleccioni el dibuix que vulguis: ")
    return opcio

def crear_punts(a):
    match a:
        case "1":
            print("""  .  
             . . 
             .   .
              . . 
                .  
            """)
        case "2":
            print(""" __
            | | |
             _ _ 
             | | |
             _ _ 
            """)
        case "3":
            print("""
            +-+
            -+-
            +-+
            """)
        case other:
            print("Adeu")

opcio=2
while(opcio!=0):
    opcio = menu()
    crear_punts(opcio)
print("Adeu, ja hem acabat")