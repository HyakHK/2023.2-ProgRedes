import socket
import threading
from socket_constants import *
from comandos import *

def handle_client(connection, client_address):
    print('Conectado por: ', client_address)

    while True:
        mensagem = connection.recv(BUFFER_SIZE)
        if not mensagem:
            break
        print(client_address, mensagem.decode(CODE_PAGE))

        # Devolvendo uma mensagem ao cliente
        try:
            mensagem_retorno = rDado(mensagem.decode(CODE_PAGE))
        except Exception as e:
            mensagem_retorno = str(e)

        connection.send(mensagem_retorno.encode(CODE_PAGE))

    print('Finalizando Conexão do Cliente ', client_address)
    connection.close()

# Criando o socket TCP
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Ligando o socket a porta
tcp_socket.bind((HOST_SERVER, SOCKET_PORT))

# Máximo de conexões enfileiradas
tcp_socket.listen(MAX_LISTEN)

print('Recebendo Mensagens...\n\n')

while True:
    # Aceita a conexão com o cliente
    conexao, cliente = tcp_socket.accept()

    # Criando uma thread para lidar com o cliente
    client_thread = threading.Thread(target=handle_client, args=(conexao, cliente))
    client_thread.start()
