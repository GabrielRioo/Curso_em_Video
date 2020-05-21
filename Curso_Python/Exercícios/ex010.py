# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar
# Considere US$1,00 = R$ 3,27
# Dolar tá 5,59 em 21/05 ;-;

dinheiro = float(input('Quanto de dinheiro voce tem na carteira? R$'))
dolar = dinheiro / 3.27
print('Voce tem US${:.2f} dolares'.format(dolar))