#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira
#Ex: Digite um número: 6.124534. O número 6.124534 tem a parte inteira 6
#Dica olhar todas as funções do módulo Math
from math import trunc
n1=float(input('Digite algo '))
#print('Sua porção inteira é', trunc(n1))
#print('O valor digitado foi {} e sua porção inteira é {}'.format(n1, trunc(n1)))
print(f'O valor digitado foi {n1} e sua porção inteira é {trunc(n1)}')
#print(f'O valor digitado foi {n1} e sua porção inteira é {(int(n1))}')