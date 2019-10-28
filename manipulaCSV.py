import csv
import estrutura

class ManipulaCSV():
    
    def __init__(self, arqIn, arqOut, i, vetor):
        self.arqIn = arqIn
        self.arqOut = arqOut
        self.i = str(i)
        self.vetor = vetor
        self.listaRegistros = []
    
    def leitura_arquivo(self):
        caminho = '/home/annecaroli/Documents/repos/ordenacao/dados/'
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
    
        arquivo.close()
    
    
    def escrita_arquivo(self):
        arq = self.arqIn[:-4] + "_" + self.arqOut + "_" + self.i
        
        with open(arq, mode='w') as csvfile:
            escreve = csv.writer(csvfile, delimiter=';')
            escreve.writerow(['email', 'gender', 'uid', 'birthdate', 'height', 'weight'])
            for i in range(len(self.vetor)):
                escreve.writerow([self.vetor[i].get_email(),
                                 self.vetor[i].get_gender(),
                                 self.vetor[i].get_uid(),
                                 self.vetor[i].get_birthdate(),
                                 self.vetor[i].get_height(),
                                 self.vetor[i].get_weight()])
        csvfile.close()
