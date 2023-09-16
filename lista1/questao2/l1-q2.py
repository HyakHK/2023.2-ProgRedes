import os,sys


try:
    hereAnt = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    q1A = str(input('Digite o nome do arquivo localizado'))
    q1L = str(input('Digite o nome da lista'))
    print()
except:
    print('Erro:' ,sys.exc_info()[0] + "Tente novamente")