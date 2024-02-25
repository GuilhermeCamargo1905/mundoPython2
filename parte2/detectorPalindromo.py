pali = input('Digite uma palavra: ').upper()

frase_dividida = pali.split()
frase_junta = ''.join(frase_dividida)

frase_invertida = ''

for cont in range(len(frase_junta) -1, -1, -1):
    frase_invertida += frase_junta[cont]

print(f'Palavra Junta: {frase_junta}')
print(f'Palavra Invertida: {frase_invertida}')