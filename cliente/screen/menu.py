def __show_options():
    print("Menu do Cliente")
    print("1 - Adicionar cliente Pessoa Física")
    print("2 - Adicionar cliente Pessoa Jurídica")
    print("3 - Remover cliente")
    print("4 - Mostrar dados do cliente")
    print("x -- Sair")

def menu():
    
    while True:
        __show_options()
        opcao = input("Informe a opção desejada: ")
        match opcao:
            case 'x':
                return None
            case _:
                return opcao
