import os 
os.system("cls || clear ")

def mostrar_tabuada(numero):
    for i in range(1,11):
        print(f"{numero} x {i} = {numero * i }")


numero = int(input("digite um numero: "))


mostrar_tabuada(numero)




