import os, rarfile
here = os.path.dirname(os.path.abspath(__file__))
dump_locate = os.path.join(here,'tcp_dump')


def extract_dump():

    r = rarfile.RarFile(dump_locate + '.rar')
    r.extractall() 
    r.close()

extract_dump()

def ler_dump():
    with open (dump_locate , 'r'):
        ...


#ler_dump()