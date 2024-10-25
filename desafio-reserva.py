# - ***Desafio 2:  Condicionais***

# ***Sistema de Reservas de Hotel:***

# ***Você foi contratado(a) para desenvolver uma parte do sistema de um hotel. O objetivo é criar
#  um sistema que gerencie reservas de quartos e o pagamento das diárias***

print('Seja bem vindo ao Hotel')

cadastro = ['cliente1', 'cliente2', 'cliente3']

cadastro[0] = {
    'nome':'josé',
    'idade': 29
}

cadastro[1] = {
    'nome':'Pedro',
    'idade': 33
}


cadastro[2] = {
    'nome':'Ronaldo',
    'idade': 18
}

quartos = ["Simples", "Duplo", "Luxo"]

print('''
    ESCOLHA O QUARTO DE SUA ESTADIA:

    digite: 100 para - Simples: R$ 100,00 por dia.
    digite: 150 para- Duplo: R$ 150,00 por dia.
    digite: 250 para -  Luxo: R$ 250,00 por dia.
''')

escolha = int(input('Escolha o número correspondente do quarto de sua estadia'))

if escolha == 100:
    print('Sua escolha foi', quartos[0], '100 p/dia')
elif escolha == 150:
    print('Sua escolha foi', quartos[1], '150 p/dia')
elif escolha == 250:
    print('Sua escolha foi', quartos[2], '250 p/dia')
else:
    print('faça uma escolha valida')



qts_dias = int(input('Quantos dias você pretende ficar?'))

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

valor_cliente = escolha * qts_dias
print('O valor total da sua reserva é:', valor_cliente)



print('COMPRA CONCLUIDA COM SUCESSO!')






# - *Cadastro de Cliente:*

# *O sistema deve permitir que o usuário "cadastre" o nome e a idade de até 3 clientes.*

# - *Reservas de Quartos:*

# ***O sistema deve oferecer 3 tipos de quartos:*** 

# ***"Simples", "Duplo" e "Luxo".***

# ***Cada cliente deve escolher um quarto para sua estadia.
# O preço da diária varia conforme o tipo de quarto:
# Simples: R$ 100,00 por dia.
# Duplo: R$ 150,00 por dia.
# Luxo: R$ 250,00 por dia.***

# - ***Cálculo da Estadia:***

# ***O usuário deve informar quantos dias cada cliente ficará no hotel.
# O sistema deve calcular o valor total da estadia para cada cliente, considerando o tipo 
# de quarto e a quantidade de dias.***

# Exemplo: 

#  ***valor_cliente3 = preco_duplo * cliente3_dias***

# *Pagamento:*

# *O sistema deve exibir o valor total a ser pago por cada cliente após a aplicação do desconto.*

# *Regras Adicionais:
# Utilize apenas variáveis, condicionais (if, elif, else) e listas para resolver o desafio.*