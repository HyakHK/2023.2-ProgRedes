import socket,sys
from separar import *

strHost = 'www.ifrn.edu.br'

ipHost = socket.gethostbyname(strHost)
list = criarList()

for n in list:
    item = n.split(';')
    port = int(item[0].strip('\ufeff'))
    proto = item[1]
    desc = item[2]
    sock = socket.socket(family= socket.AF_INET, type= socket.SOCK_STREAM)
    sock.settimeout(3)
    try:
        conn = sock.connect_ex((ipHost,port))
        if conn == 0:
            stat = 'aberto'
        else:
            stat = 'fechado'
    except:
        pass
        #print(f"Erro: {port} ------{sys.exc_info()[0]}")
    else:
        print(f'Porta: {port} | Protocolo: {proto} |  Descrição: {desc} |  {stat}')
        sock.close()

