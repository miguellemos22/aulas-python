import os 
os.system("cls || clear ")

lista_numeros = []

def verificando_numeros(lista_numeros):
    valor_atualizado = []

    for numero in  lista_numeros:
        if numero < 0:
            numero = 0
        valor_atualizado.append(numero)
    return valor_atualizado
    
for i in range(5):
     numero = float(input(F"digite o {i + 1}º numero: "))
     lista_numeros.append(numero)

lista_numeros = verificando_numeros(lista_numeros)
for numero in lista_numeros:
    print(f"numero: {numero}")