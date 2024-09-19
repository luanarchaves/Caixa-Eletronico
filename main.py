
def operação(matriz, valor, option):
    #o loop esta retirando as notas de forma errada  
    if option == '1':
        print('vc escolheu 1\n')
        valor -= 20
        matriz[2][2] -= 1
        matriz[3][2] += 1
    elif option == '2':
        print('vc escolheu 2\n')
        valor -= 20
        matriz[2][3] -= 2
        matriz[3][3] += 1
    elif option == '3':
        print('voce escolheu 3\n')
    else:
        print('A opção inserida não existe.')
        return

    i = 0
    for i in range(6):
        if valor >= matriz[1][i]:
            while valor >= matriz[1][i]:
                valor -= matriz[1][i]
                matriz[2][i] -= 1
                matriz[3][i] += 1 
    return matriz

def carregar_notas(matriz):
    print('\n--Notas Carregadas, retorno ao Menu.')
    i = 1
    for i in range(6):
        matriz[2][i - 1] = 100
    return matriz
    
def retirar_notas(matriz):
    total_caixa = 0
    i = 0
    for i in range(6):
        total_caixa = matriz[1][i] * 100
        


    print('\nQuanto deseja retirar?\n')
    valor = int(input())

    if valor > total_caixa:
        print('Valor excedeu o limite do caixa. Retornando ao menu')
        menu()

    print(
        '\nDeseja notas de troco sobre o valor solicitado, 1 nota de 20 ou 2 notas de 10?\n'
        '1 nota de 20 - Digite 1\n'
        '2 nota de 10 - Digite 2\n'
        'Não retirar notas de troco - Digite 3')
    
    option = input()

    matriz = operação(matriz, valor, option)  

    print('Voce vai receber:\n')
    i = 0
    for i in range(6):
        if matriz[3][i] > 0:
            print(f'{matriz[3][i]} nota(s) de {matriz[1][i]}')
        
    print(
        '\nEsta de acordo?\n'
        'Sim - Digite 1\n'
        'Cancelar - Digite 2'
    )

    option = input()

    if option == '2':
        print('Retirada de notas sendo cancelada. Retorno ao menu.')
        menu()
    elif option != '1' and option != '2':
        print('Opção invalida. Retorno ao menu')
        menu()

    #perguntar se ta tudo ok ou se quer cancelar
    print(matriz)
    print('\n--Operação finalizada, retorno ao Menu.')
    return matriz
    
def estatistica(matriz, value_estatist):
    return 'Obrigo por utlizar nossos serviços'


def menu(cod_banco):

#se o cliente for do banco Caixa as info de saque deles serão armazenadas na coluna caixa no final
    matriz = [ 
    ['Banco do Brasil', 'Santander', 'Itaú','Caixa'],
    [100, 50, 20, 10, 5, 2],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
    ]

    value_estatist = [
        ['Banco do Brasil', 'Santander', 'Itaú','Caixa'],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]

    while True:

        if cod_banco >= 5:
            print('A opção inserida não existe\n')
            return

        print(
            f'\nCaixa Eletronico {matriz[0][cod_banco - 1]}\n'
            '\nEscolha o que deseja fazer:\n'
            '\nCarregar Notas - Digite 1\n'
            'Retirar Notas - Digite 2\n'
            'Estatistica - Digite 3\n'
            'Finalizar - Digite 4\n'
            )

        option = input()

        if option == '1':
            matriz = carregar_notas(matriz)
        elif option == '2':
            matriz = retirar_notas(matriz)
        elif option == '3':
            value_estatist = estatistica(matriz, value_estatist)
        elif option == '4':
            print('Obrigo por utlizar nossos serviços')
            break
        else:
            print('A opção inserida não existe')
            menu()
        
    return 0

print(
        '\nDigite seu banco\n'
        '\nBanco do Brasil - Digite 1\n'
        'Santander - Digite 2\n'
        'Itaú - Digite 3\n'
        'Caixa - Digite 4\n')
        
cod_banco = int(input())


menu(cod_banco)



