# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidae de dias
# pelos quas ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 pr km rodado.

alugel = int(input('Quantos dias alugados? '))
rodado = int(input('Quantos km rodados? '))
total = (alugel * 60) + (rodado*0.15)
print('O total a pagar é e R${:.2f}'.format(total))