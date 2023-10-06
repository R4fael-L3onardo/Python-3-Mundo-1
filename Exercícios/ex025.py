# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input("Qual é seu nome completo? ")).upper().strip()

contemSilva = "SILVA" in nome

print("Seu nome tem Silva? {}".format(contemSilva))
