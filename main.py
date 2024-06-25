'''Progama que le valores de produtos e soma o total 
alem de contar quantos produtos forma mais de mil reais.'''


total_gasto = 0
qnt_produto_mil = 0

while True:
    print(f'1. Adiconar produto \n2. Sair')

    op = input('Digite a opção desejada: ')
    match op:
        case '1':
            print(f'\nCadastrando novo produto!')
            valor = int(input('Digite o valor do produto: '))
            
            total_gasto += valor
            if valor >= 1000:
                qnt_produto_mil += 1
        case '2':
            print(f'Encerrando Execução')
            break
        case _:
            print(f'Opção Inválida')



print(f'Total gasto: R${total_gasto}')
print(f'A quantidade de produtos acima de mil: {qnt_produto_mil}')