import os,sys
from function import *
try:
    hereAnt = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    q1P = str(input('Digite o nome da pasta: '))
    q1L = str(input('Digite o nome da lista: '))
    if q1L.endswith('.txt'):
        ...
    else:
        q1L = q1L + '.txt'
    nome_arquivo = os.path.join(hereAnt,'questao1',q1P,q1L)
    try:
        f = open(nome_arquivo)
        f.close
    except:
        print('Arquivo não existente')
        exit()
        
    
    lido = ler_arquivo(nome_arquivo)

    lista = ordena_lista(lido)
    print(lista)
except:
    print('Erro:' ,sys.exc_info()[0] + "Tente novamente")
