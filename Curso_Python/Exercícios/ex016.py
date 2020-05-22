# Crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua porção inteira
# Ex: Digite um numero: 6.127, o numero 6.127 tem a parte inteira 6.

num = float(input('Digite um numero: '))
print('O numero digitado foi {} e em inteiros é: {}'.format(num, int(num)))

# OU
from math import trunc
print('O numero digitado foi {} e em inteiros é: {}'.format(num, trunc(num)))
