import os

restaurantes = [{'nome':'House of the Podrão', 'categoria': 'Podrão Raiz', 'ativo': False},
                {'nome':'Bodega do Carlão', 'categoria': 'Boteco', 'ativo': True},
                {'nome':'Flor de giz de cera', 'categoria': 'Doceria diabetes tipo 1', 'ativo': True},
                {'nome':'Biqueira do sabor, tempero verde e marmita prensada', 'categoria': 'Marmitaria de quebrada', 'ativo': False},     
]

def msg_boasvindas():
    print('Ｓａｂｏｒ Ｅｘｐｒｅｓｓ 🥗 \n\n')

def menu_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar ou desativa restaurante')
    print('4. Sair \n')

def voltar_menu_principal():
    input('\n Precione qualquer botão para voltar ao menu novamente ')
    main()
    
def opcao_invalida():
    print('Opção inválida! \n')
    voltar_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastar_restaurante():
    exibir_subtitulo('Cadastro de restaurante')

    nome_restaurante = input('Digite o nome do restaurante: ')
    categoria = input(f'Digite a categoria do restaurante: {nome_restaurante}: ')

    dados_restaurantes = {'nome': nome_restaurante, 'categoria': categoria, 'ativo': False}

    restaurantes.append(dados_restaurantes)
    print(f'Restaurante: {nome_restaurante}, cadastrado com sucesso ✅ \n')

    voltar_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Restaurantes cadastrados')

    print(f'{'Nome do restaurante'.ljust(20)}   {'Categoria'.ljust(20)}   Status')
    print()

    for restaurante in restaurantes:
        nome = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] == True else 'desativado'
        print(f'{nome.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    print()
    voltar_menu_principal()
    
def escolhe_opcao():
    try:
        escolha = int(input('Selecione uma das opções: '))

        if escolha == 1:
            cadastar_restaurante()
        elif escolha == 2:
            listar_restaurantes()
        elif escolha == 3:
            alternar_estado_restaurante()
        elif escolha == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
         
        """
            match escolha:
            case 1:
                print('Cadastrar restaurante')
            case 2:
                print('Listar restauntares')
            case 3:
                print('Ativar restaurante')
            case 4:
                finalizar_app()
        """

def alternar_estado_restaurante():
    exibir_subtitulo('Ativar ou desativar cadastro de restaurante')
    
    nome_restaurante = input('Digite o nome do restaurante que deseja ativar ou desativar o cadastro: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            messagem = f'Restaurante {nome_restaurante} ativado com sucesso ✅' if restaurante['ativo'] else f'Restaurante {nome_restaurante} desativado com sucesso ✅'
            print(messagem)
    if not restaurante_encontrado:
        print('Restaurante não encontrado')
    
    voltar_menu_principal()

def finalizar_app():
    exibir_subtitulo('Encerrando App')

def main():
    os.system('cls')
    msg_boasvindas()
    menu_opcoes()
    escolhe_opcao()

if __name__ == '__main__':
    main()
