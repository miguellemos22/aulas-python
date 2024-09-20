import os 
os.system("cls || clear ")


numeros_inteiros = 5
contador_pares = 0
contador_impares = 0
contador_positivos = 0
contador_negativos = 0

for i in range(numeros_inteiros):
    numero = int(input(f"digite o {i + 1}º numero: "))
    if numero %2 == 0:
        contador_pares += 1

    else:
        numero %2 == 0
        contador_impares += 1

    if numero > 0:
        contador_positivos += 1

    else:
        numero < 0
        contador_negativos += 1

print("==== mostrando resultados ====")
print(f"quantidade de numeros pares: {contador_pares}")
print(f"quantidade de numeros impares: {contador_impares}")
print(f"quantidade de numeros positivos: {contador_positivos}")
print(f"quantidade de numeros negativos: {contador_negativos}")
