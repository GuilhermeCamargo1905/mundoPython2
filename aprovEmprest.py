valor = float(input('Qual o valor da casa que você deseja comprar? '))
salario = float(input('Qual o seu salário? '))
anos = int(input('Em quantos anos você deseja pagar? '))

tempo = anos * 12
valor_mensal = valor / tempo

print('Para pagar uma casa com esse valor de {:.2f} em {} anos as parcelas serão de {:.2f}'.format(valor,anos,valor_mensal))

if valor_mensal < 30 / 100 * salario:
    print('Emprestimo aprovado')
else:
    print('Emprestimo negado')