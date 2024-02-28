import os


def msg_boasvidas():
    print('Ｓａｂｏｒ Ｅｘｐｒｅｓｓ 🥗 \n\n')

def menu_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair \n')
    
def escolhe_opcao():
    escolha = int(input('Selecione uma das opções: '))

    if escolha == 1:
        print('Cadastrar restaurante')
    elif escolha == 2:
        print('Listar restauntares')
    elif escolha == 3:
        print('Ativar restaurante')
    else:
        finalizar_app()

def finalizar_app():
    os.system('cls')
    print('Encerrando App \n')
    
def main():
    msg_boasvidas()
    menu_opcoes()
    escolhe_opcao()

if __name__ == '__main__':
    main()
