import os
from funcao import *

here = os.path.dirname(os.path.abspath(__file__))
dump_locate = os.path.join(here,'tcp_dump','cap1.dump')

with open (dump_locate,'rb') as yesn:
    print(yesn.read())

