import os
#Exemplo de dicionário (chave-valor)
restaurantes = [{'nome':'LifeBox', 'categoria':'Hamburgueria','ativo':False},
                {'nome':'Verona', 'categoria': 'Italiana', 'ativo':True}, 
                {'nome': 'Outback', 'categoria': 'steakhouse alemã', 'ativo':False}
                ]

def exibir_nome_do_programa():
    '''Função exibe nome  estilizado do programa, copiado com uma fonte diferente do site 'fsymbols' '''
    print("""
─────────────────────────────────────────────────────────────────────────────────────────────────────
─██████████████─██████████████───────────██████████████─██████████████─██████████████─████████████───
─██░░░░░░░░░░██─██░░░░░░░░░░██───────────██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░████─
─██░░██████████─██░░██████████───────────██░░██████████─██░░██████░░██─██░░██████░░██─██░░████░░░░██─
─██░░██─────────██░░██───────────────────██░░██─────────██░░██──██░░██─██░░██──██░░██─██░░██──██░░██─
─██░░██─────────██░░██████████───────────██░░██████████─██░░██──██░░██─██░░██──██░░██─██░░██──██░░██─
─██░░██─────────██░░░░░░░░░░██───────────██░░░░░░░░░░██─██░░██──██░░██─██░░██──██░░██─██░░██──██░░██─
─██░░██─────────██████████░░██───────────██░░██████████─██░░██──██░░██─██░░██──██░░██─██░░██──██░░██─
─██░░██─────────────────██░░██───────────██░░██─────────██░░██──██░░██─██░░██──██░░██─██░░██──██░░██─
─██░░██████████─██████████░░██─██████────██░░██─────────██░░██████░░██─██░░██████░░██─██░░████░░░░██─
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██────██░░██─────────██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░████─
─██████████████─██████████████─██████────██████─────────██████████████─██████████████─████████████───
─────────────────────────────────────────────────────────────────────────────────────────────────────
""")

def exibir_opcoes():
    '''Essa função é responsável por exibir o menu de opções disponíveis '''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    ''' Função responsável por exibir a mensagem de finalização do app. '''
    
    exibir_subtitulo('Finalizando app.')
    
def voltar_ao_menu_principal():
    ''' função solicita uma tecla para retornar ao menu principal '''
    input("\nDigite uma tecla para voltar ao menu principal --> ")
    main()

def opcao_invalida():
    ''' Função responsável por exibir a mensagem de opção inválida e retornar ao menu principal '''
    print('Opção Inválida!\n')
    voltar_ao_menu_principal()
    
def exibir_subtitulo(texto):
    ''' Essa função é responsável por exibir um subtítulo estilizado
    
    Inputs:
    - texto: str - O texto do subtítulo'''
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()
    
def cadastrar_novo_restaurante():
    ''' Essa função é responsável por cadastrar um novo restaurante 
    
    Inputs:
    - Nome do restaurante
    - Categoria 
    
    Output:
    - adiciona um novo restaurante a lista de restaurantes.
    
    '''
    
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da catagoria do Restaurante {nome_do_restaurante}: ')
    dados_do_restaurante ={'nome': nome_do_restaurante, 'categoria':categoria, 'ativo': False }
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    
    voltar_ao_menu_principal()
    
def listar_restaurantes():
    ''' Essa função é responsável por listar todos os restaurantes já cadastrados. 
    
    Outputs:
    - Exibe a lista de restaurantes cadastrados na tela. 
    
    '''
    exibir_subtitulo('Listando restaurantes')
    
    print(f'{'Nome do Restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    
    voltar_ao_menu_principal()
    
def alternar_estado_restaurante():
    ''' Essa função altera o estado (negativo/positivo) de um restaurante.
    
    Outputs: 
    - Exibe uma mensagem indicando o sucesso da operação;
    
    '''
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo'] #com a palavra reservada 'not' ele vai inverter o valor tem. 
            mensagem = f'O Restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'o Restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)
    if not restaurante_encontrado:
        print(f'O Restaurante {nome_restaurante} não foi encontrado.' )
        
def escolher_opcao():
    '''Função solicita e executa a opção escolhida pelo usuário.
    
    Outputs
    - Executa a opção escolhida pelo usuário.
    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        elif opcao_escolhida == 3: 
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
        
def main():
    '''Função principal que inicia o programa'''
    
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()