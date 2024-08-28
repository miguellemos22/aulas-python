
import os 
import time
os.system("cls || clear ")
soma = 0
quantidadesdenotas = 2


for i in range(quantidadesdenotas):
    while True:
        notas = float(input(f"digite sua nota: "))

        if notas >= 0 and notas <= 10:
            break 
    soma += notas

media = soma / quantidadesdenotas


print(f"media: {media}")