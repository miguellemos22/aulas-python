import os 
os.system("cls || clear ")

valor_numeros = []
quantidade_de_numeros = 5

for i in range(quantidade_de_numeros):
    numero = float(input(F"digite o {i + 1}º numero: "))
    if numero <= 0:
        numero = 0
    valor_numeros.append(numero)

for numero in valor_numeros:
    print(f"numero: {numero}")