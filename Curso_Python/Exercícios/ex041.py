# A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# categroia, de acordo com a idade: Até 9 anos: Mirim. Até 14 anos: Infantil. Até 19 anos: Junior. Até 20 anos: Sênior.
# Acima: Master.

from datetime import date

dia = int(input('Digite o dia do seu nascimento: '))
mes = int(input('Digite o mes do seu nascimento: '))
ano = int(input('Digite o ano do seu nascimento: '))
print('Sua data de nascimento é: {}/{}/{}'.format(dia, mes, ano))

print(int(date.today-ano))
