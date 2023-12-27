import socket
import threading
import requests
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
# print(reqURL.status_code)
# print(f'\n{retorno}')


def close_socket():
    try:
        tcp_socket.close()
    except Exception as e:
        print("Error closing socket:", e)

def client_interaction():
    while True:
        try:
            updates = requests.get(f'{strURL}/getUpdates', params={'offset': last_update_id + 1}).json()['result']

            for update in updates:
                message = update.get('message')
                if message:
                    chat_id = message['chat']['id']
                    text = message['text']
                    # Convertendo a mensagem digitada de string para bytes
                    messagem = text.encode(CODE_PAGE)
                    # Enviando a mensagem ao servidor
                    tcp_socket.send(messagem)
                    
                    last_update_id = max(last_update_id, update['update_id'])
        
        except Exception as e:
            print("Error in client interaction:", e)
            break

    close_socket()

def server_interaction():
    while True:
        try:
            received_data = tcp_socket.recv(BUFFER_SIZE)
            received_message = ("\n" + received_data.decode(CODE_PAGE))
            data = {'chat_id': id_chat, 'text': received_message}
            post = requests.post(strURL + '/sendMessage', data=data)
        except Exception as e:
            print("Error in server interaction:", e)
            break

    close_socket()

try:
    id_chat = retorno['result'][0]['message']['chat']['id']
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.connect((HOST_SERVER, SOCKET_PORT))
    
    t_server = threading.Thread(target=server_interaction)
    t_user = threading.Thread(target=client_interaction)

    t_user.start()
    t_server.start()

    t_user.join()
    t_server.join()

except Exception as e:
    print("Error:", e)