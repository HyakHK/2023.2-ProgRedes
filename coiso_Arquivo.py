import random

# flt = open('Lista_Nao_Ordenada.txt', 'w')
n = int(input("Digite o número de elementos: "))
lista = []

while n > 0:
    num = random.randint(1, 1000000)
    # nl = flt.write(num + '\n')
    lista.append(num)
    n = n - 1
# Sendo enviado para o documents
with open('C:/Users/20231014050039/Documents/Lista_Nao_Ordenada.txt' , 'w') as arquivo:
    ctl = arquivo.write(str(lista))
    print()
