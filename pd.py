import pandas as pd   
import numpy as np    
import matplotlib.pyplot as plt

# Shift + Alt + ↓  COPIA A LINHA PARA A LINHA DE BAIXO


#To run code:
#use shortcut Ctrl+Alt+N
#or press F1 and then select/type Run Code,
#or right click the Text Editor and then click Run Code in editor context menu
#or click Run Code button in editor title menu
#or click Run Code button in context menu of file explorer
#To stop the running code:
#use shortcut Ctrl+Alt+M
#or press F1 and then select/type Stop Code Run
#or click Stop Code Run button in editor title menu
#or right click the Output Channel and then click Stop Code Run in context menu


print('Helo pandas')

#dados = pd.read_excel('C:/Users/ribei/OneDrive/Documentos/excel/arquivo1.xlsx')

#print(dados)

#print(dados.head())S

# KAGGLE SITE PARA CONJUNTO DE DADOS

dados2 = pd.read_csv("C:/Users/ribei/Downloads/athlete_events.csv/athlete_events.csv")
#print(dados2.describe())
dados3 = dados2.head(20) #CRIA UM NOVO DATAFRAME COM AS (5) PRIMEIRAS LINHAS
#print(dados3)
dados3.loc[dados3['NOC']=='USA']# FILTRA SOMENTE OS ATLETAS DOS EUA
#print(dados3.loc[dados3['NOC']=='USA']) 
dados2['City'].value_counts()# .VALUE_COUNTS MOSTRAR OS VALORES QUE EXISTEM NA COLUNA E QUNATAS VEZES CADA UM APARECEU
#print(dados2['City'].value_counts()) 
dados2.rename(columns={'Name':'Atleta'})# MUDAR O NOME DA COLUNA 'NAME' PARA 'ATLETA'
#print(dados2.rename(columns={'Name':'Athlete'})) 
#dados3.drop('ID', axis =1, inplace=True) #Excluir colunas
#print(dados3)
#dados2.hist(column='Weight',bins=100) # hist do pandas = HISTOGRAMAS
#plt.show() # matplotlib PARA CRIAR GRAFICOS
kmh = [40, 50, 60, 70, 80, 40, 50, 60, 70, 80 ,90, 100, 110, 120]
#plt.hist(kmh,bins=100) # para arrays
#plt.show()
#dados2.boxplot(column=['Age', 'Weight', 'Height']) # blox-plot
#plt.show()

dados4 = dados2.dropna() # QUALQUE LINHA QUE TENHA ALGUMA INFORMAÇÃO FALTANDO, SERA EXCLUIDA
#print(dados4.head(20))
#print(dados4.shape)
#print(dados2.shape)

pd.set_option('display.max_rows', None)  # Mostra todas as linhas
#pd.set_option('display.max_columns', None)  # Mostra todas as colunas (caso precise)

enulo = dados2.isnull() # SUBSTITUI OS DADOS POR TRUE PARA DADO FALTANTE E FALSE PARA DADO NAO FALTANTE
#print(enulo.head(100))
faltantes = dados2.isnull().sum() # REVELA QUANTOS DADOS FALTANTES EXISTEM EM CADA COLUNA DO DATAFRAME
#print(faltantes)
faltantes_percentual = (dados2.isnull().sum()/ len(dados2['ID']))*100 # REVELA O PERCENTUAL DE DADOS FALTANTES
#print(faltantes_percentual)
dados2['Medal'] = dados2['Medal'].fillna('No medal') # SUBSTITU TODOS OS DADOS FALTANTES DA COLUNA 'MEADA' PARA 'NO MEDAL'
dados2['Age'] = dados2['Age'].fillna(dados2['Age'].mean()) # SUBSTITUI TODOS OS DADOS FALTANTE DA COLUNA 'AGE' PARA A MEDIA DA COLUNA
dados2['Height'] = dados2['Height'].fillna(dados2['Height'].mean())
dados2['Weight'] = dados2['Weight'].fillna(dados2['Weight'].mean())
print(dados2.head(100))
faltantes = dados2.isnull().sum()
print(faltantes)
faltantes_percentual = (dados2.isnull().sum()/ len(dados2['ID']))*100
print(faltantes_percentual)


#Sex,Age,Height

# ALTURA E PESO DOS HOMENS
#atletasHomens= dados2.loc[ dados2['Sex']=='M']
#print(atletasHomens)
#alturaHomens= atletasHomens['Height']
#print(alturaHomens)
#pesoHomens= atletasHomens['Weight']
#print(pesoHomens)
#plt.scatter(alturaHomens,pesoHomens)# RELAÇAO ENTRE ALTURA E PESO DOS ATLETAS MASCULINOS 
#plt.show()


# Criando DATAFRAME com dictionary

alunos = {'Nome':['Kalleb','Thais','Ricardo','Isabel','Luiza','Joao','Isabele','Neymar'], 
          'Nota':[10.0,7.0,2.6,8.3,5.0,9.8,10.0,4.3],
          'Aprovado':['Sim','Sim','Não','Sim','Nao','Sim','Sim','Nao']}

dataframe = pd.DataFrame(alunos)

#print(dataframe)

# SAIDA (dataframe)
#        Nome    Nota Aprovado
#    0   Kalleb  10.0      Sim
#    1    Thais   7.0      Sim
#    2  Ricardo   4.6      Não
#    3   Isabel   8.3      Sim 

dataframe['Nome']
#print(dataframe['Nome']) #FILTRAR COLUNA

dataframe.loc[[0]] #FILTRAR LINHA
#print(dataframe.loc[0:2]) #FILTRAR INTERVALO DE LINHAS 0-1-2

dataframe.loc[ dataframe['Nome']=='Kalleb']
#print(dataframe.loc[ dataframe['Aprovado']=='Sim'])

alunosAprovados = dataframe.loc[ dataframe['Aprovado']=='Sim'] # CRIAR UM NOVO DATAFRAME APARTIR DE OUTRO
#print(alunosAprovados)
#print(dataframe.loc[dataframe['Nota']>=4]) #NOVO DATAFRAME >= 4 MAIOR OU IGUAL A 4 /<=4 MENOR/ != DIFERENTE/  ==4 IGUAL A 4 

objeto1 = pd.Series([1,2,3,4,5,6,])

#print(objeto1)

array1 = np.array([1,2,3,4,5,6])
array2 = np.array([(1,2,3,4,5,6),(7,8,9,10,11,12)])

objeto2 = pd.Series(array1)
#print(objeto2)

# SHAPE = DIZ QUANTAS LINHAS E COLUNAS (EM DATAFRAME)

#print(dataframe.shape)

# DESCRIBE = DESCREVE COLUNAS NUMERICAS
#           Nota
#count   4.00000 -> valores
#mean    7.47500 -> media
#std     2.27651 -> desvio padrao
#min     4.60000 -> valor min
#25%     6.40000 -> percentil
#50%     7.65000 -> percentil
#75%     8.72500 -> percentil
#max    10.00000 -> valor max

#print(dataframe.describe())


x=[1,2,3,4,5,6,7,8,9,10]
y=[1,2,3,4,5,6,7,8,9,10]

#plt.scatter(x,y)
#plt.show()

x1 = np.arange(0,1000,1) # CONSTRUA UM ARRAY DE 0 ATE 1000 DE 1 EM 1
#print(x1)

plt.plot(x1, x1**2)
#plt.show()