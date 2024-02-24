prova1 = float(input('Digite a sua nota na primeira prova: '))
prova2 = float(input('Digite a sua nota na segunda prova: '))

media = float((prova1 + prova2) / 2)

if media < 5.0:
    print('Sua média foi {:.1f} e por isso foi REPROVADO'.format(media))
elif media > 5.0 and media <= 6.9:
    print('Sua média foi {:.1f} e por isso você está de RECUPERAÇÃO'.format(media))
else:
    print('Sua média foi {:.1f} você foi APROVADO'.format(media))