import numpy as np
from matplotlib import pyplot as plt


NUM_OVERLAP = 15

N = 1000
P = 120  
M = np.linspace(0.1, 1, num=NUM_OVERLAP) 
ITER = 20

ms2 = np.zeros((NUM_OVERLAP, ITER))

for i in range(NUM_OVERLAP):

	xi = np.random.randint(2, size=(P,N))
	xi[xi == 0] = -1

	J = np.dot(xi.T, xi) / N
	J = J - np.diag(np.diag(J)) 

	prb_x0 =  (1+M[i]*xi[:1])/2 
	filter_  = np.random.rand(1,N) 
    
	x0 = np.zeros((1, N))  
	x0[prb_x0 >= filter_] = 1
	x0[prb_x0 < filter_]  =  -1
	x = x0.T  

	ms2[i, 0]=np.dot(xi[:1],x)/N
    
	t = 0
	while t < ITER:

		input = np.dot(J,x) 
        
		x[input >= 0] = 1
		x[input < 0]  = -1

		ms2[i, t] = np.dot(xi[:1],x)/N
		t = t + 1

for i in range(NUM_OVERLAP):
    plt.plot(ms2[i, :], color='gray', lw=1)
    plt.xlabel('Time step $t$')
    plt.ylabel('Overlap $m$')
plt.show()
