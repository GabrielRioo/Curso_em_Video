# 	Codigo:
# \033[0;33;44m
# Type:
# 0 - none
# 1 - bold
# 4 - underline
# 7 - Negative
# Text / Background
# 30 / 40- branco
# 31 / 41 - vermelho
# 32 / 42 - verde
# 33 / 43 - amarelo
# 34 / 44 - azul
# 35 / 45 - roxo
# 36 / 46 - ciano
# 37 / 47 - cinza


# \033[1;35;43m
# \033[30;42m
# \033[m
# \033[7;30m
print('\033[0;30;41m Olá, Mundo!')
print('\033[4;33;44m Olá, Mundo!')
print('\033[1;35;43m Olá, Mundo!')
print('\033[30;42m Olá, Mundo!')
print('\033[m Olá, Mundo!')
print('\033[7;30m Olá, Mundo!')
print('\033[0;30;41m Olá Mundo! \033[m')
print('\033[0;30;41m Olá, Mundo!\033[m')
print('\033[4;33;44m Olá, Mundo!\033[m')
print('\033[1;35;43m Olá, Mundo!\033[m')
print('\033[30;42m Olá, Mundo!\033[m')
print('\033[m Olá, Mundo!\033[m')
print('\033[7;30m Olá, Mundo!\033[m')
print('\033[30m Olá, Mundo!')
print('\033[31mOlá, Mundo!\033[m')

a = 3
b = 4
nome = 'Gabriel'
print('Os valores são \033[31m{}\033[m e \033[32m{}\033[m'.format(a, b))
print('Olá, muito prazer emt e conhecer {}{}{}'.format('\033[4;34m', nome, '\033[m'))

cores = {'limpa':'\033[m', 'azul':'\033[34m', 'amarelo':'\033[33m'}
print('Olá, muito prazer emt e conhecer {}{}{}'.format(cores['amarelo'], nome, cores['limpa']))
