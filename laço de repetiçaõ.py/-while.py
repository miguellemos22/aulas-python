import os 
import time
os.system("cls || clear ")

contador = 0
continua = 's'

#comandos a serem repetidos

while continua =='s':
    print("repetindo...")

    contador += 1 # += - contador = contador + 1

    continua = input("tecle's' se deseja continuar: ").strip().lower()

if contador == 0:
    print("o bloco NAO foi repetido.")
else:
    print(f"o bloco foi repetido {contador} vezes")