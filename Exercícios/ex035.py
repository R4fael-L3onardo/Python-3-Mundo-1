# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas 
# podem ou não formar um triângulo.

print("-------------------------------")
print("   Analisador de Triângulos    ")
print("-------------------------------")

primeiro = float(input("Primeiro segmento: "))
segundo = float(input("Segundo segmento: "))
terceiro = float(input("Terceiro segmento: "))

if (primeiro + segundo) > terceiro and (primeiro + terceiro) > segundo and (terceiro + segundo) > primeiro:
    print("Os segmentos acima Podem Formar um triângulo!")
else:
    print("Os segmentos acima Não Podem Formar um triângulo!")
