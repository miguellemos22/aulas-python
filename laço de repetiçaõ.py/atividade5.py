import os 
import time
os.system("cls || clear ")
soma = 0
media = 0

for i in range(3):
    notas = float(input(f"digite {i + 1}º nota: "))
    soma = soma + notas
media = media + soma /3

if (media >= 7):
    print("aprovado")
else:
    if notas < 4:
        print("reprovado")
    else:
        print("recuperação")
