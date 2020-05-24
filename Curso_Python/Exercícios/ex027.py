# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
# Exemplo: Ana Maria de Souza
# primeiro: Ana
# Ultimo: Souza

nome = str(input('Digite um nome: ')).strip().split()
print('Seu primeiro nome é {} e seu ultimo nome {}'.format(nome[0].capitalize(), nome[len(nome)-1].capitalize()))