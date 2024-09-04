import os 
os.system("cls || clear ")

#função com retorno.
def somar(n1, n2): #n1 e n2 = primeiro_numero e segundo_numero
    soma = n1 + n2
    return soma

primeiro_numero = int(input("digite o primeiro numero: "))
segundo_numero = int(input("digite o segundo numero: "))

soma = somar(primeiro_numero, segundo_numero)

print(f"soma: {soma}")