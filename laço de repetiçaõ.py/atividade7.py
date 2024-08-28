import os 
import time
os.system("cls || clear ")

nota = float(input("digite sua nota: "))

while nota < 0 or nota > 10:
    print("a nota deve ser maior que 0 e menor que 10")
    nota = float(input("digite sua nota: "))

print(f"nota: {nota}")


