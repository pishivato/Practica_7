from angryB import *


Birds = []
blue = Blue("Blue", "Azul", "150M", "Mediano", "12.5 mts")
Birds.append(blue)
chuck = Chuck("Chuck", "Amarillo", "120M", "Chico", "15.5 mts")
Birds.append(chuck)
black = Black("Black", "Negro", "200M", "Grande", "10 mts")
Birds.append(black)



while True:
    print("Que Angry Bird, quiere ver?: \n")
    print("(1)-> Bird_1\n")
    print("(2)-> Bird_2\n")
    print("(3)-> Bird_3\n")
    print("(4)-> Salir\n")
    op = int(input("Elige una opcion: \n"))

    if op == 1:
        print(f"Nombre: {Birds[0]._getNombre()}\n")
        print("Ataque:\n")
        Birds[0].Ataque()
    elif op == 2:
        print(f"Nombre: {Birds[1]._getNombre()}\n")
        print("Ataque:\n")
        Birds[1].Ataque()
    elif op == 3:
        print(f"Nombre: {Birds[2]._getNombre()}\n")
        print("Ataque:\n")
        Birds[2].Ataque()
    elif op == 4:
        break

