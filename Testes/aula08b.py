from math import sqrt, trunc

numero = int(input("Digite um número: "))

raiz = sqrt(numero)

print("A raiz de {} é igual a {}.".format(numero, trunc(raiz)))