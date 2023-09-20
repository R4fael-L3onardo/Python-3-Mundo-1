# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área 
# e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta 
# uma área de 2m².

largura = float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))

areaParede = largura * altura
tintaParede = areaParede / 2

print("Sua parede tem a dimensão de {} x {} e a sua aréa é de {:.3f}m².".format(largura, altura, areaParede))
print("Para pintar essa parede, você precisará de {}L de tinta.".format(tintaParede))
