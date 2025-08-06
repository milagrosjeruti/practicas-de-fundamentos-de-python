import os

while True:
    os.system("cls")
    print("1. Calculadora")
    print("2. chrome")
    print("0. Salir")
    opcion = input("Opcion:")
    if (opcion == "1" ):
        os.system("calc")
    elif (opcion == "2" ):
        os.system("start chrome")
    elif (opcion == "0" ):
        break
    else:
        print("????")
        input("nellll, si desea continuar presione enter")