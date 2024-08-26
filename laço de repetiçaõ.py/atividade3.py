import os 
import time
os.system("cls || clear ")

pares = 0
impares = 0

for i in range(5):
    numero = int(input(f"digite {i + 1}º numero: "))
    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

time.sleep(0.5)

print(f"pares: {pares}")
print(f"impares: {impares}")
