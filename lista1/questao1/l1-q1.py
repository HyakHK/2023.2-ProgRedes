import sys,os

n_rep = 0
ls_int = []
while n_rep < 3:
    try:
        inteiro = int(input('Digite 3 numeros inteiros'))
        ls_int.append(inteiro)
        n_rep = n_rep + 1
    except ValueError:
        print("Invalido, tente um numero inteiro")
    except:
        print('Erro desconhecido:' ,sys.exec_info()[0])



# arquivo open

# DIRETORIO = os.path.dirname(os.path.abspath(__file__))
# NOMEARQUIVO = DIRETORIO + '\\valores_nao_ordenados.txt'
