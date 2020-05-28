# Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.
# Para salarios superiores a R$1250,00, calcule um aumento de 10%
# Para as inferiores ou iguais, o aumento é de 15%

salario = float(input('Qual é o seu salário? '))
if salario >= 1250:
    aumento = salario * 0.10
    print('O seu salário com aumento é: {}'.format(aumento + salario))
else:
    aumento = salario * 0.15
    print('O seu salário com aumento é {}'.format(aumento + salario))