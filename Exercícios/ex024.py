# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input("Em que cidade você nasceu? ")).upper().strip()

comecaComSanto = (cidade[:5] == "SANTO")

print(comecaComSanto)
