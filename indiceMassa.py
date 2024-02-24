altura = float(input('Digite a sua altura: '))
peso = float(input('Digite o seu peso: '))

print('Sua altura é {:.2f}m e você pesa {:.2f}kg'.format(altura,peso))

imc = float(peso / (altura ** 2))

if imc < 18.5:
    print('Você está abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Você está no peso ideal')
elif imc >= 25 and imc < 30:
    print('Você está com sobre peso')
elif imc >= 30 and imc < 40:
    print('Você está obeso')
else:
    print('Você está com obesidade mórbida')
