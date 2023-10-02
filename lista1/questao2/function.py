
import array
def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            content = arquivo.read()
        lido = True
    except:
        lido = False
        content = None
    
    return lido and content

def ordena_lista(lido):
    try:

        match str(input('Tipo de ordenação(todas maiusculas)')):
            case 'BUBBLE':
                lista = ordena_bubble(lido)
            case 'INSERTION':
                lista = ordena_insertion(lido)
            case 'SELECTION':
                lista = ordena_selection(lido)
            case 'QUICK':
                lista = ordena_quick(lido)
        ordenada = True
    except:
        ordenada = False
        lista = None
    return ordenada and lista


def ordena_bubble(lido):
    n = len(lido)
    if n <= 1:
        swapped = False
        for i in range(n-1):
            for j in range(0, n-i-1):
                if lido[j] > lido[j + 1]:
                    swapped = True
                    lido[j], lido[j + 1] = lido[j + 1], lido[j]
            if not swapped:
                return

def ordena_insertion(lido):
    n = len(lido)
    #Retornar se possuir 1 elemento ou menor
    if n <= 1:
        return
    for i in range(1, n):
        key = lido[i]
        j = i-1
        while j >= 0 and key < lido[j]: #movimentar maior para o lado
            lido[j + 1] = lido[j] #mevo para dito lado(é a direita so para saber)
            j =- 1
        lido[j + 1] = key

def ordena_selection(lido):
    size = len(lido)

    for ind in range(size):
        min_index = ind
        for j in range(ind + 1, size): #Selecionar menor
            if array[j] < array[min_index]:
                min_index = j
            #posicionamento
        (array[ind], array[min_index]) = (array[min_index], array[ind])

def partition(array,low,high):
    pivot = array[high]
    i = low - 1
    #comparar com pivot
    for j in range(low, high):
        if array[j] <= pivot:
            #se maior que pivot trocar por elemento apontado
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    #trocar elementon pivot por maior
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    #Resumo conta no i e usa numero i como comparação para o maior
    return i + 1



def ordena_quick(lido):
    high = len(lido) - 1
    low = 0

    if low < high :
        pi = partition(lido, low, high)
        #chamada esquerda
        ordena_quick(lido, low, pi - 1)
        #chamada direta
        ordena_quick(lido, pi - 1, high)


