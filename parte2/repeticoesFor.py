#for c in range(0, 7, 2):
#    print(c)
#Caso queremos fazer uma contagem regrssiva adicionamos mais um parametro , -1 ou +1

"""
"n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('FIM')
"""

"""
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('Fim')
"""
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores foi {}'.format(s))