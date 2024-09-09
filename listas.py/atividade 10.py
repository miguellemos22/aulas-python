import os 
os.system("cls || clear ")

altura = float(input("digite sua altura: "))

peso = float(input("digite seu peso: "))

def imc(n1, n2):
    
    resposta = n2 / (n1 * n1)

    return resposta
resposta = imc(altura, peso)

if resposta >= 40:
    print("obesidade grau 3:")
elif resposta >= 35:
    print("obesidade grau 2:")
elif resposta >= 30:
    print("obesidade grau 1:")
elif resposta >= 25:
    print("sobrepeso:")
elif resposta >= 18.5:
    print("peso normal:")
elif resposta <= 18.5:
    print("abaixo do peso") 



print(f"imc: {resposta:.2f}")