import numpy as np
import matplotlib.pyplot as plt
import time
start = time.time()

eta=2.0
sep=4
dtaw=0.05
deta=eta/sep
ita=100

def rayleigh():

    for n in range(ita):
        for k in range(2,sep+1):
            U[k]=U[k]+dtaw*((U[k+1]-2*U[k]+U[k-1])/(deta)**2+(k-1)*(U[k+1]-U[k-1]))
    return U



if __name__=='__main__':
    U=np.zeros(sep+2)
    U[1]=1
    U[-1]=0
    rayleigh()
    etag=np.zeros(sep+2)
    for i in range(1,sep+2):
        etag[i]=(i-1)*deta

    print(U)
    print(etag)
    plt.rcParams['font.family'] ='Times New Roman'
    plt.rcParams['mathtext.fontset'] = 'stix'
    plt.figure()
    plt.subplot(111)
    plt.xlabel("U")
    plt.ylabel('$\eta$')
    plt.plot(U[1:sep+2], etag[1:sep+2],"k",marker='o')
    plt.show()

    elapsed_time = time.time() - start
    print("elapsed_time:{0}".format(elapsed_time))
