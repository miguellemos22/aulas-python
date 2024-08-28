import os 
import time
os.system("cls || clear ")

import os 
import time
os.system("cls || clear ")

contador = 0

while True:
    login = input("digite seu login: ")
    senha =int(input("digite sua senha: "))
    contador += 1

    if login == "migs" and senha == 123:
            print("bem vindo") 
            break
    else: 
            print("tente novamente")
            if contador == 3:
                   break
            
        
     