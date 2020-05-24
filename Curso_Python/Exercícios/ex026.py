# Faça um programa que leia um frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A".
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a ultima vez.

frase = str(input('Digite uma frase: ')).strip().upper()
print('A frase contem {} letras "A", sua primeira letra "A" se encontra no indice {} e a ultima {}'.format(frase.count('A'), frase.find('A')+1,frase.rfind('A')+1 ))