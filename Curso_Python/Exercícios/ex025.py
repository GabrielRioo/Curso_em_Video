# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome
# Em qualquer lugar tenha o silva. Retornar true ou false

nome = str(input("Digite o seu nome: ")).strip().upper()
print('SILVA' in nome, "\n", nome)

#OU

print('SILVA' in nome.upper())