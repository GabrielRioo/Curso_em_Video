# Excreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
n = float((input('Digite um numero: ')))
print('A medida de {}m corresponde a: '.format(n))
print('{}km \n{}hm \n{:.1f}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format((n*0.001), (n*0.01), (n*0.1), (n*10), (n*100), (n*1000)))