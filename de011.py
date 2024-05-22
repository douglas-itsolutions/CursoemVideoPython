#Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e
# a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²
largura=float(input('Digite a largura da parede em metros '))
altura=float(input('Agora, digite a altura da parede, também em metros '))
área=largura*altura
tinta=área/2
#print(f'Você precisará de ', t1, 'litros de tinta para pintar uma área de ', a2, 'm²')
print('Sua parede tem a dimensão de {:.2f} x {:.2f} e sua área é de {:.2f} m²'.format(largura,altura,área))
print('Você precisará de {} litros de tinta para pintá-la!'.format(tinta))