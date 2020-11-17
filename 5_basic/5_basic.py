import numpy as np
import matplotlib.pyplot as plt
import time
start = time.time()

#root parameter
C=2
m=100
#Transcendental
n=100

def newton_root():
    x[0]=1
    for i in range(m):
        x[i+1]=(x[i]+C/x[i])/2
    print(x[m])
    return x

def newton_Transcendental():
    xx[0]=4
    for i in range(n):
        xx[i+1]=xx[i]-(np.tan(xx[i])-1/xx[i])/(1/(np.cos(xx[i]))**2-np.log(xx[i]))
        delt=(np.tan(xx[i])-1/xx[i])/(1/(np.cos(xx[i]))**2-np.log(xx[i]))
    print(xx[i])
    print(delt)
    return xx
if __name__=='__main__':
    x=np.zeros(m+1)
    x=newton_root()

    xx=np.zeros(n+1)
    xx=newton_Transcendental()
