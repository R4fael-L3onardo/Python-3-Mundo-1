# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

nome = str(input("Digite seu nome completo: ")).strip()
print("Analisando seu nome ...")

maiusculas = nome.upper()

minusculas = nome.lower()

letrasAoTodo = len(nome) - nome.count(" ")

primeiroNome = nome.split()[0]
letrasPrimeiroNome = len(primeiroNome)

print("Seu nome em maiúsculas é {}.".format(maiusculas))
print("Seu nome em minúsculas é {}.".format(minusculas))
print("Seu nome tem ao todo {} letras.".format(letrasAoTodo))
print("Seu primeiro nome é {} e ele tem {} letras.".format(primeiroNome, letrasPrimeiroNome))
