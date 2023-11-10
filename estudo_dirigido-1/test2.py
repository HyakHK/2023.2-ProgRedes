import subprocess,os
here = os.path.dirname(os.path.abspath(__file__))
arq = str(input("nome do arquivo: "))
nome_arquivo = os.path.join(here, 'fotos', arq)
print(nome_arquivo)
exeProcess = "hachoir-metadata"
process = subprocess.Popen([exeProcess,nome_arquivo],
						stdout=subprocess.PIPE,
						stderr=subprocess.STDOUT,
						universal_newlines=True)
Dic={}

for tag in process.stdout:
		line = tag.strip().split(':')
		Dic[line[0].strip()] = line[-1].strip()

for k,v in Dic.items():
	print(k,':', v)
