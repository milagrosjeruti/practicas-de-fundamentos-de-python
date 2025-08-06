# operadores aritmeticos
#imprimir la suma de 3 + 4
print("la suma de 10 + 4 es: ", 10 + 4)

#resolver todas las operaciones: 10-4, 10*4, 10%4, 10//4, 10**4
print("el resta de 10-4 es:", 10-4)
print("la multiplicacion de  10*4 es:", 10*4)
print("el modulo de 10%4 es:", 10%4)
print("la division entera de 10//4 es:", 10//4)
print("la potencia de 10**4 es:", 10**4)

#resolver la ecuacion cuadratica: 2x²-7x+3 = 0
import math

a = 2
b = -7
c = 3

# Calculamos el discriminante
discriminante = b**2 - 4*a*c

# Verificamos si hay soluciones reales
if discriminante >= 0:
    # Calculamos las dos soluciones
    x1 = (-b + math.sqrt(discriminante)) / (2*a)
    x2 = (-b - math.sqrt(discriminante)) / (2*a)
    print(f"Las soluciones son: x1 = {x1}, x2 = {x2}")
else:
    print("La ecuación no tiene soluciones reales.")
#operaciones con cadenas de texto
print("SNPP " + "CTFPPJ " + "PROGRAMACION PYTHON")
print("AULA " + "2102") 

# Operaciones mixtas
print("Tun chi " * 5)
print("Ja " * (2 ** 3))

#operadores de comparacion 
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)

# operaciones con cadenas de texto
print("python" > "PYTHON")
print("aaa" >= "abaa") #ordenacion alfabetica por ASCII
print(len("aaaa") >= len("abaa")) #cuenta caracteres

print("python" != "PYTHON")

### OPERACIONES LOGICOS

print(10 > 4 and "Z" > "A")
print(10 > 4 or "Z" > "A")
print(not(10 > 4) and "Z" > "A")