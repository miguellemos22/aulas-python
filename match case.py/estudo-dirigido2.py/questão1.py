class RegistroFinanceiro:
    def __init__(self, id, p1, p2, p3, r1, r2, r3, t_entradas, saidas, fornecedores, aluguel, luz, agua, f_pasamento, fgts, inss, rsocios, tsaidas):
        self.id = id
        self.p1 = p1  # Lista de valores previstos tipo 1
        self.p2 = p2  # Lista de valores previstos tipo 2
        self.p3 = p3  # Lista de valores previstos tipo 3
        self.r1 = r1  # Lista de valores realizados tipo 1
        self.r2 = r2  # Lista de valores realizados tipo 2
        self.r3 = r3  # Lista de valores realizados tipo 3
        self.t_entradas = t_entradas  # Total de Entradas
        self.saidas = saidas  # Total de Saídas
        self.fornecedores = fornecedores
        self.aluguel = aluguel  # Total de aluguel
        self.luz = luz  # Total de luz
        self.agua = agua  # Total de água
        self.f_pasamento = f_pasamento  # Total de f. pasamento
        self.fgts = fgts  # Total de FGTS
        self.inss = inss  # Total de INSS
        self.rsocios = rsocios  # Total de R Sócios
        self.tsaidas = tsaidas  # Total de TSaídas

    def saldo_anterior(self):
        # Calcula o saldo anterior como a diferença total entre entradas e saídas
        return self.t_entradas - self.saidas

    def saldo_acumulado(self):
        # Calcula o saldo acumulado subtraindo os valores dos fornecedores, aluguel, luz, água, f. pasamento, FGTS, INSS, R sócios e TSaídas do saldo anterior
        saldo_anterior = self.saldo_anterior()
        return saldo_anterior - (
            self.fornecedores + self.aluguel + self.luz + self.agua +
            self.f_pasamento + self.fgts + self.inss + self.rsocios + self.tsaidas
        )

    def saldo_total(self):
        # Retorna o saldo total, que é o saldo acumulado
        return self.saldo_acumulado()

    def __str__(self):
        return (
            f"ID: {self.id}\n"
            f"Previsto Tipo 1: {self.p1}\n"
            f"Previsto Tipo 2: {self.p2}\n"
            f"Previsto Tipo 3: {self.p3}\n"
            f"Realizado Tipo 1: {self.r1}\n"
            f"Realizado Tipo 2: {self.r2}\n"
            f"Realizado Tipo 3: {self.r3}\n"
            f"Total Entradas: {self.t_entradas}\n"
            f"Saídas: {self.saidas}\n"
            f"Fornecedores: {self.fornecedores}\n"
            f"Aluguel: {self.aluguel}\n"
            f"Luz: {self.luz}\n"
            f"Água: {self.agua}\n"
            f"F. Pasamento: {self.f_pasamento}\n"
            f"FGTS: {self.fgts}\n"
            f"INSS: {self.inss}\n"
            f"R Sócios: {self.rsocios}\n"
            f"TSaídas: {self.tsaidas}\n"
            f"Saldo Anterior: {self.saldo_anterior()}\n"
            f"Saldo Acumulado: {self.saldo_acumulado()}\n"
            f"Saldo Total: {self.saldo_total()}\n"
        )


class SistemaFinanceiro:
    def __init__(self):
        self.registros = {}

    def adicionar_registro(self, id, p1, p2, p3, r1, r2, r3, t_entradas, saidas, fornecedores, aluguel, luz, agua, f_pasamento, fgts, inss, rsocios, tsaidas):
        if id in self.registros:
            print(f"Erro: Já existe um registro com o ID {id}.")
        else:
            self.registros[id] = RegistroFinanceiro(id, p1, p2, p3, r1, r2, r3, t_entradas, saidas, fornecedores, aluguel, luz, agua, f_pasamento, fgts, inss, rsocios, tsaidas)
            print(f"Registro {id} adicionado com sucesso!")

    def listar_registros(self):
        if not self.registros:
            print("Nenhum registro encontrado.")
        else:
            for registro in self.registros.values():
                print(registro)

    def buscar_registro(self, id):
        registro = self.registros.get(id)
        if registro:
            print(registro)
        else:
            print(f"Erro: Registro com ID {id} não encontrado.")

    def saldo_anterior(self, id):
        registro = self.registros.get(id)
        if registro:
            print(f"Saldo Anterior para ID {id}: {registro.saldo_anterior()}")
        else:
            print(f"Erro: Registro com ID {id} não encontrado.")

    def saldo_acumulado(self, id):
        registro = self.registros.get(id)
        if registro:
            print(f"Saldo Acumulado para ID {id}: {registro.saldo_acumulado()}")
        else:
            print(f"Erro: Registro com ID {id} não encontrado.")

    def saldo_total(self, id):
        registro = self.registros.get(id)
        if registro:
            print(f"Saldo Total para ID {id}: {registro.saldo_total()}")
        else:
            print(f"Erro: Registro com ID {id} não encontrado.")


# Exemplo de uso do sistema
if __name__ == "__main__":
    sistema = SistemaFinanceiro()
    
    # Adicionando um registro com os valores fornecidos
    p1 = [60000]
    r1 = [60000]
    p2 = [100000]
    r2 = [80000]
    p3 = [100000]
    r3 = [80000]
    p4 = [100000]
    r4 = [80000]
    
    t_entradas = sum(p1 + p2 + p3 + p4)  # Total de entradas previstas
    saidas = sum(r1 + r2 + r3 + r4)  # Total de saídas realizadas
    
    fornecedores = 60000
    aluguel = sum([10000] * 5)  # Total de aluguel (5 vezes 10.000)
    luz = sum([4000] * 5)  # Total de luz (5 vezes 4.000)
    agua = sum([1000] * 5)  # Total de água (5 vezes 1.000)
    f_pasamento = sum([40000] * 5)  # Total de f. pasamento (5 vezes 40.000)
    fgts = sum([4000] * 5)  # Total de FGTS (5 vezes 4.000)
    inss = sum([4000] * 5)  # Total de INSS (5 vezes 4.000)
    rsocios = sum([15000] * 5)  # Total de R Sócios (5 vezes 15.000)
    tsaidas = 20000
    
    sistema.adicionar_registro(
        '001', p1, p2, p3, r1, r2, r3, t_entradas, saidas, fornecedores, aluguel, luz, agua, f_pasamento, fgts, inss, rsocios, tsaidas
    )
    
    while True:
        print("\nSistema Financeiro XYZ")
        print("1. Adicionar Registro")
        print("2. Saldo Anterior")
        print("3. Saldo Acumulado")
        print("4. Saldo Total")
        print("5. Listar Registros")
        print("6. Buscar Registro")
        print("7. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            id = input("Digite o ID do registro: ")
            p1 = list(map(float, input("Digite os valores previstos tipo 1 separados por vírgula: ").split(',')))
            p2 = list(map(float, input("Digite os valores previstos tipo 2 separados por vírgula: ").split(',')))
            p3 = list(map(float, input("Digite os valores previstos tipo 3 separados por vírgula: ").split(',')))
            r1 = list(map(float, input("Digite os valores realizados tipo 1 separados por vírgula: ").split(',')))
            r2 = list(map(float, input("Digite os valores realizados tipo 2 separados por vírgula: ").split(',')))
            r3 = list(map(float, input("Digite os valores realizados tipo 3 separados por vírgula: ").split(',')))
            t_entradas = float(input("Digite o total de Entradas: "))
