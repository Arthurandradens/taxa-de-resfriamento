import matplotlib.pyplot
import math

#Constante de resfriamento
k = 0.1
#Temperatuda inicial do objeto
T = 80
#Temperatura ambiente
Ta = 25
#tempo que vai multiplicar a constante de resfriamento
t = 5

#def calcular_exponencial_negativa():
 #   resultado = math.exp(-0.5)
  #  return resultado

derivada = -k * (T - Ta) * math.exp(-k * t)

grafico = [t,T,derivada]
print((derivada))

matplotlib.pyplot.xlabel("Taxa de resfriamento(minuto)")
matplotlib.pyplot.ylabel("Temperatura Máxima(Graus C")
matplotlib.pyplot.plot(grafico)

matplotlib.pyplot.show()
