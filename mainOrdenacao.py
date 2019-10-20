import sys, time
from manipulaCSV import ManipulaCSV
from ordenacao import Ordenacao

class Executa():
    
    def __init__(self, alg, arqIn, arqOut):
        self.alg = alg
        self.arqIn = arqIn
        self.arqOut = arqOut
    
    def executa(self):
        # realiza leitura de arquivo
        instArquivo = ManipulaCSV(self.arqIn,'',[])
        vetor = instArquivo.leitura_arquivo()
        
        # realiza uma sequencia de tres testes
        for i in range(1,4):
            # realiza ordenacao
            instOrdenacao = Ordenacao(vetor)
            if self.alg == 'selectsort':
                inicio = time.time()
                ord = instOrdenacao.selectsort()
                fim = time.time()
                tam = instOrdenacao.calcula_tamanho()
            elif self.alg == 'insertsort':
                inicio = time.time()
                ord = instOrdenacao.insertsort()
                fim = time.time()
                tam = instOrdenacao.calcula_tamanho()
            elif self.alg == 'mergesort':
                inicio = time.time()
                ord = instOrdenacao.mergesort()
                fim = time.time()
                tam = instOrdenacao.calcula_tamanho()
            elif self.alg == 'quicksort':
                inicio = time.time()
                ord = instOrdenacao.quicksort()
                fim = time.time()
                tam = instOrdenacao.calcula_tamanho()
            elif self.alg == 'heapsort':
                inicio = time.time()
                ord = instOrdenacao.heapsort()
                fim = time.time()
                tam = instOrdenacao.calcula_tamanho()
            else:
                print("Algoritmo nao encontrado")
                break

            # realiza escrita de arquivo - errado
            #instEscrita = ManipulaCSV('',self.arqOut,ord)
            #instEscrita.escrita_arquivo()
        
            # calcula delta do tempo de execucao em milisegundos
            deltaTempo = (fim - inicio) * 1000
        
            # escreve do terminal as informacoes 
            print("%s   %s   %d   %.5f" %(i, self.alg, tam, deltaTempo))
        

def main(argv):
    
    # leitura das informacoes da linha de comando
    nomeAlg = sys.argv[1]
    nomeArqIn = sys.argv[2]
    nomeArqOut = sys.argv[3]
    
    # execucao do algoritmo
    fazer = Executa(nomeAlg, nomeArqIn, nomeArqOut)
    fazer.executa()       
    
if __name__=='__main__':
    main(sys.argv)