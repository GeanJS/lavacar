# Classe Ordem de Servico a ideia dela é mostar o veiculo e o cliente, a descrição do serviço e o valor dele, exemplo "Troca de Óleo, R$300.00"
class OrdemServico:
    def __init__(self, cliente, veiculo, descricao, valor):
        self.cliente = cliente
        self.veiculo = veiculo
        self.descricao = descricao
        self.valor = valor
        
    def exibe_dados(self):
        print("\nOrdem de Serviço:")
        print(f"Cliente: {self.cliente.nome}")
        print(f"Veículo: {self.veiculo.modelo} ({self.veiculo.placa})")
        print(f"Descrição: {self.descricao}")
        print(f"Valor: R${self.valor:.2f}\n")