texto = input('introduce un titulo  \n')
nombre_fichero = 'archivo-' + texto + '.txt'
f = open(nombre_fichero, 'w') #apertura w= write, r = read, a = appen
mensaje = input('ingrese un texto o alguna palabra \n')
f.write(f'{mensaje}\n')
f.close()