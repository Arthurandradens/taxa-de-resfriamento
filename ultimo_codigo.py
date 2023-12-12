import matplotlib.pyplot as plt
import numpy as np

#Derivada de Newton:
#T(t)=Ta +(T0−Ta)⋅e−kt

#Constante de resfriamento
k = 0.1
#Temperatuda inicial do objeto
T = 80
#Temperatura ambiente
Ta = 25
#tempo que vai multiplicar a constante de resfriamento
t = 61

lista_tempo = list(range(t))#Cria uma lista de tempo que vai de acordo com o tempo(t)
lista_temperatura = np.zeros(t)#cria uma lista de zeros que vai de acordo com o tempo(t)
lista_temperatura[0] = T#Define que o primeiro valor da lista vai ser a temperatura inicial(T)

i = 1 #Valor de inicio do loop
#Cálculo da derivada de newton que calcula a taxa de resfriamento de um objeto com base no tempo
while i < t:
  lista_temperatura[i] =Ta + (T - Ta) * np.exp(-k * i)#Converte o logaritmo para um número real
  i +=1

print(lista_temperatura)


plt.figure(figsize=(10, 10))#Define o tamanho do gráfico
plt.plot(lista_tempo, lista_temperatura, label='Temperatura do objeto')
plt.axhline(y=Ta, color='r', linestyle='--', label='Temperatura ambiente')
plt.title('Resfriamento do objeto ao longo do tempo')
plt.xlabel('Tempo (minutos)')
plt.ylabel('Temperatura (°C)')
plt.legend()#Adiciona as descrições no gráfico
plt.grid(True)#Gerar as linhas
plt.show()#Plota o gráfico
