from random import randint
import sys,os

here = os.path.dirname(os.path.abspath(__file__))

def gerar_lista(ls_int):
    try:
        rng = []
        for l in range(ls_int[0]):
            rng.append(randint(ls_int[1],ls_int[2]))
        certo = True
    except:
        print('Erro:' ,sys.exc_info()[0])
        certo = False
        rng = None
    return certo, rng
    
def salvar_lista(lista, bl):
    gen = (str(el) for el in lista)
    sep = '\n'
    lista = sep.join(gen)
    trg = "s" 
    r = True

    while trg == "s":
        try:
            trg = "n"
            nome_lista = input('Digite o nome da lista: ')
            nome_arquivo = input('Digite o nome do arquivo: ')

            # Criar o diretório se não existir
            os.makedirs(os.path.join(here, nome_arquivo), exist_ok=True)

            # Caminho completo para o arquivo
            arquivo_path = os.path.join(here, nome_arquivo, f"{nome_lista}.txt")

            with open(arquivo_path, "w") as new_created_file:
                new_created_file.write(lista)
                new_created_file.write("\n" + str(bl))
                


        except Exception as e:
            r = False
            print(f"Erro: {e}. Não foi possível salvar corretamente.")

            try:
                print("Fechará se o digito não for escolhido corretamente")
                trg = str(input("Tentar salvar lista novamente [s/n]: "))
            except:
                print('Ta de gracinha dnv, volta ao inicio')
                trg = "n"

    return r    

# def salvar_lista():
#     #Repeticao para nao comecar no inicio
#     trg =="s"
#     while trg == "s":
#         try:
#             r = True
#             nome_lista = input('Digite o nome da lista: ')
#             nome_arquivo = input('Digite o nome da arquivo: ')
#         try:
#             os.mkdir(here + f"//{nome_arquivo}")
#             with open(f"lista1\\questao1\\{nome_arquivo}\\{nome_lista}.txt", "w") as new_created_file:

#         except:
#             with open(f"lista1\\questao1\\{nome_arquivo}\\{nome_lista}.txt", "w") as new_created_file:
            
#         except:
#             r = False
#             print(sys.exc_info()[0], "Não salvo corretamente")
#             try:
#                 trg = str(input("Tentar salvar lista novamente[s/n]"))
#             except:
#                 print('Ai é foda so por isso volta do inicio')
#                 trg = "n"
#     return r
    