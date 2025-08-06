usuarios = {'mili':'7374810', 'Denisse':'1234', 'Ernesto':'3210'}

intentos = 0
Max_intentos = 3

usuario = input("Ingrese su usuario: \n ")

while (intentos < Max_intentos ):
    Password = input("su contraseña es: \n")


    if usuario in usuarios:
        if usuarios[usuario] == Password:
            print("¡Acceso concedido✅🎉!")
            break
        else:
            print("Contraseña incorrecta.🤨")
            intentos = intentos + 1
    else:
        print("Usuario no encontrado.(┬┬﹏┬┬)")
        intentos = intentos + 1

if intentos == Max_intentos:
    print("Has superado el número máximo de intentos. Acceso bloqueado.😠(HECKER❌)")