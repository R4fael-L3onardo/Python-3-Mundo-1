numero1 = int(input("Um valor: "))
numero2 = int(input("Outro valor: "))

soma = numero1 + numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2
divisaoInteira = numero1 // numero2
exponenciacao = numero1 ** numero2

print("A soma é {}, o produto é {} e a divisão é {:.3f}.".format(soma, multiplicacao, divisao))
print("Divisão inteira {} e potência {}.".format(divisaoInteira, exponenciacao))
