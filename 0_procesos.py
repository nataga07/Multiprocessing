"""
0_procesos
usuario:nataga07
"""

from time import sleep
from random import random

from multiprocessing import Process

def f():
    for i in range(5):
        print ("hola", i)
        sleep(random())
        
if __name__ == "__main__":
    p = Process(target=f)
    q = Process(target=f)
    p.start()
    q.start()
    print ("fin")

