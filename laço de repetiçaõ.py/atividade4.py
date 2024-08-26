import os 
import time
os.system("cls || clear ")
soma = 0
media = 0

for i in range(4):
    notas = float(input(f"digite {i + 1}º nota: "))

soma = soma + notas
media = media + notas

print(f"media: {media}")