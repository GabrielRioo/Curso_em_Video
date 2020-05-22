# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo
from math import sin, cos, tan,radians

num = int(input('Digite um angulo: '))

print('O angulo de {} tem o SENO de {:.2f}'.format(num, sin(radians(num))))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(num, cos(radians(num))))
print('O angulo de {} tem o TANGENTE de {:.2f}'.format(num, tan(radians(num))))


