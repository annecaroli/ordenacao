import sys
import leituraCSV
import heapsort


def main(argv):
    # esta variavel guarda a quantidade de vezes que os testes serao realizados
    # para cada dupla de sort-dataset
    numTestes = 5

    # esta variavel quarda a chave de ordenacao
    chave = 'iud'

    # variavel que recebe um vetor com elementos a serem ordenados
    vetor = leituraCSV.leArquivo(sys.argv[1])
    #print(vetor)

    ordenado = heapsort.heapsort(vetor, chave)
    print(ordenado,'\n')

    #for i in numTestes:
        # chama o algoritmo sort
        # escreve o arquivo ordenado
        # escreve o resultado do tempo de execucao 

if __name__=='__main__':
    main(sys.argv)