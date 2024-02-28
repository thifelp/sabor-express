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

    match escolha:
        case 1:
            print('Cadastrar restaurante')
        case 2:
            print('Listar restauntares')
        case 3:
            print('Ativar restaurante')
        case 4:
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
