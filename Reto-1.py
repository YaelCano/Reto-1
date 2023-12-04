import math
# Reto 1: Fibonacci
# Los números de Fibonacci 𝐹𝐾 son una sucesión de números naturales definidos de la siguiente manera:
# En palabras simples, la sucesión de Fibonacci comienza con 0 y 1, y los siguientes términos siempre son la suma de los dos anteriores.
# En la siguiente tabla, podemos ver los números de Fibonacci desde el 0-ésimo hasta el duodécimo.
#  N = 0 1 2 3 4 5 6 7 8 9 10 11 12
#  F(N) = 0 1 1 2 3 5 8 13 21 34 55 89 144


# 1.Escriba un programa que reciba como entrada un número entero n, y entregue como salida el n-ésimo número de Fibonacci:
def fibonacci_con_bucle(n):
    fib = [0,1]
    for i in range(2, n + 1):
        fib.append(fib[i -1] + fib[i - 2])
    return fib
n = int(input("Elije el numero de Fibonacci: "))
arreglo =  fibonacci_con_bucle(n)
print(arreglo[n])
# 2. Escriba un programa que reciba como entrada un número entero e indique si es o no un número de Fibonacci:
def fibonacci_confirmacion(x):
    fib = [0,1]
    num = 2
    while True:
        num += 1
        fib.append(fib[-1]+ fib[-2])
        if fib[-1]== x:
            return fib
            break
        if fib[-1] > x:
            return False
x = int(input("Digita el numero: "))
bool_result = fibonacci_confirmacion(x)
print(bool_result)

if bool_result:
    print(f"{x} Si es un numero de fibonacci")
else:
    print(f"{x} No es un numero de fibonacci")    


# 3. Escriba un programa que muestres los m primeros números de Fibonacci, donde m es un número ingresado por el usuario:
def fibonacci_numericos(g):
    fib = [0,1]

    for i in range(2, g):
        fib.append(fib[i - 1] + fib[i -2])
    return fib
consecutivo = int(input("Digita el numero: "))
print(fibonacci_numericos(consecutivo))



