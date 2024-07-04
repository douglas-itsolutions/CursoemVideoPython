#crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
#Considere US$ 1.00 = R$ 3,27
d1=float(input(' Quanto dinheiro você tem em sua carteira? R$ '))
d2=d1/(3.27)
#print('Com este valor você consegue comprar', d2, 'dólares')
print('Com R$ {:.2f} você consegue comprar US$ {:.2f} dólares'.format(d1, d2))