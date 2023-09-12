import sys,os
from funcao import *
# Respectivamente quantidade, valor min e valor max
n_rep = 0
ls_int = []
while n_rep < 3:
    try:
        #1 quantidade, 2 valor min, 3 valor max
        inteiro = int(input(f'Digite o {n_rep + 1} numero inteiro: '))
        ls_int.append(inteiro)
        n_rep = n_rep + 1
    except:
        print('Erro:' ,sys.exc_info()[0] + "Tente novamente")

lista = gerar_lista(ls_int)


salvar_lista(lista)