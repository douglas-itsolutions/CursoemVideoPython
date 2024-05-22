'''Crie um programa que leie o nome completo de uma pessoa e mostre:

- O nome com todas as letras maiúsculas
- O nome com todas as letras minúsculas
- Quantas letras ao todo sem considerar espaços
- Quantas letras tem o primeiro nome'''
nome=str(input('Por favor, digite seu nome ')).strip()
nomedividido=nome.split()
print(f'Seu nome {nome} em maiúsculo fica ', nome.upper())
print(f'já seu nome {nome} em minúsculo ', nome.lower())
print(f'Seu nome {nome} têm ', len(nome), 'letras')
#print('Retirando espaços, seu nome possui ', len(''.join(nomedividido)), 'letras')
print('Retirando espaços, seu nome possui ', len(nome) - nome.count(' '))
print('Seu primeiro nome tem ', len(nomedividido[0]), 'letras')
#print(len(''.join(nomedividido)))
