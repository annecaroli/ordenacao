import matplotlib.pyplot as plt
import numpy as np

def calcula_media(vetor):
    media = []
    for i in vetor:
        # calcula a media e guarda apenas a parte inteira do resultado 
        media.append(int(np.average(i)))
    return media

def plota_grafico(eixoX, eixoY, nomeAlg):
    plt.plot(eixoX, eixoY)
    plt.title(nomeAlg)
    plt.xlabel('Amostra')
    plt.ylabel('Media do Tempo de Execucao (ms)')
    plt.show()

# define um array para os algoritmos de ordenacao por comparacao (eixoX_A)
# e outro para algoritmos de ordenacao (eixoX_B)
eixoX_A = ['10e1', '25e1', '50e1', '75e1',
           '10e2', '25e2', '50e2', '75e2',
           '10e3', '25e3', '50e3', '75e3',
           '10e4']

eixoX_B = ['25e1', '50e1', '75e1', '10e2',
         '25e2', '50e2', '75e2', '10e3',
         '25e3', '50e3', '75e3', '10e4',
         '25e4', '50e4', '75e4', '10e5',
         '25e5']

# array com os resultados dos testes

selectsortValues = np.array([[2.11310, 2.02084, 1.95003], [17.03596, 14.14299, 13.23915], [46.71907, 54.62217, 53.11179],
                             [101.18580, 110.43000, 106.98509], [199.03803, 202.26693, 197.77608],
                             [1177.14500, 1197.52693, 1228.38616], [5717.59605, 5909.05499, 5565.86194],
                             [15339.23602, 15036.38387, 14518.83698], [26449.18600, 27937.18600, 26882.33590],
                             [192817.49487, 197150.57111, 187150.09212], [2029920.86387, 2086766.81590, 2130942.33298],
                             [4589602.12207, 4761193.15195, 4906238.47198], [3546783.23293, 3716081.87008, 3798506.14786]])

insertsortValues = np.array([[1.17922, 1.10412, 1.67704], [7.14517, 7.43699, 9.75299], [29.14000, 29.60515, 38.23185], 
                             [64.69011, 66.81490, 68.84003], [115.61704, 119.19212, 115.80515],
                             [690.90104, 755.00894, 786.54003], [3075.92487, 3747.07007, 2896.95883], 
                             [8073.87185, 6859.01499, 7085.11400], [12449.91207, 13847.05806, 12849.79510], 
                             [96813.83991, 96473.34909, 96572.30210], [434553.23911, 430834.27811, 429554.38995],
                             [1164616.85181, 1127190.02485, 1062476.47214], [1833686.11598, 1848744.86303, 1919494.12084]])

mergesortValues = np.array([[4.12607, 4.39310, 3.85189], [7.93409, 8.78215, 8.72493], [12.61091, 11.31988, 10.73003],
                            [13.31687, 12.61592, 14.98294], [27.58002, 38.79905, 33.78201], [57.88612, 70.87708, 67.13295],
                            [96.60602, 99.85685, 104.36988], [130.02396, 140.36393, 137.86983],
                            [363.24501, 367.14506, 410.17509], [775.48003, 941.75792, 920.69888],
                            [1337.24999, 1727.84305, 1339.27584], [1795.32695, 2172.92905, 1830.10697],
                            [5603.74689, 5241.56404, 4899.22595], [10460.78610, 9962.14104, 10073.19307],
                            [15660.55679, 15618.73603, 16579.28395], [21625.26798, 21567.35897, 22208.21309],
                            [57243.89100, 58727.94104, 58241.66393]])

quicksortValues = np.array([[2.07686, 2.01797, 1.98412], [5.04518, 5.16510, 4.05407], [4.97413, 6.12211, 4.06814],
                            [8.77404, 6.35004, 6.75988], [21.30699, 30.14779, 36.91101], [39.28590, 45.47596, 58.30193],
                            [67.01708, 72.33000, 72.27492], [90.31010, 102.82993, 101.12095], [271.47079, 263.47995, 250.96893],
                            [596.48514, 648.17882, 629.01998], [975.39306, 987.26296, 1312.35909],
                            [1274.80483, 1300.31800, 1296.46397], [4862.75816, 3684.67784, 3688.65299],
                            [8057.96719, 8033.79607, 8073.11988], [12699.70298, 12205.39403, 13186.55300], 
                            [18314.17322, 18977.70095, 17484.50002], [48647.28403, 48375.62323, 48763.81516]])

heapsortValues = np.array([[2.65098, 2.95901, 2.43497], [11.28912, 6.61898, 5.17201], [8.33201, 12.95400, 12.72297],
                          [13.04984, 12.66217, 13.01098], [35.27308, 38.94782, 39.98685],
                          [82.10795, 79.82302, 80.09410], [119.49110, 126.83201, 126.40095],
                          [177.99401, 184.06582, 178.46894], [501.35398, 580.56903, 591.88604],
                          [1110.83889, 1155.86686, 1248.25978], [1703.10903, 1711.59387, 1714.92600],
                          [2420.08901, 2437.46710, 2423.74587], [2420.08901, 2437.46710, 2423.74587],
                          [16608.13594, 15670.38608, 15704.56409],[25166.83507, 24487.05721, 24687.76393],
                          [34403.07307, 34765.60521, 32957.41296], [95587.67104, 94937.18719, 96265.73610]])

# passa pela funcao que calcula eixoY (que e a media) para cada algoritmo
eixoY_SS = calcula_media(selectsortValues)
eixoY_IS = calcula_media(insertsortValues)
eixoY_MS = calcula_media(mergesortValues)
eixoY_QS = calcula_media(quicksortValues)
eixoY_HS = calcula_media(heapsortValues)

# passa pela funcao que plota o grafico
graficoSS = plota_grafico(eixoX_A, eixoY_SS, 'Selectsort')
graficoIS = plota_grafico(eixoX_A, eixoY_IS, 'Insertsort')
graficoMS = plota_grafico(eixoX_B, eixoY_MS, 'Mergesort')
graficoQS = plota_grafico(eixoX_B, eixoY_QS, 'Quicksort')
graficoHS = plota_grafico(eixoX_B, eixoY_HS, 'Heapsort')

# plota infos do selectsort e insertsort
plt.plot(eixoX_A, eixoY_SS, label='Selectsort')
plt.plot(eixoX_A, eixoY_IS, label='Insertsort')
plt.title('Comparacao Selectsort x Insertsort')
plt.xlabel('Amostra')
plt.ylabel('Media do Tempo de Execucao (ms)')
plt.legend()
plt.show()

# plota infos do merge, quick e heapsort
plt.plot(eixoX_B, eixoY_MS, label='Mergesort')
plt.plot(eixoX_B, eixoY_QS, label='Quicksort')
plt.plot(eixoX_B, eixoY_HS, label='Heapsort')
plt.title('Comparacao Mergesort x Quicksort x Heapsort')
plt.xlabel('Amostra')
plt.ylabel('Media do Tempo de Execucao (ms)')
plt.legend()
plt.show()
