# Escreva um programa que leia a velocidade de um carro
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ee foi multado
# A multa vai custar R$7,00 por cada km acima do limite

velocidade = int(input('Informe a velocidade do seu carro: '))
multa = (velocidade - 80) * 7
if velocidade >= 80:
    print('Voce foi multado! Voce estava a: {}km/h. Terá que pagar: R${:.2f}'.format(velocidade, multa))
print('Voce esta a {}jkm/h, tenha um bom dia!'.format(velocidade))
