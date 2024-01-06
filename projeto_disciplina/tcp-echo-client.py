import socket
import requests #Não esquecer de instalar requests
from socket_constants import *


#Update de mensagem do bot por id
def get_last_update_id():
    response = requests.get(f'{strURL}/getUpdates')
    updates = response.json()['result']
    if updates:
        return updates[-1]['update_id']
    return None

strURL = f'https://api.telegram.org/bot{API_KEY}'
last_update_id = get_last_update_id()

reqURL = requests.get(strURL + '/getUpdates')
retorno = reqURL.json()

# Testes de conexão bot

id_chat = retorno['result'][0]['message']['chat']['id']
# Criando o socket TDP
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_socket.connect((HOST_SERVER, SOCKET_PORT))

while True:
    updates = requests.get(f'{strURL}/getUpdates', params={'offset': last_update_id + 1}).json()['result']

    for update in updates:
        # Processar mensagem
        mensagem = update.get('message')
        if mensagem:
            chat_id = mensagem['chat']['id']
            text = mensagem['text']

            # Convertendo a mensagem digitada de string para bytes
            mensagem = text.encode(CODE_PAGE)
            # Enviando a mensagem ao servidor
            tcp_socket.send(mensagem)

            # Recebendo echo do servidor
            dado_recebido     = tcp_socket.recv(BUFFER_SIZE)
            mensagem_recebida = dado_recebido.decode(CODE_PAGE)
            dados = {'chat_id':id_chat, 'text':mensagem_recebida}
            post = requests.post(strURL + '/sendMessage',data=dados)


            # Failsafe para não repetir mesma mensagem
            last_update_id = max(last_update_id, update['update_id'])
            



# Fechando o socket
tcp_socket.close()