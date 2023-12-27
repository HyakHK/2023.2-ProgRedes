import socket
import threading
from socket_constants import *
from comandos import *

print('Recebendo Mensagens...\n\n')

def clientInt(conexao, cliente):
    mensagem = b''
    while mensagem != b'/q':
        try:
            mensagem = conexao.recv(BUFFER_SIZE)
            print(cliente, mensagem.decode(CODE_PAGE))
            opt = {'/t' : teste(cliente[0]),
                   '/s' : s_info()
                }
            comando = opt[mensagem.decode(CODE_PAGE)]
            mensagem_retorno = comando
            print(mensagem_retorno)
            conexao.send(mensagem_retorno.encode(CODE_PAGE))
        except:
            mensagem = b'/q'
    allClient.remove((conexao, cliente))
    conexao.close()




try:
    allClient = []

    # Criando o socket TCP
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Ligando o socket a porta
    tcp_socket.bind((HOST_SERVER, SOCKET_PORT))
    # Máximo de conexões enfileiradas
    tcp_socket.listen(MAX_LISTEN)

    while True:
        # Aceita a conexão com o cliente
        conexao, cliente = tcp_socket.accept()
        print('Conectado por: ', cliente)
        allClient.append((conexao ,cliente))
        tClient = threading.Thread(target=clientInt, args=(conexao ,cliente))
        tClient.start()
        tClient.join()

except Exception as e:
    print("Erro: ", e)



