# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
produto = float(input('Qual é o preço do produto: R$'))
desconto = produto * 0.05
print('O valor do desconto é R${}, o produto com desconto sai por: R${}'.format(desconto, produto-desconto))