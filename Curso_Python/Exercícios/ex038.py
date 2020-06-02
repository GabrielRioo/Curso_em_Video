# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem: O primeiro valor é
# Maior. O segundo valor é Maior. Não existe valor maior, os dois são iguais

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite o segundo numero: '))
color = {
    'limpa':'\033[m',
    'vermelho':'\033[31m',
    'verde':'\033[32m'
}

if n1 == n2:
    print("\033[33mOs numeros são iguais!")
elif n1 > n2:
    print('{}O numero {} é maior que {}'.format('\033[32m', n1, n2))
else:
    print('\033[32mO numero {}{}{} {}é maior que {}'.format(color['vermelho'], n2,color['limpa'], color['verde'], n1))