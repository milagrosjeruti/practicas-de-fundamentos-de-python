credenciales = {"admin": "12345", "invitado":"root"}

user = input("Ingrese su usuario: ")
password = input("Ingrese su contraseña")

if user in credenciales:
    #usuario existe
    intentos = 1
    while True:
        if credenciales[user] == password:
            #acceso correcto
            print("Acceso correcto")
            break
        else:
            #contraseña incorrecta
            intentos += 1
            if intentos <= 3:
                password = input(f"Intento {intentos} de 3. Ingrese su contraseña: ")
            else:
                print("DEmasiados intentos. Pruebe en una hora")
                break

else:
    #usuario no existe
    print("Credenciales invalidos")