# Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada
n = int(input('Digite um numero: '))
dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)
print('O dobro é {0} \nO triplo é {1} \nA raiz é {2:.0f}'.format(dobro, triplo, raiz))
# ou
print('O dobro é {}, o triplo é {}, a raiz é {:.0f}'.format((n*2), (n*3), (n**(1/2))), end=' ')
print('<3')