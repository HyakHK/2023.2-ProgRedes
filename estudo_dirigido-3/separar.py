import sys, os
def criarList():
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        file = open(here + "/tabela.csv", "r", encoding='utf-8')
        file = file.read()
        list = file.split('\n')
        list.remove('')
    except:
        print(f"Erro: {sys.exc_info()[0]}")
    else:
        return list