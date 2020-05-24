# nome = str(input('Qual é o seu nome? '))
# if nome == 'Gabriel':
#     print('Que nome lindo você tem!')
# else:
#     print('Que nome feio!')
# print('Bom dia {}!'.format(nome))

n1 = float(input('Digite a AV1: '))
n2 = float(input('Digite a AV2: '))
media = (n1 + n2) / 2
print('A sua media foi {:.1f}'.format(media))
if media >= 6:
    print('Sua media está boa')
else:
    print('Sua media eta um coco')
print('PARABENS!!' if media >= 6 else 'ESTUDA MAIS GARAI!')