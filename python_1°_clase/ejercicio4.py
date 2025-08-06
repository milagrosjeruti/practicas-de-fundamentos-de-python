### Strings o cadenas de textos

nombre = "milagros jeruti "
apellido = 'Dure Nuñez'

print(nombre + " " + apellido)

texto = "este texto \n tiene salto de linea y \t tabulacion"
print(texto)

#formateo

user, password, email = "moios", 12345, "admin@admin.com"
print("su usuario y contraseña son {} {} y su email {}".format(user, password, email))
print("su usuario y contraseña son %s %d y su email %s" % (user, password, email))
print("su usuario y contraseña son " + user + " " + str(password) + " y su email " + email )
print(f"su usuario y contraseña son {user} {password} y email {email} ")
