#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
#lendo o nome deles e escrevendo o que foi escolhido
#import random
from random import choice
nome1=str(input('Digite o nome do 1o. aluno '))
nome2=str(input('Agora, digite o nome do 2o. aluno '))
nome3=str(input('3o. aluno '))
nome4=str(input('e por último, digite o nome do 4o. aluno '))
#alunos= nome1, nome2, nome3, nome4
lista=[nome1, nome2, nome3, nome4]
#print('O aluno escolhido foi ', random.choice(lista))
print('O aluno escolhido foi ', choice(lista))
#print('O aluno escolhido foi ', random.choice(alunos))