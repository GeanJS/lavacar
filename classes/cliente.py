# Aqui temos a classe Cliente, cada cliente tem uma lista de veiculos em seu nome
class Cliente:
    def __init__(self, nome, celular, email):
        self.nome = nome
        self.celular = celular
        self.email = email
        self.veiculos = []
        self.ordens_servico = []
        
        
    # Método simples para adicionar veiculo ao cliente :)
    def adiciona_veiculo(self, veiculo):
        self.veiculos.append(veiculo)
        print(f"Veículo {veiculo.modelo} adicionado para {self.nome}.")
     
     
    # Esse é pra remover, usei a placa como parâmetro de busca por que ela não se repete    
    def remove_veiculo(self, placa):
        for veiculo in self.veiculos:
            if veiculo.placa == placa:
                self.veiculos.remove(veiculo)
                print(f"Veiculo com a placa {placa} removido com sucesso")
                return
        print(f"Veículo com placa {placa} não encontrado.")
    
    
    # Método para exibir os dados, não usei o __str__ apresentado em sala pois ainda não me acostumei
    def exibe_dados(self):
        print(f"Cliente: {self.nome}")
        print(f"Celular: {self.celular}")
        print(f"Email: {self.email}")
        print("\nVeículos:")
        for veiculo in self.veiculos:
            veiculo.exibe_dados()

        print("\nOrdens de Serviço: ")
        total = 0
        for ordem in self.ordens_servico:
            ordem.exibe_dados()
            total += ordem.valor
        print(f"\nTotal: R${total:.2f}")
            
            
# Decidi deixar as classes filhas no mesmo arquivo, o polimorfismo já está implementado no método exibe_dados.            
class PessoaFisica(Cliente):
    def __init__(self, nome, celular, email, cpf):
        super().__init__(nome, celular, email)
        self.cpf = cpf
        
    def exibe_dados(self):
        super().exibe_dados()
        print(f"\nCPF: {self.cpf}")


class PessoaJuridica(Cliente):
    def __init__(self, nome, celular, email, cnpj):
        super().__init__(nome, celular, email)
        self.cnpj = cnpj
    
    def exibe_dados(self):
        super().exibe_dados()
        print(f"\nCNPJ: {self.cnpj}")