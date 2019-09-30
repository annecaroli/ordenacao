import csv

def leArquivo(nomeArq):
    # preciso fazer a parada de encontrar o caminho generico
    caminho = '/home/annecaroli/Documents/repos/ordenacao/data/'
    arquivo = open(caminho + nomeArq)

    linhas = csv.reader(arquivo)
    next(linhas) # pula a linha de cabecalho do arquivo

    listaTermos = []
    for linha in linhas:
        dic = {}
        dic["email"] = linha[0]
        dic["gender"] = linha[1]
        dic["uid"] = linha[2]
        dic["birthdate"] = linha[3]
        dic["height"] = linha[4]
        dic["weight"] = linha[5]
        listaTermos.append(dic)
    return listaTermos