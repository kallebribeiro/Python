Lista1 = [1, 2, 3]
type(Lista1)

print (Lista1)
print (Lista1 [0])

Lista2 = [[1, 2 ,3], [4, 5, 6], [7, 8, 9]]

print (Lista2 [0] [1])

Lista3 = ['Óla', 'Oi',]

print (Lista3)
print (Lista3 [0])

select = Lista2[1]

print (select)

print (type(select))

Alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

print (Alfabeto)

print ([Alfabeto[:17]])

print ([Alfabeto[10:20]])

import random

cidades = ['São Paulo', 'Rio de Janeiro', 'Paris', 'New York', 'Tokyo']

escolhida = random.choice(cidades)

print ('A cidade sorteada foi: ' + escolhida)

a = [1, 2, 3]

a.append(4)

print (a)

b = [7, 8 , 9]

for item in b:
    a.append(item) 
    
print (a)

x = [2,4,10,6]

print (x)

z = []

for i in x:
    z.append(float(i))

print (z)


p = [2,3,4,5]

print (p)

p[0] = 1093

print (p)

tuple = (1,2,3,4,5)

print (tuple)

# tuple[0] = 1782 

# Uma tuple é uma lista criada com () e diferente da lista normal com [], a tuple é imutável 

Carro = ['Uno', 'Onix', 'Renegade', '911', 'Camaro', 'Seal', 'Corolla']

CarroSorteio = random.choice(Carro)

print (Carro)

print (Carro[1:4])

print (CarroSorteio)
