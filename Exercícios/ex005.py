# Faça um programa que leia um número inteiro e mostre na tela seu sucessor e seu antecessor.

numero = int(input("Digite um número: "))

antecessor = numero - 1
sucessor = numero + 1

print("Analisando o valor {}, seu antecessor é {} e o sucessor é {}.".format(numero, antecessor, sucessor))
