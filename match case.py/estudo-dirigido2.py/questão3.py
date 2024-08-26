import os 
os.system("cls || clear ")

def calcular_payback(investimento, fluxos_de_caixa):
    acumulado = 0
    for i, fluxo in enumerate(fluxos_de_caixa):
        acumulado += fluxo
        if acumulado >= investimento:
            # O payback ocorre entre o período atual e o período anterior
            periodo = i + 1
            retorno_acumulado = acumulado
            return periodo, retorno_acumulado
    return None, acumulado

# Parâmetros
investimento_inicial = 60000
fluxos_de_caixa = [10000, 5000, 5000, 5000, 6000, 8000, 15000, 20000, 100000]

# Cálculo do payback
periodo_payback, retorno_acumulado = calcular_payback(investimento_inicial, fluxos_de_caixa)

if periodo_payback:
    print(f"O payback ocorre no período {periodo_payback} com retorno acumulado de R${retorno_acumulado:.2f}.")
else:
    print("O investimento não é totalmente recuperado com os fluxos de caixa fornecidos.")
