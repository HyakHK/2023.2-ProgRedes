import random

def rDado(mensagem):
    mensagem = mensagem.split('d')
    Dquant = int(mensagem[0])
    dado = int(mensagem[1])
    result = []
    while Dquant > 0:
        result.append(str(random.randint(1, dado)))
        Dquant -= 1
    
    result = ' , '.join(result)
    return result