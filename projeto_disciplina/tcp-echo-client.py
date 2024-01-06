import socket
import requests
import threading
from socket_constants import *

strURL = f'https://api.telegram.org/bot{API_KEY}'

# Update de mensagem do bot por id
def get_last_update_id():
    response = requests.get(f'{strURL}/getUpdates')
    updates = response.json()['result']
    if updates:
        return updates[-1]['update_id']
    return None

def receive_messages():
    while True:
        mensagem_recebida = tcp_socket.recv(BUFFER_SIZE).decode(CODE_PAGE)
        print(f'Mensagem Recebida do Servidor: {mensagem_recebida}')
        dados = {'chat_id': id_chat, 'text': mensagem_recebida}
        post = requests.post(strURL + '/sendMessage', data=dados)

# Criando o socket TCP
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectando ao servidor
tcp_socket.connect((HOST_SERVER, SOCKET_PORT))

# Obtendo o ID do chat
reqURL = requests.get(strURL + '/getUpdates')
retorno = reqURL.json()
id_chat = retorno['result'][0]['message']['chat']['id']

# Obtendo o último update ID
last_update_id = get_last_update_id()

# Criando uma thread para receber mensagens do servidor
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

try:
    while True:
        # Obtendo updates do Telegram
        updates = requests.get(f'{strURL}/getUpdates', params={'offset': last_update_id + 1}).json()['result']

        for update in updates:
            mensagem = update.get('message')
            if mensagem:
                text = mensagem['text']

                # terminação cliente
                if text == '/q':
                    raise KeyboardInterrupt  #CTRL + C

                # Convertendo a mensagem digitada de string para bytes
                mensagem_bytes = text.encode(CODE_PAGE)
                # Enviando a mensagem ao servidor
                tcp_socket.send(mensagem_bytes)

                # Failsafe para não repetir mesma mensagem
                last_update_id = max(last_update_id, update['update_id'])
except KeyboardInterrupt:
    print('Encerrando cliente...')
finally:
    # Aguardando o encerramento da thread de recebimento
    receive_thread.join()

    # Fechando o socket
    tcp_socket.close()
