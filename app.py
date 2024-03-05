import os

restaurantes = ['House do podrão']

def msg_boasvindas():
    print('Ｓａｂｏｒ Ｅｘｐｒｅｓｓ 🥗 \n\n')

def menu_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair \n')

def voltar_menu_principal():
    input('\n Precione qualquer botão para voltar ao menu novamente ')
    main()
    
def opcao_invalida():
    print('Opção inválida! \n')
    voltar_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def cadastar_restaurante():
    exibir_subtitulo('Cadastro de restaurante')

    nome_restaurante = input('Digite o nome do restaurante: ')
    restaurantes.append(nome_restaurante)
    print(f'Restaurante: {nome_restaurante}, cadastrado com sucesso ✅ \n')

    voltar_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Restaurantes cadastrados')

    for restaurante in restaurantes:
        print(f'.{restaurante}')
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
            print('Ativar restaurante')
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

def finalizar_app():
    exibir_subtitulo('Encerrando App')

def main():
    os.system('cls')
    msg_boasvindas()
    menu_opcoes()
    escolhe_opcao()

if __name__ == '__main__':
    main()
