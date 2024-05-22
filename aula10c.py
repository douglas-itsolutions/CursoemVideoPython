nota1=float(input('Digite sua primeira nota: '))
nota2=float(input('Digita sua segunda nota: '))
média=(nota1+nota2)/2
print('Sua média é {:.1f}'.format(média))
if média>=7:
    print('Você passou!')
else:
    print('Não foi desta vez, estude mais')