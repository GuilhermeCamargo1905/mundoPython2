num = int(input('Digite um numero: '))
total = 0

for c in range(1, num + 1):
    if num % c == 0:
        total += 1
    else:
        print(f'{c}', end=' ')

if total == 2:
    print('\nO numero {} é divisivel por {} valores logo é primo'.format(num, total))
else:
    print('\nO numero {} é divisivel por {} valores logo não é primo'.format(num, total))