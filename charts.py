import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-1000, 1000, 1)
y = x**2
print(x)
#plt.plot(x,y)
#plt.show()


y1 = x**2
y2 = x**3
y3 = -x**2
y4 = -x**3

#plt.subplot(2,2,1) # SUBPLOT PARA MAIS DE UM GRAFICO/ DIVISAO DA ARE DE GRAFICOS = ( LINHAS = 2,COLUNAS = 2, ONDE A FIGURA SERA ALOCADA = 1 (QUADRANTE))
#plt.plot(x, y1)
#plt.subplot(1,2,2)
#plt.plot(x, y2)
#plt.subplot(2,2,3)
#plt.plot(x, y3)
#plt.subplot(2,2,4)
#plt.plot(x, y4)
#plt.show()

#figura = plt.figure(figsize=(10,10)) # CONFIGURA O TAMANHO DA janela

#figura.add_subplot(2,2,1) # SUBPLOT PARA MAIS DE UM GRAFICO/ DIVISAO DA ARE SDE GRAFICOS = ( LINHAS = 2,COLUNAS = 2, ONDE A FIGURA SERA ALOCADA = 1 (QUADRANTE))
#plt.plot(x, y1)
#figura.add_subplot(2,2,2)
#plt.plot(x, y2)
#figura.add_subplot(2,2,3)
#plt.plot(x, y3)
#figura.add_subplot(2,2,4)
#plt.plot(x, y4)
#plt.show()

y=[y1, y2, y3, y4]

figura = plt.figure(figsize=(10,10))
for i in range(4):
    figura.add_subplot(2,2,i+1)
    plt.plot(x,y[i])
plt.show()

from skimage.io import imread  # PARA ABRIR IMAGENS
image = imread('')
plt.imshow(image)
plt.show()

# PARA MOSTRAR TODAS AS IMAGENS DE UMA VEZ
endereco = ''
imagens = []
for i in range(3):
    imagem = imread(endereco +'ps'+str(i+1)+'.jpg')
    imagens.append(imagem)
    
figura = plt.figure(figsize=(15,8))
for i in range (3):
    figura.add_subplot(3,1,i+1)
    plt.imshow(imagens[i])
plt.show()