valor_produto = float(input('Digite o valor a ser pago da compra: '))


print('[1] : A vista no dinheiro ou no cheque vc ganha 10% de desconto\n'
      '[2] : A vista no cartão você ganha 5% de desconto\n'
      '[3] : Em até 2x no cartão o produto sai pelo preço normal\n'
      '[4] : Em 3x ou mais no cartão o produto tem 20% de juros')
print('\n')

num = int(input('Digite o numero correspondente a opção desejada: '))

if num == 1:
    calc = valor_produto - (valor_produto * 10 / 100)
elif num == 2:
    calc = valor_produto - (valor_produto * 5 / 100)
elif num == 3:
    calc = valor_produto
    parcela = valor_produto / 2

    print('A sua compra será parcelada em 2x saindo com um valor de {}'.format(parcela))
    print()
elif num == 4:
    calc = valor_produto + (valor_produto * 20 / 100)
    parcela = int(input('Em quantas parcelas você deseja parcelar? '))

    print()

    novo_preco = calc / parcela
    print('Você parcelou em {} vezes logo cada parcela tem o valor de {:.2f}'.format(parcela, novo_preco))
    print()
print('Como você escoçlheu a opção {} , o produto saira pelo valor de {}'.format(num,calc))
