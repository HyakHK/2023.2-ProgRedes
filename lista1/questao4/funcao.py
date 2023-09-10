import zipfile,os,sys

flName = "serie_historica_anp.zip"

def extrair(flName):
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        filename = os.path.join(here, flName)
        with zipfile.ZipFile(filename, 'r') as archive:
            archive.extractall("lista1/questao4")
    except:
        print('Erro:' ,sys.exc_info()[0])
extrair(flName)

# def callFile(flName):
#     try:
#         here = os.path.dirname(os.path.abspath(__file__))
#         filename = os.path.join(here, flName)

#         with zipfile.ZipFile(filename, 'r') as archive:
#             files = [name for name in archive.namelist() if name.endswith('.csv')]
        
#         for file in files:
#             print(file)
#     except:
#         print('Erro:' ,sys.exc_info()[0])

# callFile(flName)
