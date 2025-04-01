dicionario = {'Curso':'Python para ML',
              'Produtor':'Eu',
              'Preço':'Free',
              'Nota':10}

#CHAVE:VALOR --> {}

print (dicionario['Curso'])

print (dicionario['Nota'])

a = dicionario['Preço']

print (a)

dicionario['Preço'] = 'R$300,00'

print (dicionario['Preço'])

print (dicionario)

dicionario.keys()

frase = 'Eu estou gostando do curso'

print (frase)

print (frase[2:])

print (frase[2:14])

print (frase[2:24:2]) #COMEÇA NO 2 ATE O 24 DE 2 EM 2

print (frase.count('t')) # -- COUNT -- CONTA QUANTOS 'T'

print (frase.count('o'))

print ('O tamanho da frase é =',len(frase)) # -- LEN -- CONTA O TAMANHO

print (frase.replace('curso','assunto'))

