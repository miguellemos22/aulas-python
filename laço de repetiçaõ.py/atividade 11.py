import os 
import time
os.system("cls || clear ")

soma = 0

for i in range(3):
     
     while True:
         nota = float(input(f"digite {i + 1}º nota: "))

         if nota < 0 or nota > 10:
            print("\nAs notas devem ser maior ou menor que 10.")
         else:
          soma = soma + nota
         break

media = soma / 3
     
   
if media >= 7:
        print("aprovado")
        
elif media <= 5:
        print("reprovado")
        
else:
        print("recuperação")
        
print(f"media: {media}")