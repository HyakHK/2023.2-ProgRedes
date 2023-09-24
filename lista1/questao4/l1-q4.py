from funcao import *
import zipfile,os,sys

zipName = "serie_historica_anp.zip"
fdName = "serie_historica_anp"
here = os.path.dirname(os.path.abspath(__file__))
sha = here + '\\serie_historica_anp'

criarDir()
extrair(zipName)
uniteFd()
lstCreate()