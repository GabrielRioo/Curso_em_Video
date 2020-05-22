# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo,calcule e mostre o comprimento da hipotenusa
from math import hypot

catOposto = float(input('Digite o cateto oposto: '))
catAdjacente = float(input('Digite o cateto adjacente: '))
hipo = hypot(catAdjacente, catOposto)
print('A hipotenusa do triangulo é: {:.2f}'.format(hipo))

# OU

hipotenusa = (catOposto ** 2 + catAdjacente ** 2) ** (1/2)
print('A hipotenusa do triangulo é: {:.2f}'.format(hipotenusa))