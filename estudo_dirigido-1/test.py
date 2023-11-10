import subprocess
import os

here = os.path.dirname(os.path.abspath(__file__))
arq = str(input("nome do arquivo: "))
nome_arquivo = os.path.join(here, 'fotos', arq)

exeProcess = "hachoir-metadata"
process = subprocess.Popen([exeProcess, nome_arquivo],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT,
                           universal_newlines=True)

output, _ = process.communicate()

Dic = {}

for tag in output.splitlines():
    line = tag.strip().split(':')
    Dic[line[0].strip()] = line[-1].strip()

for k, v in Dic.items():
    print(k, ':', v)


    #c:\Users\HOME\Documents\GitHub\2023.2-ProgRedes\estudo_guiado-1\fotos\2.png