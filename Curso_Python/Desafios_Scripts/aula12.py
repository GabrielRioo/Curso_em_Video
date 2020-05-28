nome = str(input('Digite o seu nome: '))
cores = {'branco':'\033[30m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m',
         'azul':'\033[34m',
         'roxo':'\033[35m',
         'ciano':'\033[36m',
         'cinza':'\033[37m',
         'limpa':'\033[m'}
if nome == 'Gabriel':
    print(cores['verde'], 'Que nome bonito!', cores['limpa'])
elif nome == 'Leonardo' or nome == 'matheus' or nome == 'Camila':
    print(cores['ciano'], 'Seu nome é muito popular no Brasil!', cores['limpa'])
else:
    print(cores['vermelho'], 'Seu nome é bem normal.', cores['limpa'])
print(cores['roxo'], 'Tenha um bom dia, {}{}!'.format(nome, cores['limpa']))