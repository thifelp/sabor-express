import os

restaurants = [{'name':'House of the Podrão', 'category': 'Podrão Raiz', 'active': False},
                {'name':'Bodega do Carlão', 'category': 'Boteco', 'active': True},
                {'name':'Flor de giz de cera', 'category': 'Doceria diabetes tipo 1', 'active': True},
                {'name':'Biqueira do sabor, tempero verde e marmita prensada', 'category': 'Marmitaria de quebrada', 'active': False},     
]

def welcome_message():
    print('Ｓａｂｏｒ Ｅｘｐｒｅｓｓ 🥗 \n\n')

def options_menu():
    '''
    Função para exibir as opções do menu
    '''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar ou desativa restaurante')
    print('4. Sair \n')

def retunr_main_menu():
    '''
    Função para voltar ao menu principal
    '''
    input('\n Precione qualquer botão para voltar ao menu novamente ')
    main()
    
def invalid_option():
    '''
    Função para lançar execeção na escolha de ações no menu principal
    '''
    print('Opção inválida! \n')
    retunr_main_menu()

def show_subtitle(text):
    os.system('cls')
    line = '*' * (len(text))
    print(line)
    print(text)
    print(line)
    print()

def register_restaurant():
    ''' 
    função para cadastrar novos restaurantes

    Inputs:
    - nome do restaurante
    - categoria

    Output: 
    - Nome do restaurante cadastrado
    '''
    show_subtitle('Cadastro de restaurante')

    name = input('Digite o nome do restaurante: ')
    category = input(f'Digite a categoria do restaurante: {name}: ')

    data_restaurants = {'name': name, 'category': category, 'active': False}

    restaurants.append(data_restaurants)
    print(f'Restaurante: {name}, cadastrado com sucesso ✅ \n')

    retunr_main_menu()

def list_restaurants():
    show_subtitle('Restaurantes cadastrados')

    print(f'{'Nome do restaurante'.ljust(20)}   {'Categoria'.ljust(20)}   Status')
    print()

    for restaurante in restaurants:
        name = restaurante['name']
        categoria = restaurante['category']
        active = 'ativado' if restaurante['active'] == True else 'desativado'
        print(f'{name.ljust(20)} | {categoria.ljust(20)} | {active}')
    print()
    retunr_main_menu()
    
def choose_option():
    try:
        choose = int(input('Selecione uma das opções: '))

        if choose == 1:
            register_restaurant()
        elif choose == 2:
            list_restaurants()
        elif choose == 3:
            change_active_state()
        elif choose == 4:
            finish_app()
        else:
            invalid_option()
    except:
        invalid_option()

def change_active_state():
    show_subtitle('Ativar ou desativar cadastro de restaurante')
    
    name = input('Digite o nome do restaurante que deseja ativar ou desativar o cadastro: ')
    find_restaraunt = False

    for restaurant in restaurants:
        if name == restaurant['name']:
            find_restaraunt = True
            restaurant['active'] = not restaurant['active']
            message = f'Restaurante {name} ativado com sucesso ✅' if restaurant['active'] else f'Restaurante {name} desativado com sucesso ✅'
            print(message)
    if not find_restaraunt:
        print('Restaurante não encontrado')
    
    retunr_main_menu()

def finish_app():
    show_subtitle('Encerrando App')

def main():
    os.system('cls')
    welcome_message()
    options_menu()
    choose_option()

if __name__ == '__main__':
    main()
