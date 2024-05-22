#O mesmo professor do desafio anterior quer sortear a ordem de apresentação dos alunos. Faça um programa
# que leia o nome dos quatro alunos e mostre a ordem sorteada
#import random
from random import shuffle
nome1=str(input('Digite o nome do 1o. aluno '))
nome2=str(input('Agora, digite o nome do 2o. aluno '))
nome3=str(input('3o. aluno '))
nome4=str(input('e por último, digite o nome do 4o. aluno '))
lista=[nome1, nome2, nome3, nome4]
#random.shuffle(lista)
shuffle(lista)
print('A ordem de apresentação é :', lista)