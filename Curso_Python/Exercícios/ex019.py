# Um professor que sortear um dos seus quatro alunos para apagar o quadro. Faça um pregraa que ajude ele, lendo o nome
# deles e escrevendo o nome do escolhido

from random import choice

n1 = str(input('Digite o primeiro nome: '))
n2 = str(input('Digite o segundo nome: '))
n3 = str(input('Digite o terceiro nome: '))
n4 = str(input('Digite o quarto nome: '))
lista = [n1, n2, n3, n4]
print('O aluno sorteado foi: {}'.format(choice(lista)))