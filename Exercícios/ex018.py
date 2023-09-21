# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e 
# tangente desse ângulo.

import math

angulo = float(input("Digite o ângulo que você deseja: "))

radiano = math.radians(angulo)
seno = math.sin(radiano)
cosseno = math.cos(radiano)
tangente = math.tan(radiano)

print("O ângulo de {} tem o SENO de {:.2f}".format(angulo, round(seno, 2)))
print("O ângulo de {} tem o COSSENO de {:.2f}".format(angulo, round(cosseno, 2)))
print("O ângulo de {} tem o TANGENTE de {:.2f}".format(angulo, round(tangente, 2)))
