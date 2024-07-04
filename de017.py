#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# calcule e mostre o comprimento da hipotenusa
#Cateto oposto é a altura do triangulo retangulo, adjacente é a base dele, com os dois temos o angulo de 90 graus
# e a hipotenusa, que interliga estes pontos
#O quadrado da hipotenusa = a soma do quadrado da soma dos catetos
#pode usar módulos para esta solução
#from math import sqrt, pow, hypot
from math import hypot
co=float(input('Digite o comprimento do cateto oposto de um triângulo retângulo '))
ca=float(input('Agora, digite o comprimento de seu cateto adjacente '))
#hi=sqrt((pow(co,2))+pow(ca,2))
hi=hypot(co,ca)
print(f'O cateto oposto {co} x cateto adjacente {ca} equivale ao comprimento da hipotenusa que é {hi:.2f}')

