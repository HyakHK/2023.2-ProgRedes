


import subprocess


def teste(cliente):
    resultado = subprocess.run(f'ping {cliente}', shell=True, capture_output=True, text=True).stdout
    return resultado