import os 
os.system("cls || clear ")

lista_notas = []

for i in range(2):
    nota = float(input("digite uma nota: "))
    lista_notas.append(nota)#append = adiconar

#saida de dados
for nota in lista_notas:
    print(f"nota: {nota}")
