import zipfile,os,sys

zipName = "serie_historica_anp.zip"
fdName = "serie_historica_anp"
here = os.path.dirname(os.path.abspath(__file__))
sha = here + '\\serie_historica_anp'

#Criar diretorio dados_estatisticos no mesmo diretorio do .py
def criarDir():
    try:
        os.mkdir(here + "\\dados_estatisticos", exist_ok=True)
    except:
        print('Erro:' ,sys.exc_info()[0])

criarDir()


#extrair do arquivo zipado serie_historica_anp.zip
def extrair(zipName):
    try:
        filename = os.path.join(here, zipName)
        with zipfile.ZipFile(filename, 'r') as archive:
            archive.extractall("lista1/questao4")
    except:
        print('Erro:' ,sys.exc_info()[0])
extrair(zipName)


def uniteFd():
    with open("lista1\\questao4\\.tempList.txt", "w") as new_created_file:
        files_in_directory = os.listdir(sha)
        for name in files_in_directory:
            file_path = os.path.join(sha, name)
            try:
                with open(file_path, 'r') as file:
                    for line in file:
                        line = line.replace(';;',';')
                        new_created_file.write(line)
                    new_created_file.write("\n")
            
            except Exception as e:
                print(f"Erro ao abrir o arquivo {file_path}: {e}")

uniteFd()

#Refazer
def lstCreate():
    lstNew = []
    with open("lista1\\questao4\\.tempList.txt", "r") as tempFile:
        lstTemp = (tempFile.read()).split("\n")
    for l in range(len(lstTemp)):
        item = lstTemp[l]
        item = item.split(";")
        lstNew.append(item)
    if lstNew.count(['']) > 0:
        lstNew.remove([''])
    if lstNew.count('') > 0:
        lstNew.remove('')
        #da lista 0,1,10,11,12,15
    return lstNew

lstNew = lstCreate()
#Organizar lista para salvar no dados_estatisticos
def data_lst(lstNew):
    print(lstNew)
    Flist = []
    with open(here + "\dados_estatisticos\serie_historica_ano.txt", "w") as new_created_file:
        for i in range(len(lstNew)):
            Flist.append(lstNew[i][0])
            Flist.append(lstNew[i][1])
            Flist.append(lstNew[i][10])
            Flist.append(lstNew[i][11])
            Flist.append(lstNew[i][12])
            try:
                Flist.append(lstNew[i][15]) #disfuncional
            except:
                Flist.append('BRANCA')
        
        
data_lst(lstNew)


















def ending():
    os.remove("lista1\\questao4\\.tempList.txt")
#ending()





#Teste mostrar arquivos .csv dentro de um diretorio
# def callFile(zipName):
#     try:
#         filename = os.path.join(here, zipName)

#         with zipfile.ZipFile(filename, 'r') as archive:
#             files = [name for name in archive.namelist() if name.endswith('.csv')]
        
#         for file in files:
#             print(file)
#     except:
#         print('Erro:' ,sys.exc_info()[0])

# callFile(zipName)
