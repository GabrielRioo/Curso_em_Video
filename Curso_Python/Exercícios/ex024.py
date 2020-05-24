# Crie um programa que leia o nome de uma cidade  diga se ela começa ou nao com o nome 'SANTO'

cidade = str(input('Digite o nome de uma cidade: ')).strip()
cidade = cidade.lower()
print('santo' in cidade)

#OU

print(cidade[:5].upper() == 'SANTO')
