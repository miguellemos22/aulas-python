import os 
os.system("cls || clear ")

numero = 0

def impar_par(numero):
    if numero % 2 == 0:
        return print(f"{numero} par")
    else:
        return print(f"{numero} impar")
 

numero = int(input("digite um numero: "))
impar_par = impar_par(numero)
