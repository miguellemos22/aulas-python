import os 
os.system("cls || clear ")

nome = input("digite seu nome: ")
idade = int(input("digite sua idade: "))
nota1 = float(input("digite sua primeira nota: "))         
nota2 = float(input("digite sua segunda nota: "))
nota3 = float(input("digite sua terceira nota: "))
media = (nota1 + nota2 + nota3) /3

if media < 7:
    resultado = "reprovado"

else:
    resultado = "aprovado"

print(f"nome do aluno: {nome}")
print(f"idade do aluno: {idade}")
print(f"primeira nota: {nota1}")
print(f"segunda nota: {nota2}")
print(f"terceira nota: {nota3}")
print(f"media do aluno: {media}")
print(f"resultado: {resultado}")