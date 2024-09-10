import os 
os.system("cls || clear ")

lista_notas = []
quantidade_notas = 4
contador = 0
soma = 0

for i in range(quantidade_notas):
    nota = float(input("digite uma nota: "))
    lista_notas.append(nota)
    soma += nota
media = soma / quantidade_notas
os.system("cls || clear ")

for i, nota in enumerate(lista_notas):
    print(f"{i+1}º nota: {nota}")

if nota >= 7:
    print("aprovado")
elif nota <= 5:
    print("recuperação")
else:
    print("reprovado")

print(f"media: {media}")

