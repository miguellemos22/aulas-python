import os 
os.system("cls || clear ")

lista_numeros = []
contador_par = 0
contador_impar = 0

for i in range(6):
    numero = float(input(f"digite o {i + 1}º numero: "))
    lista_numeros.append(numero)


    if numero % 2 == 0:
            contador_par += 1
    else:
            contador_impar += 1
        
       
print(f"\nquantidade pares: {contador_par}")
print(f"\nquantidade impares: {contador_impar}")
 