#Escreva um programa que leia três números e mostre qual é o maior e qual é o menor
n1 = int(input('Digite o 1o. número: '))
n2 = int(input('Digite o 2o. número: '))
n3 = int(input('Agora, digite o 3o. e último número: '))
'''if n1>n2 and n1>n3:
    print(n1, 'é o maior')
if n2>n1 and n2>n3:
    print(n2, 'é o maior')
if n3>n1 and n3>n2:
    print(n3, 'é o maior')
if n1<n2 and n1<n3:
    print(n1, 'é o menor')
if n2<n1 and n2<n3:
    print(n2, 'é o menor')
if n3<n1 and n3<n2:
    print(n3, 'é o menor')'''
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

print('O maior valor digital é ', maior)
print('O menor valor digital é ', menor)
