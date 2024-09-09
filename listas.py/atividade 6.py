import os 
os.system("cls || clear ")

valor_original = float(input("digite um valor: "))
        
def flacionacao(valor_novo):

    if valor_original < 100:
        valor_novo = valor_original * 1.1
    else:
        valor_novo = valor_original * 1.2

    return valor_novo


valor_original = flacionacao(valor_original)

print(f"preço: {valor_original}")