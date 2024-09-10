import os 
os.system("cls || clear ")

lista_numeros = []
soma = 0
positivo = 0
negativo = 0

for i in range(10):
    numeros = float(input("digite um numero: "))
    lista_numeros.append(numeros)
    if numeros >= 0:
        positivo += 1
        soma += numeros
    else:
        negativo += 1
    
for i, numero in enumerate(lista_numeros):
    print(f"{i + 1}ºnumero:{numero}")
print(f"soma dos numeros positivos: {soma}")
print(f"quantidade positivos: {positivo}")
print(f"quantidade negativos: {negativo}")
    