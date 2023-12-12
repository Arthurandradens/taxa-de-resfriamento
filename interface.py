from PySimpleGUI import Window, Button,Text, Image,Input, Column, HSeparator,Push, theme
import matplotlib.pyplot as plt
import numpy as np

theme('darkblue9')

def calcula_resfriamento(temperatura_ambiente,temperatura_inicial,constante_resfriamento,tempo_total,intervalo_tempo):
    num_pontos = int(tempo_total / intervalo_tempo)

    # Arrays para armazenar os valores do tempo e da temperatura
    tempos = np.linspace(0, tempo_total, num_pontos)#vai gerar um array intervalo com base no tempo total / intervalo
    temperaturas = np.zeros(num_pontos)#vai criar as temperaturas zeradas com base nos pontos
    temperaturas[0] = temperatura_inicial #definir a temperatura inicial

    # Calculando a temperatura para cada intervalo de tempo
    for i in range(1, num_pontos):
        derivada = constante_resfriamento * (temperaturas[0] - temperatura_ambiente) * np.exp(-constante_resfriamento * (tempos[i]))#Derivada do newton
        temperaturas[i] = temperaturas[i-1] - derivada
    # Plotando o gráfico
    plt.figure(figsize=(10, 10))#Define o tamanho do gráfico
    plt.plot(tempos, temperaturas, label='Temperatura do objeto')
    plt.axhline(y=temperatura_ambiente, color='r', linestyle='--', label='Temperatura ambiente')
    plt.title('Resfriamento do objeto ao longo do tempo')
    plt.xlabel('Tempo (minutos)')
    plt.ylabel('Temperatura (°C)')
    plt.legend()#Adiciona as descrições no gráfico
    plt.grid(True)#Gerar as linhas
    plt.show()


layout_esquerda = [
        [Text('********* Descubra a taxa de resfriamento do seu telhado *********')],
        [Image(filename='telhado2.png')],
]

layout_direita = [

    
    [Text('Temperatura do ambiente(Graus):'),Input(key='temp_ambiente')],
    [Text('Temperatura inicial do objeto:      '),Input(key='temp_inicial')],
    [Text('Constante de resfriamento:         '),Input(key='constante_resfriamento')],
    [Text('Tempo total:                              '),Input(key='tempo_total')],
    [Text('Intervalo de tempo:                     '),Input(key='intervalo_tempo')],
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
                temperatura_ambiente = float(values['temp_ambiente'])
                temperatura_inicial = float(values['temp_inicial'])
                constante_resfriamento = float(values['constante_resfriamento'])
                tempo_total = float(values['tempo_total'])
                intervalo_tempo = float(values['intervalo_tempo'])
                calcula_resfriamento(temperatura_ambiente,temperatura_inicial,constante_resfriamento,tempo_total,intervalo_tempo)
                
        case None:
              break    
         
window.close()
