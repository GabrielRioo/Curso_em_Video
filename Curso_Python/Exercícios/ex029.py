# Escreva um programa que leia a velocidade de um carro
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ee foi multado
# A multa vai custar R$7,00 por cada km acima do limite

velocidade = int(input('Qual a velocidade atual do carro? '))
multa = float(7)
if velocidade >= 80:
    print('Você foi multado por dirigir acima de 80km/h. Sua velocidade: {}km/h'.format(velocidade))
    multa = (velocidade - 80) * 7
    print('Sua multa foi de R${:.2f}'.format(multa))
else:
    print('Sua velocidade é: {} .Tenha um bom dia e dirija com segurança!'.format(velocidade))