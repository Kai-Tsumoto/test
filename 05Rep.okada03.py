import numpy as np
from matplotlib import pyplot as plt
import matplotlib.animation as animation

NUM_OVERLAP = 15

N = 1000
P = 120  
M = np.linspace(0.1, 1, num=NUM_OVERLAP) 
ITER = 30

fig=plt.figure()

im=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ims=[]

plt.xlabel('Time step $t$')
plt.ylabel('Overlap $m$')
plt.xlim(0,ITER)
plt.ylim(0.0,1.0)

for k in range(ITER):

	np.random.seed(0)
	ms2 = np.zeros((NUM_OVERLAP, k+1))

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
		while t <= k :

			input = np.dot(J,x) 
        
			x[input >= 0] = 1
			x[input < 0]  = -1

			ms2[i, t] = np.dot(xi[:1],x)/N
			t = t + 1

	for i in range(NUM_OVERLAP):
		im[i]=plt.plot(ms2[i, :], color='red', lw=1)
		print(ms2[i,:])

	ims.append(im[0]+im[1]+im[2]+im[3]+im[4]+im[5]+im[6]+im[7]+im[8]+im[9]+im[10]+im[11]+im[12]+im[13]+im[14])

ani_art = animation.ArtistAnimation(fig, ims, interval=200)

plt.show()

#ani_art.save("Hopfield_network.gif")
