import os 
import time
os.system("cls || clear ")

while True:
    nota = float(input("digite sua nota: "))

    if nota < 0 or nota > 10:
        print("\nA nota deve ser maior ou igaul a 0 e menor e igual a 10.")
    else:
        break # para o laço de repetição. 

print(f"nota: {nota}")

