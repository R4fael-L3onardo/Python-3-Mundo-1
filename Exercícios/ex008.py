# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e 
# milimetros.

distancia = float(input("Digite uma distância em metros: "))

print("A medida de {:.1f}m corresponde a".format(distancia))
print("{}km".format(distancia / 1000 ))
print("{}hm".format(distancia / 100))
print("{}dam".format(distancia / 10))
print("{:.0f}dm".format(distancia * 10))
print("{:.0f}cm".format(distancia * 100))
print("{:.0f}mm".format(distancia * 1000))
