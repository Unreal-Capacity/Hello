#import numpy as np
#import pandas as pd 

#data = pd.read_csv("AB_NYC_2019.csv")
#min_t, max_t = data.price.quantile([0.01,0.999], interpolation="higher")
#datast = data[(data.price>min_t)&(data.price<max_t)]
#st = pd.DataFrame(datast.price)
from primePy import primes
def prime():
    counter = 0
    for a in range(2,n+1):
        if primes.check(a) == True:
            counter+=1
        continue
    print(counter)
    return
n = int(input("Enter any Number: "))
prime()