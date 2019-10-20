import csv
import estrutura

class ManipulaCSV():
    
    def __init__(self, arqIn, arqOut, vetor):
        self.arqIn = arqIn
        self.arqOut = arqOut
        self.vetor = vetor
        self.listaRegistros = []
    
    def leitura_arquivo(self):
        # preciso fazer a parada de encontrar o caminho generico
        caminho = '/home/annecaroli/Documents/repos/ordenacao/data/'
        arquivo = open(caminho + self.arqIn)

        linhas = csv.reader(arquivo)
        next(linhas) # pula a linha de cabecalho do arquivo

        for linha in linhas:
            novoRegistro = estrutura.Estrutura()
            novoRegistro.set_email(linha[0])
            novoRegistro.set_gender(linha[1])
            novoRegistro.set_uid(linha[2])
            novoRegistro.set_birthdate(linha[3])
            novoRegistro.set_height(linha[4])
            novoRegistro.set_weight(linha[5])
            self.listaRegistros.append(novoRegistro)
        return self.listaRegistros
    
    # refazer
    def escrita_arquivo(self):
        arq = self.arqOut
        
        with open('arq', mode='w') as csvfile:
            escreve = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
            escreve.writerow(['email', 'gender', 'uid', 'birthdate', 'height', 'weight'])
            #for linha in self.vetor:
                #escreve.writerow(linha)
            #csvfile.close()
    