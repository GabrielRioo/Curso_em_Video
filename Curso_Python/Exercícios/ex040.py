# Crie um programa que leia duas notas de um aluno e calcule sua média. mostrando uma mensagem no final, de acordo com a
# média atingida: Média abaixo de 5: Reprovado. Média entra 5 e 6.9: Recuperação. Média 7 ou superior: Aprovado.

av1 = float(input('Digite a nota da AV1: '))
av2 = float(input('Digite a nota da AV2: '))
media = (av1 + av2) / 2
color = {
    'limpar':'\033[m',
    'vermelho':'\033[31m',
    'verde':'\033[32m',
    'amarelo':'\033[33m'
}
if media < 5:
    print(color['vermelho'], 'Você está reprovado!')
elif media >= 5 and media < 7:
    print(color['amarelo'], 'Você está de recuperação!')
else:
    print(color['verde'], 'Você está aprovado!!')