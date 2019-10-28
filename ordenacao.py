class Ordenacao():
    
    def __init__(self, vetor):
        lista = []
        for item in vetor:
            lista.append(item)
        self.lista = lista
      
    def selectsort(self):
        array = self.lista
        for i in range(len(array)):
            menorIndex = i
            for j in range(i+1, len(array)):
                if array[j].get_uid() < array[menorIndex].get_uid():
                    menorIndex = j
            
            array[i], array[menorIndex] = array[menorIndex], array[i]
            
    def insertsort(self):
        array = self.lista
        for i in range(1, len(array)): 
            chave = array[i]
            j = i-1
            while j >= 0 and chave.get_uid() < array[j].get_uid(): 
                array[j+1] = array[j] 
                j -= 1
            array[j+1] = chave
            
    def mergesort(self, array): 
        if len(array) > 1: 
            meio = len(array) // 2
              
            instEsq = Ordenacao(array[:meio])
            self.mergesort(instEsq.lista)
            
            instDir = Ordenacao(array[meio:])
            self.mergesort(instDir.lista)
  
            i = j = k = 0
          
            while i < len(instEsq.lista) and j < len(instDir.lista): 
                if instEsq.lista[i].get_uid() < instDir.lista[j].get_uid(): 
                    array[k] = instEsq.lista[i] 
                    i+=1
                else: 
                    array[k] = instDir.lista[j] 
                    j+=1
                k+=1
          
            while i < len(instEsq.lista): 
                array[k] = instEsq.lista[i] 
                i+=1
                k+=1
          
            while j < len(instDir.lista): 
                array[k] = instDir.lista[j] 
                j+=1
                k+=1

    def partition(self, array, menor, maior): 
        i = (menor - 1)
        pivot = array[maior]
  
        for j in range(menor, maior):  
            if array[j].get_uid() < pivot.get_uid():  
                i = i + 1 
                array[i], array[j] = array[j], array[i] 
        array[i+1], array[maior] = array[maior], array[i+1] 
        return (i + 1) 
 
    def quicksort(self, array, menor, maior):
        if menor < maior:  
            pi = self.partition(array, menor, maior)  
            self.quicksort(array, menor, pi-1) 
            self.quicksort(array, pi+1, maior) 
            
    def heapify(self, array, n, i): 
        maior = i 
        esq = 2 * i + 1 
        dir = 2 * i + 2 
   
        if esq < n and array[i].get_uid() < array[esq].get_uid(): 
            maior = esq 
        if dir < n and array[maior].get_uid() < array[dir].get_uid(): 
            maior = dir  
        if maior != i: 
            array[i], array[maior] = array[maior], array[i] 
            self.heapify(array, n, maior)
    
    def heapsort(self): 
        array = self.lista
        n = len(array) 
        
        for i in range(n, -1, -1): 
            self.heapify(array, n, i) 
        for i in range(n - 1, 0, -1): 
            array[i], array[0] = array[0], array[i] 
            self.heapify(array, i, 0) 
    
    """        
    def timsort(self, array, n): 
        RUN = 32
        for i in range(0, n, RUN):
            array = array[i:min((i+31), (n-1))]
            instIns = Ordenacao(array)  
            instIns.insertsort()
        
        tam = RUN 
        while tam < n:
            for esq in range(0, n, 2 * tam):  
                #meio = esq + tam - 1 
                #dir = min((esq + 2 * tam - 1), (n - 1))
                instNovoArray = Ordenacao(array)
                self.mergesort(instNovoArray) 
            tam = 2 * tam
    """ 
    
    def printa_ordenado(self):
        for item in self.lista:
            print(item)

    def calcula_tamanho(self):
        i = 0
        while i < len(self.lista):
            i = i + 1
        return i