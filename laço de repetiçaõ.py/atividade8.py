
import os 
import time
os.system("cls || clear ")



while True:

    nota1 = float(input(f"digite primeira nota: "))
    nota2 = float(input(f"digite segunda nota: ")) 

    if (nota1 < 0 or nota1 > 10) or ( nota2 < 0 or nota2 > 10):

        print("\nAs notas devem ser maior ou menor que 10.")
    else:
        
        break 

soma = nota1 + nota2
media = soma / 2


print(f"media: {media}")