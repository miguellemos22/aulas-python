import os
os.system("cls || clear")

quantidade_numeros = 6
lista_pares_positivos = []

def solicitar_dados():
    for i in  range(quantidade_numeros):
        while True:
            numero = int(input(f"digite o {i + 1}º numero: "))
            if numero % 2 == 0 and numero > 0:
                lista_pares_positivos.append(numero)
                break
            else:
                print("numero invalido. /nTente novamente. /n/n")
    return lista_pares_positivos

lista_numeros = solicitar_dados()
for i,numero in enumerate(reversed(lista_pares_positivos)):
    print(f"{len(lista_pares_positivos) -i}º - {numero}")
    