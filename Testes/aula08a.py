import math

numero = int(input("Digite um número: "))

raiz = math.sqrt(numero)

print("A raiz de {} é igual a {}.".format(numero, math.trunc(raiz)))