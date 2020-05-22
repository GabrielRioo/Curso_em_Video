# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras em maiusculo
# O nome com todas minusculas
# Quandas letras ao Total(sem considerar espaços)
# Quantas letras tem o primeiro nome

nome = str(input('Digite o seu nome completo: ')).strip() # ja corta os espaços iniciais e finais
print('Nome em maisuculo: {}'.format(nome.upper()))
print('Nome em minusculo: {}'.format(nome.lower()))
print('Seu nome tem: {} letras'.format(len(nome) - nome.count(' '))) # Conta quantos caracteres e diminui dos espaços

print('Seu primeiro nome tem: {} letras'.format(nome.find(' '))) # primeiro espaço
# OU
separa = nome.split()
print('Seu primeiro nome é {}, e tem: {} letras'.format(separa[0], len(separa[0])))