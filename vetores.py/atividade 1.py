import os 
os.system("cls || clear ")

lista_notas = []
quantidade_notas = 3
contador = 0
for i in range(quantidade_notas):
    nota = float(input("digite uma nota: "))
    lista_notas.append(nota)


for i, nota in enumerate(lista_notas):
    print(f"{contador+1}º nota: {nota}")