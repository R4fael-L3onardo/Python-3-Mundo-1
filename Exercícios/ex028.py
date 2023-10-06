# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça 
# para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

print("vou pensar em um núemro entre 0 e 5. Tente adivinhar...")
numero = int(input("Em que número eu pensei? "))
print("PROCESSANDO...")
sleep(3)

numeroSorteado = randint(0, 5)

if numero == numeroSorteado:
    print("Parabéns! Você conseguiu me vencer!")
else:
    print("Ganhei! Eu pensei no número {} e não no {}!".format(numeroSorteado, numero))
