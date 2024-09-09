import os 
os.system("cls || clear ")

ano_de_nascimento = int(input("digite seu ano de nascimento: "))

def idade(n1):
    ano_atual = 2024
    subtracao = ano_atual - n1 

    return subtracao

idade = idade(ano_de_nascimento)
print(f"idade: {idade}")