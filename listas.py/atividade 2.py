import os 
os.system("cls || clear ")

def soma(n1, n2):
    soma = n1 + n2
    return soma

def subtracao(n1, n2):
    subtracao = n1 - n2
    return subtracao

def multiplicacao(n1, n2):
    multiplicacao = n1 * n2
    return multiplicacao

def divisao(n1, n2):
    divisao = n1 / n2
    return divisao

n1 = int(input("digite o primeiro numero: "))
n2 = int(input("digite o segundo numero: "))
os.system("cls || clear ")

soma = soma(n1, n2)
print(f"soma: {soma}")
subtracao = subtracao(n1, n2)
print(f"subtracao: {subtracao}")
multiplicacao = multiplicacao(n1, n2)
print(f"multiplicacao: {multiplicacao}")
divisao = divisao(n1, n2)
print(f"divisao: {divisao}")



