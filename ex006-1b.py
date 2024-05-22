n1=int(input('Digite um número :'))
n2=int(input('Digite outro número :'))
som=n1+n2
sub=n1-n2
div=n1/n2
din=n1//n2
res=n1%n2
mul=n1*n2

print('A soma é {}, a subtração é {}, a divisão normal é {:.3f},'.format (som, sub, div), end=' ')
print(f'a divisão inteira é {din}, o resto da divisão é {res} e a multiplicação é {mul}')
