import os,sys
from funcao import *

try:
    here = os.path.dirname(os.path.abspath(__file__))
    ano = str(input("Qual ano do cartola: "))
    ctl = "cartola_fc_" + ano + ".txt"
    arquivo = os.path.join(here, "dados_cartola_fc", ctl)
    with open(arquivo,"r") as carai:
        content = carai.read()
        print(content)

except:
    print('Erro:' ,sys.exc_info()[0] + "Tente novamente")
