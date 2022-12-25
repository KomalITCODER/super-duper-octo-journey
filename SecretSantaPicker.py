import random as rd
import pandas as pd
import numpy as np

Myfile=open('ListofPeople.txt', "r")
names=Myfile.readlines()

count=len(names)
presents=rd.sample(names,count)

check_self_present = np.array(np.array(names) == np.array(presents)).any()

while check_self_present:
    presents = rd.sample(names,count)
    check_self_present = np.array(np.array(names) == np.array(presents)).any()

pairs = [(names[i], presents[i]) for i in range(count)]   

for p in pairs:
    print(f'{p[0]} buys a presnts for {p[1]}')