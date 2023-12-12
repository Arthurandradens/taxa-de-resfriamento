import matplotlib.pyplot as plt
import numpy as np

# Constantes para o problema (ajuste conforme necessário)
Ta = 25  # Temperatura ambiente em graus Celsius
T = 80   # Temperatura inicial do objeto em graus Celsius
k = 0.1  # Constante de resfriamento

# Intervalo de tempo e número de pontos para o gráfico
t = 60  # Tempo total em minutos
intervalo_tempo = 1  # Intervalo de tempo entre cada ponto em min
num_pontos = int(t / intervalo_tempo)

# Arrays para armazenar os valores do tempo e da temperatura
tempos = np.linspace(0, t, num_pontos)#vai gerar um array intervalo com base no tempo total / intervalo
temperaturas = np.zeros(num_pontos)#vai criar as temperaturas zeradas com base nos pontos
temperaturas[0] = T #definir a temperatura inicial

# Calculando a temperatura para cada intervalo de tempo
for i in range(1, num_pontos):
    derivada = k * (temperaturas[0] - Ta) * np.exp(-k * (tempos[i]))#Derivada do newton
    temperaturas[i] = temperaturas[i-1] - derivada

# Plotando o gráfico
plt.figure(figsize=(10, 10))#Define o tamanho do gráfico
plt.plot(tempos, temperaturas, label='Temperatura do objeto')
plt.axhline(y=Ta, color='r', linestyle='--', label='Temperatura ambiente')
plt.title('Resfriamento do objeto ao longo do tempo')
plt.xlabel('Tempo (minutos)')
plt.ylabel('Temperatura (°C)')
plt.legend()#Adiciona as descrições no gráfico
plt.grid(True)#Gerar as linhas
plt.show()