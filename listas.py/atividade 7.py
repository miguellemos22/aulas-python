import os 
os.system("cls || clear ")

def notas_aluno(n1, n2):
    soma = n1 + n2
    media = soma /2
    return media

def valor_notas(n1, n2):
    if n1 and n2 >= 7:
        print(" aprovado ")
    else:
        print(" reprovado ")
    return(n1,n2)

n1 = float(input("digite sua nota: "))
n2 = float(input("digite sua nota: "))

resultado = notas_aluno(n1, n2)
resultado2 = valor_notas(n1,n2)

print(f"media: {resultado}")
print(f"notas: {resultado2}")
 