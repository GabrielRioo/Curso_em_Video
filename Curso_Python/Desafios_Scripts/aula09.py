frase = '   Curso em Video Python'
print(frase[3])
print(frase[3:13])
print(frase[:14])
print(frase[15:])
print(frase[3:14:2])
print(frase[2::])
print(frase.count('o'))
print(frase.upper().count('o'))
print(len(frase))
print(len(frase.strip()))
print(frase.replace('Python', 'Android'))
print('Android' in frase)
print(frase.find('Curso'))
print(frase.find('Android'))
print(frase.split())
dividido = frase.split()
print(dividido[0][3]) # Pega o primeiro item e mostra a quarta letra dele


print("""\nfazendo o teste
das 3 aspas para
printar um texto
com varias linhas""")