# Crie um programa que leia um numero inteiro qualquer e mostre na tela se ele é PAR ou IMPAR

n = int(input('Digite um numero: '))
if n % 2 == 0:
    print('O numero {} é PAR'.format(n))
else:
    print('O numero {} é IMPAR'.format(n))