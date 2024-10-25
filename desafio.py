# ***Desafio 1 Condicionais***

# ***Crie um sistema de e-commerce, onde o usuário possa:***

# *cadastrar-se*

cadastro = []

login_cadastro = int(input('digite seu numero de cadastro: '))
senha_cadastro = int(input('digite sua senha de cadastro: '))

cadastro.insert(0, login_cadastro)
cadastro.insert(1, senha_cadastro)

print(cadastro)

print('AGORA QUE VC TERMINOU SEU CADASTRO, FAÇA O LOGIN NA SUA CONTA: ')

login = int(input('digite seu numero de login: '))
senha = int(input('digite sua senha de login: '))

list_login = [login, senha]
print(list_login)

if list_login == cadastro:
    print('Seja bem-vindo!')
    print('MERCADINHO DO JÃO')

    produtos = ['FEIJÃO', 'ARROZ']
    valores = [5.0, 10.0]

    print('''
    0 - FEIJÃO - 5.0
    1 - ARROZ - 10.0
    ''')

    carrinho = []

    escolha = int(input('escolha seu(s) produto(s): '))

    if escolha == 1 or escolha == 0:
        print('Você escolheu 1 produto')
        carrinho.append(produtos[escolha])
        print(carrinho)
    else:
        print('esse produto não existe')

    
    

    lista_sim_nao = ['sim', 'nao']
    
    print('''
    0 - sim
    1 - não
    ''')
    adicao = int(input('Você quer adicionar mais algum produto?'))

   
    if adicao == 0: 
        print(carrinho)
        print('Escolha outro produto')

        print('''
        0 - FEIJÃO - 5.0
        1 - ARROZ - 10.0
        ''')

        escolha = int(input('escolha seu(s) produto(s): '))
        carrinho.append(produtos[escolha])
        print(carrinho)    
        print('FORMA DE PAGAMENTO:')

        formas = [0, 1, 2]

        print('''
        0 - Pix
        1 - Dinheiro
        2 - Cartão
        ''')

        sua_forma_de_pagamento = int(input('Digite o número da sua forma de pagamento'))

        if sua_forma_de_pagamento == formas[0]:
            print('Sua forma de pagamento é pix')
        elif sua_forma_de_pagamento == formas[1]:
            print('Sua forma de pagamento é Dinheiro')
        elif sua_forma_de_pagamento == formas[2]:
            print('Sua forma de pagamento é Cartão')
        else:
            print('Voce inseriu uma forma invalida')


        print('...')

        print('COMPRA CONCLUIDA COM SUCESSO!')
    


    else:
        print(carrinho)    
        print('FORMA DE PAGAMENTO:')

        formas = [0, 1, 2]

        print('''
        0 - Pix
        1 - Dinheiro
        2 - Cartão
        ''')

        sua_forma_de_pagamento = int(input('Digite o número da sua forma de pagamento'))

        if sua_forma_de_pagamento == formas[0]:
            print('Sua forma de pagamento é pix')
        elif sua_forma_de_pagamento == formas[1]:
            print('Sua forma de pagamento é Dinheiro')
        elif sua_forma_de_pagamento == formas[2]:
            print('Sua forma de pagamento é Cartão')
        else:
            print('Voce inseriu uma forma invalida')


        print('...')

        print('COMPRA CONCLUIDA COM SUCESSO!')

else:
    print('ops, algo deu errado.')   

