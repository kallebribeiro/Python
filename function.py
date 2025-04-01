def somaQuadrados(a,b):
    somaQ = a**2 + b**2
    return somaQ

#print (somaQuadrados(7,9))

somaQuadrados2 = lambda a, b: a**2 + b**2

#print (somaQuadrados2(17,21))

x = lambda f:f/2

#print (x(19))

w = lambda t,y,u: t*y*u-t+u

#print (w(27,75,21))

kmh = [40, 50, 60, 70, 80 ,90, 100, 110, 120]

mph = []

for i in kmh:
    mph.append(i/1.61)
    
#print (mph)

mph2 = list(map(lambda x: x/1.61, kmh)) # MAP

#print (mph2)

mph3 = [x/1.61 for x in kmh]  # LIST COMPREHENSION
#print (mph3)

caracters = [i for i in 'Didática do dia']
#print (caracters)

lc = [x*7 for x in [2, 300, 400]]
#print (lc)

# DEF PARA FUNCAO
def teste(v,i):
    valor = v
    incremento = i
    resultado = valor + incremento
    return resultado

a = teste(10,27)
b= teste(273,7)

#print(a)
#print(b)


# ESCREVER FUNCAO COM LETRA MINUSCULA carro_parado E MAIUSCULA PARA CLASSES CarroParado

# CLASSES E METODOS  --- METODO = FUNCAO DENTRO DE UMA CLASSE --- ATRIBUTO = VARIAVEL DENTRO DE UMA CLASSE

class Classe0:
    def incrementa(self, v, i): # SELF DEVE SER COLOCADO DENTRO DE UMA FUNCAO QUE ESTEJA DENTRO DE UMA CLASSE
        valor = v
        incremento = i
        resultado = valor + incremento
        return resultado

a = Classe0()
#print(a)
b = a.incrementa(10, 1)
#print(b)
c = Classe0().incrementa(32, 21)
#print(c)

class Classe0:
    def incrementa(self,v,i):
        self.valor = v
        self.incremento = i
        self.resultado = self.valor + self.incremento
        return self.resultado
    
a = Classe0() # COM O SELF AGORA O ( a ) RECEBE OS VALORES a.valor/a.incremento/a.resultado
b = a.incrementa(21,1)
#print(b)
#print(a.valor)
#print(a.incremento)
#print(a.resultado)

# METODO CONTRUTOR INIT ADICIONA OS ATRIBUTOS PARA TODA A CLASSE E NAO SO PARA O METODO INCREMENTA

class Classe0:
    def __init__(self, v: int, i:int):
        self.valor = v
        self.incremento = i
    def incrementa(self):
        self.valor += self.incremento
        
a = Classe0(10,1) # OBJETO A
a.incrementa()
#print(a.valor)
b = Classe0(10,1) # OBJETO B
b.incrementa()
#print(b.valor)


class Classe0:
    def __init__(self, v=10, i=1): # COM VALOR PADRAO CASO NENHUM VALOR SEJA PASSADO
        self.valor = v
        self.incremento = i
    def incrementa(self):
        self.valor += self.incremento

a = Classe0()
a.incrementa() # DEPOIS DE INSTANCIARMOS a = Classe0(), QUANDO EXECUTAMOS a.incrementa(), O QUE O INTERPRETADOR ESTA FAZENDO E: Classe0().incrementa(a, 10, 1)
#print(a.valor)
#print(a.incremento)


class Class:
    def __init__(self, v=10, i=1):      
        self.valor = v                  # ATRIBUTO
        self.incremento = i             # ATRIBUTO
        self.valor_exponencial = v      # ATRIBUTO
    def incrementa(self):               # FUNCAO
        self.valor += self.incremento
    def verifica (self):
        if self.valor > 12:
            print("Ultrapassou 12 :(")
        else:
            print("Nao ultrapassou 12")
    def exponencial(self, e):
        self.valor_exponencial = self.valor**e  # O VALOR FOI SALVO EM self.valor_exponencial
    def incrementa_quadrado(self):
        self.incrementa()
        self.exponencial(2)

a = Class()
a.incrementa()
#print(a.valor)
a.exponencial(3)
#a.verifica()
#print(a.valor_exponencial)
a.incrementa_quadrado()
#print(a.valor_exponencial)

b = Class(50,5)
b.incrementa()
#print(b.valor)
#b.verifica()
b.exponencial(2)
#print(b.valor_exponencial)
b.incrementa_quadrado()
#print(b.valor_exponencial)

# HERANÇA, CRIAR CLASSE QUE DEPENDE DE OUTRAS

class Calculos(Class): # ABSORVE AS FUNCOES DA CLASSE MAE
    pass

c = Calculos()
c.incrementa()
#print(c.valor)
#c.verifica()
c.exponencial(3)
#print(c.valor_exponencial)
c.incrementa_quadrado()
#print(c.valor_exponencial)

class Calculos(Class):
    def decrementa(self):
        self.valor -= self.incremento 
        
d = Calculos(20,20)
d.incrementa()
#print(d.valor)
d.decrementa()
#print(d.valor)

class Calculos(Class):
    def __init__(self, d=5):# COMO UM NOVO INIT FOI ADICIONADO SUBSTITUIU O ATRIBUTO VALOR
        super().__init__(v=10, i=1) # INVOCANDO A SUPER CLASSE = super() --- INVOCANDO O METODO INIT DA SPCLASSE .__init__()
        self.divisor = d
    def decrementar(self):
        self.valor -= self.incremento
    def divide(self):
        self.valor /= self.divisor
        
e = Calculos()
e.incrementa()
print(e.valor)
e.decrementar()
print(e.valor)
e.divide()
print(e.valor)