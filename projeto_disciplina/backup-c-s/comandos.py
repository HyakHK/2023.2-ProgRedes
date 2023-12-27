


import subprocess


def teste(cliente):
    resultado = subprocess.run(f'ping {cliente}', shell=True, capture_output=True, text=True).stdout
    return resultado

def s_info():
    resultado = subprocess.run('systeminfo',shell=True, capture_output=True, text=True).stdout
    return resultado