import random

def rDado(mensagem):
    mensagem = mensagem.split('d')
    Dquant = int(mensagem[0])  # Convert string to integer
    dado = int(mensagem[1])    # Convert string to integer
    result = []
    while Dquant > 0:
        result.append(str(random.randint(1, dado)))  # Convert the result to string
        Dquant -= 1
    
    result = ' , '.join(result)
    return result

# Example usage:
mensagem = "3d6"  # You can replace this with your desired input
print(rDado(mensagem))