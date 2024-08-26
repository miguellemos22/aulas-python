import os 
os.system("cls || clear ")

import math

# Dados fornecidos
CA = 4000  # Custo de Aquisição
CC = 160    # Custo de Carregamento
CPA = 0.35  # Custo de Pedido por unidade
PV = 35     # Demanda Anual

# Calcular o tamanho ótimo do lote Q*
Q_star = math.sqrt((2 * CA * PV) / CC)

# Calcular o menor custo total
custo_aquisicao_total = CA * PV / Q_star
custo_carregamento_total = (CC * Q_star) / 2
custo_pedido_total = CPA * PV
custo_total = custo_aquisicao_total + custo_carregamento_total + custo_pedido_total

# Exibir os resultados
print(f"Tamanho ótimo do lote (Q*): {Q_star:.2f}")
print(f"Custo total de aquisição: R${custo_aquisicao_total:.2f}")
print(f"Custo total de carregamento: R${custo_carregamento_total:.2f}")
print(f"Custo total de pedidos: R${custo_pedido_total:.2f}")
print(f"Custo total mínimo: R${custo_total:.2f}")
