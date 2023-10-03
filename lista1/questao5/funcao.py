import sys
def tenta():
    try:
        pass
    except:
        print('Erro:' ,sys.exc_info()[0] + "Tente novamente")