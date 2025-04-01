import numpy as np # type: ignore 

a = np.array([1, 2, 3 ])

#print (a)

b = np.array([(1,2,3,),(4,5,6,),(7,8,9)])

print (b)

c = np.zeros((4, 3))

print (c)

d = np.ones((4, 3))

print (d)

f = np.eye(4)

print (f)

print (b.max()) # MAIOR VALOR

print (b.sum()) # SOMA TOTAL

print (b.mean()) # MEDIA GERAL

print (b.std()) # DESVIO PADRAO

tela = np.array([(0,0,1,0,0,),(0,1,0,1,0),(1,0,0,0,1),(0,1,0,1,0),(0,0,1,0,0)])

print (tela)

math = np.array([0,1,2,3,4,5,6,7,8,9])

print (math*2)

lc = [x*10 for x in math]

print (lc)

aocubo = np.array([0,1,2,3,4,5,6,7,8,9])

cubo = [x**3 for x in aocubo]

print (aocubo)
print (cubo)

countmath=[]
lessmath=[]

for i in math:
  countmath.append(i+1)
  lessmath.append(i**2)
  print(countmath) 
  print(lessmath) 