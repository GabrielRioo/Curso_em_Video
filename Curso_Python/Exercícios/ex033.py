# Faça um programa que leia tres numeros e mostre qual é o maior e qual é o menor

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O maior numero é {} e o menor é {}'.format(maior, menor))

#
# if n1 > n2 and n1 > n3:
#     print('O maior numero é: {}'.format(n1))
# if n2 > n1 and n2 > n3:
#     print('O maior numero é: {}'.format(n2))
# else:
#     print('O maior numero é: {}'.format(n3))
