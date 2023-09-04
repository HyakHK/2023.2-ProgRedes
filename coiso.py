#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      20231014050039
#
# Created:     04/09/2023
# Copyright:   (c) 20231014050039 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
import random

# flt = open('Lista_Nao_Ordenada.txt', 'w')
n = int(input("Digite o número de elemntos"))
lista = []

while n > 0:
    num = str(random.randint(1, 1000000))
    # nl = flt.write(num + '\n')
    lista.append(num)
    n = n - 1

with open('Lista_Nao_Ordenada.txt' , 'w') as arquivo:
    ctl = arquivo.write(str (list))




