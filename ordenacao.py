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
            
    def mergesort(self):
        array = self.lista
        if len(array) > 1: 
            meio = len(array) // 2
            esq = array[:meio]  
            dir = array[meio:] 
  
        instEsq = Ordenacao(esq)
        instEsq.mergesort()
        instDir = Ordenacao(dir) 
        instDir.mergesort() 
        i = j = k = 0
           
        while i < len(esq) and j < len(dir): 
            if esq[i] < dir[j]: 
                array[k] = esq[i] 
                i+=1
            else: 
                array[k] = dir[j] 
                j+=1
            k+=1
          
        while i < len(esq): 
            array[k] = esq[i] 
            i+=1
            k+=1
          
        while j < len(dir): 
            array[k] = dir[j] 
            j+=1
            k+=1

    def partition(array,low,high): 
        i = ( low-1 )
        pivot = arr[high] 
  
        for j in range(low , high): 
            if   arr[j] < pivot: 
                i = i+1 
                arr[i],arr[j] = arr[j],arr[i] 
  
        arr[i+1],arr[high] = arr[high],arr[i+1] 
        return ( i+1 ) 

    def quicksort(array,menor,maior): 
        if menor < maior: 
            pi = partition(array,menor,maior) 
            quickSort(arr, low, pi-1) 
            quickSort(arr, pi+1, high)
            
    def heapify(self, array, n, i): 
        maior = i 
        esq = 2 * i + 1
        dir = 2 * i + 2
  
        if esq < n and array[i] < array[esq]: 
            maior = esq 
        if dir < n and array[maior].get_uid() < array[dir].get_uid(): 
            maior = dir 
        if maior != i: 
            array[i],array[maior] = array[maior],array[i] 
  
        #self.heapify(array, n, maior) 

    def heapsort(self):
        array = self.lista 
        n = len(array) 
   
        for i in range(n, -1, -1): 
            self.heapify(array, n, i) 

        for i in range(n-1, 0, -1): 
            array[i], array[0] = array[0], array[i]
            self.heapify(array, i, 0)
    
    def printa_ordenado(self):
        for item in self.lista:
            print(item)
            
    def calcula_tamanho(self):
        i = 0
        while i < len(self.lista):
            i = i + 1
        return i