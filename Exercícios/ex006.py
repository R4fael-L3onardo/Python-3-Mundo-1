# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

numero = float(input("Digite um número: "))

dobro = numero * 2
triplo = numero * 3
raizQuadrada = numero ** 0.5

print("O dobro vale {}".format(dobro))
print("O triplo vale {}".format(triplo))
print("A raiz quadrada de {} é igual a {:.2f}".format(numero, raizQuadrada))
