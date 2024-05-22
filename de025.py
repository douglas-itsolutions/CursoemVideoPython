'''Crie um programa que leia o nome de uma pessoa e diga se ela tem SILVA no nome. True ou False'''
nome=str(input('Digite o seu nome ')).strip()
print(f'O nome informado tem "Silva" em seu sobrenome? ', 'Silva' in nome.title())