import os 
os.system("cls || clear ")

lista_pares_positivos = []
quantidade = 3

for i in range(quantidade):
    while True:
        numero = int(input("digite um numero: "))
        if numero %2 == 0 and numero > 0:
            lista_pares_positivos.append(numero)
            break
        else:
            print("numero invalido, tente novamente")

for numero in reversed (lista_pares_positivos):
    print(numero)


    