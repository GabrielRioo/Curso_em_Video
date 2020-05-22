#Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados.
# ex: Digite um numero: 1834
#unidade: 4 dezena: 3 centena: 8 milhar: 1
# como string e matematicamente

# num = str(input('Digite um numero entre 0 e 9999: '))
# print('Unidade: {}'.format(num[3]))
# print('Dezena: {}'.format(num[2]))
# print('Centena: {}'.format(num[1]))
# print('Milhar: {}'.format(num[0]))

num = int(input('Digite um numero entre 0 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))