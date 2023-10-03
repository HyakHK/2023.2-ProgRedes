import os,sys
here = os.path.dirname(os.path.abspath(__file__))
arq = str(input("nome do arquivo"))
nome_arquivo = os.path.join(here, 'fotos', arq)
def get_image_type(nome_arquivo):
    boolSucesso = False
    strTipoArq = None
    strErro = None
    #metadados e quantos bypes são
    try:
        with open(nome_arquivo, 'rb') as conteudo:
            if conteudo.read() == b'\xFF\xD8\xFF':
                strTipoArq = 'Jpg'
                boolSucesso = True
            elif conteudo.read() == b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a':
                strTipoArq = 'Png'
                boolSucesso = True

    except:
        strErro = sys.exc_info()[0]
    return boolSucesso, strTipoArq

print(get_image_type(nome_arquivo))
