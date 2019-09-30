def heapify(vetor, tam, indice):
    maior = indice
    esq = (2 * indice) + 1
    dir = (2 * indice) + 2

    if esq < tam and vetor[esq] > vetor[maior]:
        maior = esq

    if dir < tam and vetor[dir] > vetor[maior]:
        maior = dir

    if maior != indice:
        vetor[indice], vetor[maior] = vetor[maior], vetor[indice]
        heapify(vetor, tam, maior)


def heapsort(vetor, chave):
    n = len(vetor)

    for i in range(n, -1, -1):
        heapify(vetor[i], n, i)

    for i in range(n - 1, 0, -1):
        vetor[i], vetor[0] = vetor[0], vetor[i]
        heapify(vetor[i], i, 0)


# Verify it works
#random_list_of_nums = [35, 12, 43, 8, 51]
#heapsort(random_list_of_nums,0)
#print(random_list_of_nums)

# link: https://stackabuse.com/sorting-algorithms-in-python/#heapsort