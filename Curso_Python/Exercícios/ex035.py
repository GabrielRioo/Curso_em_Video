# Desenvolva um programa que leia o comprimeto de tres retas e diga ao usuario se elas podem ou nao formar um triangulo

print('-=-'*20)
print('Analisador de Triangulos')
print('-=-'*20)
r1 = float(input('Digite o comprimento da primeira reta '))
r2 = float(input('Digite o comprimento da segunda reta '))
r3 = float(input('Digite o comprimento da terceira reta '))
if r1 < r2 + r3 and r2 < r1 + r3:
    print('Os segmentos podem formar um triangulo!')
else:
    print('Os segmentos nao podem formar um triangulo!')