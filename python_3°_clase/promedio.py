
#promedio de calificacion
calif = 1
sumatoria =0 
contador = 0
while (calif != 0):
    calif = int(input("Ingrese calificacion: "))
    if (calif != 0):
        if (calif >= 1 and calif <= 5):
            sumatoria = sumatoria + calif
            contador = contador + 1
        else:
            print("dato invalido")    



print("__---__________------------____________-------")
print(f"promedio general: {sumatoria / contador}")
