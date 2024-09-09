import os 
os.system("cls || clear ")

quantidade_de_notas = 3
contador = 0
soma = 0

for i in range(quantidade_de_notas):
    nota = float(input("digite sua nota: "))
    contador += 1
    soma += nota

def media(n1, contador):
    media = soma / 3

    return media

resultado = media(soma, contador)
print(f"media: {resultado}")

