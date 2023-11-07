import sys
def criarList():
    try:
        file = open("C:/Users/HOME/Downloads/ports-ex/tabela.csv", "r", encoding='utf-8')
        file = file.read()
        list = file.split('\n')
        list.remove('')
    except:
        print(f"Erro: {sys.exc_info()[0]}")
    else:
        return list