lado_a = float(input('Digite o valor do lado A: '))
lado_b = float(input('Digite o valor do lado B: '))
lado_c = float(input('Digite o valor do lado C: '))

if lado_a < lado_b+lado_c and lado_b < lado_a + lado_c and lado_c < lado_b + lado_a:
    print('É um triangulo')

    if lado_a == lado_b  == lado_c:
        print('É um triângulo equilátero')
    elif lado_a == lado_b or lado_b == lado_c or lado_c == lado_a:
        print('É um triângulo de isóceles')
    elif lado_a != lado_b and lado_b != lado_c and lado_c != lado_a:
        print('É um triângulo escaleno')
else:
    print('Não é um triângulo')


