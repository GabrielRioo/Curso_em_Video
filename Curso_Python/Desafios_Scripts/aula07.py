# nome = input('Digite o seu nome: ')
# print('Prazer em te conhecer {:20}!'.format(nome))
# print('Prazer em te conhecer {:>20}!'.format(nome))
# print('Prazer em te conhecer {:<20}!'.format(nome))
# print('Prazer em te conhecer {:^20}!'.format(nome))
# print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
print('A soma é {}'.format(n1+n2))
s = n1 + n2
m = n1 * n2
d = n1 / n2
p = n1 ** n2
print('A soma é {0} \nA multiplicação é {1} \nA divisão é {2} \nA potencialização é {3}'.format(s,m,d,p), end=' ')
print('Aqui não quebrou linha')