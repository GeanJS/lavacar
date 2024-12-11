# Importando as classes e o mêtodo 'os' para limpar o terminal
from cliente.screen import menu as show_cliente
from cliente.entity import PessoaFisica, PessoaJuridica
from veiculo.entity import Veiculo
from ordem_de_servico.entity import OrdemServico
import os
from time import sleep


def exibindo_menu(opcao=None):
    if opcao != None:
        return opcao
    
    print("\nMenu:")
    print("C - Entrar no Menu do Cliente")
    print("5 - Adicionar veículo ao cliente")
    print("6 - Remover veículo do cliente")
    print("7 - Criar ordem de serviço")
    print("8 - Remover Ordem de Serviço")
    print("9 - Listar ordens de serviço ativas")
    print("10 - Historíco Geral de Ordens de Serviço")
    print("11 - Sair")

    return input("Escolha uma opção: ")

def main():
    clientes = []
    ordens_servico = []
    opcao = None

    while True:
        opcao = exibindo_menu(opcao)

        match opcao:
            case 'C':
                opcao = show_cliente.menu()
            case '1':  # Adiciona o cliente em Pessoa Física
                os.system('clear')
                nome = input("\nDigite o nome da pessoa: ")
                celular = input("Digite o celular da pessoa: ")
                email = input("Digite o email da pessoa: ")
                cpf = input("Digite o CPF da pessoa: ")
                pessoa_fisica = PessoaFisica(nome, celular, email, cpf)
                clientes.append(pessoa_fisica)
                print(f"Cliente {nome} adicionado com sucesso!")
                sleep(2)
                opcao = "C"

            case '2':  # Adiciona o cliente Pessoa Jurídica
                os.system('clear')
                nome = input("\nDigite o nome da empresa: ")
                celular = input("Digite o celular da empresa: ")
                email = input("Digite o email da empresa: ")
                cnpj = input("Digite o CNPJ da empresa: ")
                pessoa_juridica = PessoaJuridica(nome, celular, email, cnpj)
                clientes.append(pessoa_juridica)
                print(f"Cliente {nome} adicionado com sucesso!")
                sleep(2)
                opcao = "C"

            case '3':  # Remove o cliente
                os.system('clear')
                nome = input("\nDigite o nome do cliente para remover: ")
                cliente_encontrado = next((cliente for cliente in clientes if cliente.nome == nome), None)
                
                if cliente_encontrado:
                    print(f"\nAo remover o cliente {nome}, todos os veículos e ordens de serviço associados a ele serão removidos!")
                    confirmacao = input("\nTem certeza que deseja remover este cliente? (sim/não): ").lower()

                    if confirmacao == 'sim':
                        # Remover veículos e ordens de serviço do cliente
                        cliente_encontrado.veiculos.clear()
                        cliente_encontrado.ordens_servico.clear()

                        # Remover o cliente
                        clientes.remove(cliente_encontrado)
                        print(f"Cliente {nome} removido com sucesso, junto com seus veículos e ordens de serviço.")
                    else:
                        print(f"Remoção do cliente {nome} cancelada.")
                else:
                    print("Cliente não encontrado.")


            case '4':  # Mostra os dados do cliente
                os.system('clear')
                nome = input("\nDigite o nome do cliente para mostrar os dados: ")
                cliente_encontrado = next((cliente for cliente in clientes if cliente.nome == nome), None)
                
                if cliente_encontrado:
                    cliente_encontrado.exibe_dados()
                else:
                    print("\nCliente não encontrado.")

            case '5':  # Adiciona veículo
                os.system('clear')
                nome_cliente = input("\nDigite o nome do cliente para adicionar veículo: ")
                cliente_encontrado = next((cliente for cliente in clientes if cliente.nome == nome_cliente), None)
                
                if cliente_encontrado:
                    marca = input("Digite a marca do veículo: ")
                    modelo = input("Digite o modelo do veículo: ")
                    cor = input("Digite a cor do veículo: ")
                    placa = input("Digite a placa do veículo: ")
                    motor = input("Digite o tipo de motor do veículo: ")
                    veiculo = Veiculo(marca, modelo, cor, placa, motor)
                    cliente_encontrado.adiciona_veiculo(veiculo)
                else:
                    print("\nCliente não encontrado.")

            case '6':  # Remove veículo (Adicionei a parte de remover a OS junto)
                os.system('clear')
                nome_cliente = input("\nDigite o nome do cliente para remover o veículo: ")
                cliente_encontrado = next((cliente for cliente in clientes if cliente.nome == nome_cliente), None)
                
                if cliente_encontrado:
                    placa = input("\nDigite a placa do veículo que deseja remover: ")
                    veiculo_encontrado = None
                    for veiculo in cliente_encontrado.veiculos:
                        if veiculo.placa == placa:
                            veiculo_encontrado = veiculo
                            break
                        
                    if veiculo_encontrado:
                        ordens_a_remover = []
                        for ordem in cliente_encontrado.ordens_servico:
                            if ordem.veiculo == veiculo_encontrado:
                                ordens_a_remover.append(ordem)
                    
                        if ordens_a_remover:
                            print(f"\nEste veículo possui {len(ordens_a_remover)} ordens de serviço em aberto. Elas também serão removidas.")

                        confirmacao = input(f"\nTem certeza que deseja remover o veículo {placa}? (sim/não): ").lower()
                    
                        if confirmacao == 'sim':
                        # Remover ordens de serviço associadas
                            for ordem in ordens_a_remover:
                                cliente_encontrado.ordens_servico.remove(ordem)
                            print(f"\nAs ordens de serviço relacionadas ao veículo {placa} foram removidas.")

                            # Remover o veículo do cliente
                            cliente_encontrado.remove_veiculo(placa)
                            print(f"Veículo {placa} removido com sucesso.")

                        else:
                                print("Remoção do veículo cancelada.")
                    else:
                        print("\nVeículo não encontrado.")
                else:
                    print("\nCliente não encontrado.")

            case '7':  # Cria uma ordem de serviço
                os.system('clear')
                nome_cliente = input('\nDigite o nome do cliente para a ordem de serviço: ')
                cliente_encontrado = next((cliente for cliente in clientes if cliente.nome == nome_cliente), None)
                
                if not cliente_encontrado:
                    print('\nCliente não encontrado!')
                    continue

                if not cliente_encontrado.veiculos:
                    print(f'\nO cliente {nome_cliente} não tem veículos cadastrados!')
                    continue

                print('\nVeículos cadastrados:')
                for idx, veiculo in enumerate(cliente_encontrado.veiculos, start=1):
                    print(f'{idx} - {veiculo.modelo} ({veiculo.placa})')

                try:
                    escolha_veiculo = int(input('\nEscolha o veículo pelo número: ')) - 1
                    if escolha_veiculo < 0 or escolha_veiculo >= len(cliente_encontrado.veiculos):
                        print('Opção inválida!')
                        continue
                    veiculo_escolhido = cliente_encontrado.veiculos[escolha_veiculo]

                    print('\nServiços disponíveis:')
                    servicos_disponiveis = {
                        1: ("Limpeza Externa", 80.00),
                        2: ("Limpeza Interna", 100.00),
                        3: ("Troca de Óleo", 50.00),
                        4: ("Pintura", 1000.00),
                    }
                    for k, v in servicos_disponiveis.items():
                        print(f'{k} - {v[0]} (R${v[1]:.2f})')

                    escolha_servico = int(input("\nEscolha o serviço pelo número: "))
                    if escolha_servico not in servicos_disponiveis:
                        print("Serviço inválido. Nenhuma ordem foi criada.")
                        continue

                    descricao, valor = servicos_disponiveis[escolha_servico]

                    ordem = OrdemServico(cliente=cliente_encontrado, veiculo=veiculo_escolhido, descricao=descricao, valor=valor)
                    cliente_encontrado.ordens_servico.append(ordem)
                    ordens_servico.append(ordem) # Salvar as ordens em uma lista para ter uma cópia mesmo se forem excluidas

                    print(f"\nOrdem de serviço criada com sucesso para o cliente {cliente_encontrado.nome}:")
                    print(f"Serviço: {descricao}")
                    print(f"Veículo: {veiculo_escolhido.modelo} ({veiculo_escolhido.placa})")
                    print(f"Valor: R${valor:.2f}")

                except ValueError:
                    print("Entrada inválida. Por favor, insira um número válido.")

            case '8':  # Excluir uma ordem de serviço específica
                os.system('clear')
                nome_cliente = input("\nDigite o nome do cliente para listar as ordens de serviço: ")
                cliente_encontrado = None
                for cliente in clientes:
                    if cliente.nome == nome_cliente:
                        cliente_encontrado = cliente
                        break

                if not cliente_encontrado:
                    print('\nCliente não encontrado!')
                    continue

                if not cliente_encontrado.ordens_servico:
                    print(f'\nO cliente {nome_cliente} não tem ordens de serviço cadastradas!')
                    continue

                print('\nOrdens de serviço do cliente:')
                for idx, ordem in enumerate(cliente_encontrado.ordens_servico, start=1):
                    print(f'{idx} - {ordem.descricao} (R${ordem.valor:.2f})')

                try:
                    escolha_ordem = int(input('\nEscolha a ordem de serviço pelo número para excluir: ')) - 1
                    if escolha_ordem < 0 or escolha_ordem >= len(cliente_encontrado.ordens_servico):
                        print("Opção inválida!")
                        continue
                    ordem_escolhida = cliente_encontrado.ordens_servico[escolha_ordem]

                    confirmacao = input(f"Tem certeza que deseja excluir a ordem de serviço '{ordem_escolhida.descricao}'? (sim/não): ").lower()
                    if confirmacao == 'sim':
                        cliente_encontrado.ordens_servico.remove(ordem_escolhida)
                        print(f"Ordem de serviço '{ordem_escolhida.descricao}' removida com sucesso!")
                    else:
                        print("Exclusão da ordem de serviço cancelada.")

                except ValueError:
                    print("Entrada inválida. Por favor, insira um número válido.")
            
            case '9':  # Listar todas as ordens de serviço
                os.system('clear')
                if not clientes:
                    print('\nNão tem clientes cadastrados')

                print('\nEssas são as ordens de serviço:\n')
                total_geral = 0
                for cliente in clientes:
                    for ordem in cliente.ordens_servico:
                        ordem.exibe_dados()
                        print('-' * 12)
                        total_geral += ordem.valor
                if total_geral > 0:
                    print(f'\nValor total das ordens de serviço é de: R${total_geral:.2f}')
                else:
                    print('Não tem ordens de serviço cadastradas!')

            
            case '10':  # Histórico Geral de Ordens de Serviço
                os.system('clear')
                if not ordens_servico:
                    print('\nNão há ordens de serviço no histórico.')
                else:
                    print("\nHistórico Geral de Ordens de Serviço:\n")
                    total_geral = 0
                    for ordem in ordens_servico:
                        # Exibe as informações da ordem de serviço
                        print(f"Cliente: {ordem.cliente.nome}")
                        print(f"Veículo: {ordem.veiculo.modelo} ({ordem.veiculo.placa})")
                        print(f"Serviço: {ordem.descricao}")
                        print(f"Valor: R${ordem.valor:.2f}")
                        print('-' * 40)
                        total_geral += ordem.valor
                    if total_geral > 0:
                        print(f"\nValor total das ordens de serviço no histórico: R${total_geral:.2f}")
                    else:
                        print("Não há ordens de serviço registradas no histórico.")
            
            case '11':
                print("Programa Encerrado!!")
                break

            case _:
                print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
