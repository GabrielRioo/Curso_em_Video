#Desenvolva um programa que pergunte a distancia de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50
#por km para viagens de até 200km e R$0,45 para viagens mais longas

distancia = int(input('Qual adistancia da viagem? '))

if distancia <= 200:
    passagem = distancia * 0.50
    print('A sua passage irá custar: R${:.2f}'.format(passagem))
else:
    passagem = distancia * 0.45
    print('A sua passagem irá custar: R${:.2f}'.format(passagem))

# ou

preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('O preço da passagem é de {}'.format(preco))
