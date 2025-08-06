class Calculadora:
#atributos
    numero1 = None
    numero2 = None
    resultado = None
#contructor
    def __init__(self, n1=0, n2=0):
        self.numero1 = n1
        self.numero2 = n2
        self.resultado = 0
#metodos
    def sumar(self):
        self.resultado = self.numero1 + self.numero2
        return self.resultado
    def restar(self):
        self.resultado = self.numero1 - self.numero2
        return self.resultado    
    def multplicacion(self):
        self.resultado = self.numero1 * self.numero2
        return self.resultado
    
    def division(self):
        self.resultado = self.numero1 / self.numero2
        return self.resultado
    
    def getResultado(self):
        return self.resultado
    
class CalculadoraCientifica(Calculadora):
    def __init__(self, n1, n2):
        super().__init__(n1, n2)

    def factorial(self, num):
        if(num <= 1):
            return 1
        else:
            return num * self.factorial(num -1)
        #sobreEscribir, override, polimorfismo
    def getResultado(self):
        return f"Operacion anterior: {self.resultado}"

class CalculadoraProgramador(Calculadora):
        def __init__(self, x, y):
            super().__init__(x, y)

        def decimalToBinario(self, num):
            digitoString = ""
            while(num >= 2):
                c = int(num / 2)
                r = num % 2
                num = c
                digitoString = str(r) + digitoString
            digitoString = str(num) + digitoString
            return digitoString


if __name__ == "__main__" :
    casio = Calculadora()
    casio.numero1 = 10
    casio.numero2 = 5
    print(f"La Suma de 10 + 5 es : {casio.sumar()}")
    print(f"Resultado. {casio.resultado}")
    print(f"La resta de 10 - 5 es : {casio.restar()}")
    print(f"Resultado. {casio.resultado}")
    print(f"La multiplicacion de 10 * 5 es : {casio.multplicacion()}")
    print(f"Resultado. {casio.resultado}")
    print(f"La division de 10 / 5 es : {casio.division()}")
    print(f"Resultado. {casio.resultado}")

    hp = CalculadoraCientifica(20,8)
    print(f"La Suma con CC de ... es {hp.sumar()}")
    print(f"Resultado. {hp.resultado}")
    print(f"Factorial de 5:  {hp.factorial(5)}")
    print(f"Resultado. {hp.resultado}")

    cp = CalculadoraProgramador(2,5)
    decimal = int(input("Ingrese un decimal a convertir: "))
    print(f"El binario de {decimal} es:  " + cp.decimalToBinario(decimal))
    print(f"Resultado. {cp.resultado}")