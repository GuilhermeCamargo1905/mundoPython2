n1 = int(input('Digite o primeiro termo da P.A: '))
razao = int(input('Digite a razao da P.A: '))
decimo = n1 + (10 - 1) * razao

for i in range(n1,decimo + razao, razao):
    formula = n1 + razao

    print(i, end=' --> ')
print('FIM')

'''
a variavel 'decimo' é responsavel por fazer a PA até o décimo termo
ou seja, calcula o decimo termo da PA. na estrutura do for , ele vai do n1 
que é o numero que o usuario digitou, até o decimo termo + a razao, eu fiz + a razao
pelo fato de que o python sempre para um numero antes, ou seja ele vai só ate o numero 9
entao fazendo + a razao, ele faz ate o decimo termo.

e por ultimo na parte da razão, é o quanto ele vai pulando, ou seja se a razao for 3 
ele faz a PA de 3 em 3, se for 5, ele faz a PA de 5 em 5, e assim por diante.
'''