# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
av1 = float(input('Digite a nota da AV1: '))
av2 = float(input('Digite a nota da AV2: '))
media = (av1 + av2)/2
print('A média entre {0:.1f} e {1:.1f}: {2:.1f}'.format(av1, av2, media))