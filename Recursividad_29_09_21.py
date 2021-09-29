print("Tarea Recursividad")
print("Gonzalo Martinez Gil, Guillermo Josue Martinez Navarrete")

def cuadrado(numero):
    numerado = 1
    if numerado <= numero:
        numerado = numero * numero
    return numerado
a = int(input("Escriba el numero base: "))
print(f"El resultado al cuadrarlo es: {cuadrado(a)}")

def cubico(numero):
    numerado = 1
    if numerado <= numero:
        numerado = numero * numero * numero
    return numerado
print(f"El resultado al combertirlo al cubico es: {cubico(a)}")




def sumarNumeros(numeros):
    if len (numeros) == 0:
        return 0 
    else:
        return numeros[0] + sumarNumeros(numeros[1:])
valores=[cuadrado(a), cubico(a)]
fin = sumarNumeros(valores)
print("El resultado final despues de sumar el resultado cuadrado y el resultado cubico es: ", fin)



def invertir_numero(n):
    numero = 0
    while n != 0:
        numero = 10*numero+n % 10
        n //= 10
    return numero

numero = fin
numero_invertido = invertir_numero(numero)
print("Se toma el resultado anterior: ")
print(numero)
print("El resultado al invertirse es: ")
print(numero_invertido)



suma, numero = 0, 0

serie_de_numeros = numero_invertido

while serie_de_numeros != 0:
    numero = serie_de_numeros % 10
    serie_de_numeros = serie_de_numeros // 10
    suma = suma + numero

print("Suma de la serie del resultado anterior: ")
print("{}".format(suma))

def fibonacci(n):
    x, y = 0,1
    while x < n:
        print(x, end=" ")
        x, y = y, x + y

print("El finbonaci del resultado anterior es: ", )
fibonacci(suma)




