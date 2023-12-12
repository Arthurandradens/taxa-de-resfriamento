from PySimpleGUI import Window, Button,Text, Image,Input, Column, HSeparator,Push, theme
import matplotlib.pyplot as plt
import numpy as np

theme('Reddit')

def calcula_resfriamento(Ta,T,k,t):
    lista_tempo = list(range(0,t))  # Cria uma lista de tempo que vai de acordo com o tempo(t)
    lista_temperatura = np.zeros(t)  # cria uma lista de zeros que vai de acordo com o tempo(t)
    lista_temperatura[0] = T  # Define que o primeiro valor da lista vai ser a temperatura inicial(T)

    i = 1  # Valor de inicio do loop
    # Cálculo da derivada de newton que calcula a taxa de resfriamento de um objeto com base no tempo
    while i < t:
        lista_temperatura[i] = Ta + (T - Ta) * np.exp(-k * i)  # Converte o logaritmo para um número real
        i += 1

    plt.figure(figsize=(10, 10))  # Define o tamanho do gráfico
    plt.plot(lista_tempo, lista_temperatura, label='Temperatura do objeto')
    plt.axhline(y=Ta, color='r', linestyle='--', label='Temperatura ambiente')
    plt.title('Resfriamento do objeto ao longo do tempo')
    plt.xlabel('Tempo (minutos)')
    plt.ylabel('Temperatura (°C)')
    plt.legend()  # Adiciona as descrições no gráfico
    plt.grid(True)  # Gerar as linhas
    plt.show()  # Plota o gráfico


layout_esquerda = [
        [Text(' Descubra a taxa de resfriamento do seu telhado ')],
        [Image(filename='telhado2.png')],
]

layout_direita = [

    
    [Text('Temperatura do ambiente(Graus):'),Input(key='Ta')],
    [Text('Temperatura inicial do objeto:      '),Input(key='T')],
    [Text('Constante de resfriamento:         '),Input(key='k')],
    [Text('Tempo total:                              '),Input(key='t')],
    [Push(),Button('Calcular', size=(20,1)),Push()],
]

layout = [
    [layout_esquerda],
    [ HSeparator()  ],
    [layout_direita ]
]

window = Window(
    'Taxa de Resfriamento',
    layout=layout,
    element_justification='c'
)
while True : 
    event, values = window.read()

    match(event):
        case 'Calcular':
                temperatura_ambiente = float(values['Ta'])
                temperatura_inicial = float(values['T'])
                constante_resfriamento = float(values['k'])
                tempo_total = int(values['t'])
                calcula_resfriamento(temperatura_ambiente,temperatura_inicial,constante_resfriamento,tempo_total)
                
        case None:
              break    
         
window.close()
