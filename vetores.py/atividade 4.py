import os 
os.system("cls || clear ")

lista_numeros = []

for i in range(5):
    numero = float(input(f"digite o {i + 1}º numero: "))
    lista_numeros.append(numero)

maior_numero = max(lista_numeros)
menor_numero = min(lista_numeros)

print(f"maior: {maior_numero}")
print(f"menor: {menor_numero}")