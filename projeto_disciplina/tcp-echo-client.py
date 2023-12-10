import socket
import requests
from socket_constants import *

strURL = f'https://api.telegram.org/bot{API_KEY}'

reqURL = requests.get(strURL + '/getUpdates')
retorno = reqURL.json()

# Testes de conexão bot
# print(reqURL.status_code)
# print(f'\n{retorno}')

id_chat = retorno['result'][0]['message']['chat']['id']
# Criando o socket TDP
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_socket.connect((HOST_SERVER, SOCKET_PORT))

while True:
    mensagem = input('Digite a mensagem: ')

    if mensagem:
        # Convertendo a mensagem digitada de string para bytes
        mensagem = mensagem.encode(CODE_PAGE)
        # Enviando a mensagem ao servidor      
        tcp_socket.send(mensagem)

        # Recebendo echo do servidor
        dado_recebido     = tcp_socket.recv(BUFFER_SIZE)
        mensagem_recebida = dado_recebido.decode(CODE_PAGE)
        dados = {'chat_id':id_chat, 'text':mensagem_recebida}
        post = requests.post(strURL + '/sendMessage',data=dados)

        print(f'Echo Recebido: {mensagem_recebida}')

# Fechando o socket
tcp_socket.close()