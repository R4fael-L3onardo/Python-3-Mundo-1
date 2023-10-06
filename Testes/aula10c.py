nota1 = float(input("Digite a primeiro nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

print("A sua média foi {:.1f}".format(media))

if media >= 6.0:
    print("A sua média foi boa! Parabéns!")
else:
    print("A sua média foi ruim! Estude Mais!")
