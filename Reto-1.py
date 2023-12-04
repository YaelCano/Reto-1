# Reto 1: Fibonacci
# Los números de Fibonacci 𝐹𝐾 son una sucesión de números naturales definidos de la siguiente manera:
# En palabras simples, la sucesión de Fibonacci comienza con 0 y 1, y los siguientes términos siempre son la suma de los dos anteriores.
# En la siguiente tabla, podemos ver los números de Fibonacci desde el 0-ésimo hasta el duodécimo.
#  N = 0 1 2 3 4 5 6 7 8 9 10 11 12
#  F(N) = 0 1 1 2 3 5 8 13 21 34 55 89 144


# 1.Escriba un programa que reciba como entrada un número entero n, y entregue como salida el n-ésimo número de Fibonacci:
N = 0,1,2,3,4,5,6,7,8,9,10,11,12
F = 0,1,1,2,3,5,8,13,21,34,55,89
def fibonacci(n):
    if n == 0:
        return F[0]
    elif n == 1:
        return F[1]
    else:
        for i in range (len(F)):
            if n == i+2:
                return F[i+1]
            fibonacci(10)
            fibonacci(11)
            fibonacci(12)
            fibonacci(0)
print                 







