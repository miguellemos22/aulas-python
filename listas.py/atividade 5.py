import os 
os.system("cls || clear ")

numero = 0


def impar_par(numero):
    contador_par = 0
    contador_impar = 0

    for i in range(6):
        numero = int(input("digite um numero: "))

        if numero % 2 == 0:
            contador_par += 1
        else:
            contador_impar += 1
        
       
    print(f"\nquantidade pares: {contador_par}")
    print(f"\nquantidade impares: {contador_impar}")
 



impar_par = impar_par(numero)