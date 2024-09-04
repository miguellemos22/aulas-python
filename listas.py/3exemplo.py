import os 
os.system("cls || clear ")
#função com retorno - return
def descontos_salario(salario_bruto):
    vale_transporte = 200
    vale_refeição = 200
    plano_de_saude = 300

    resultado = salario_bruto - vale_transporte - vale_refeição - plano_de_saude

    return resultado

salario_bruto = float(input("digite o valor do seu salario bruto: "))

salario_liquido = descontos_salario(salario_bruto)

print(f"salario liquido: {salario_liquido}")