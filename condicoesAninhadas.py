nome = str(input('Digite o seu nome: '))
if nome == 'Guilherme':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Ana' or nome == 'Lucas':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Maria Cluadia Jessica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}'.format(nome))