import matplotlib
matplotlib.use('TKAgg')

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anime

N=2
K=0.0

D=51 #kinds of omega
omega_list=[(i/5)+5 for i in range(D)]

dt=0.01     
T=50           
M = int(T/dt)   
T0=T/2            
M0 = int(T0/dt)   
P=5 #fig pattern

t=0
ph=[ 1.0, 1.5 ]

fig =plt.figure()

domega_hist=np.empty((P,D))
dOmega_hist=np.empty((P,D))

#variation of K for animation
for i in range(P):

	#variation of delta omega
	for j in range(D):
	
		omega=[ omega_list[j], 10.0 ]
		t=0
		dph=[0,0]
		ph0_hist=[ ph[0] ]   
		ph1_hist=[ ph[1] ]  
		psi_hist=[ ph[0]-ph[1] ]
		t_hist=[t]
		
		#euler method
		for m in range (M): 
	    		
			dph[0]=(omega[0]+K*np.sin(ph[1]-ph[0]))*dt
			dph[1]=(omega[1]+K*np.sin(ph[0]-ph[1]))*dt
		
			for k in range (N):
				ph[k]=ph[k]+dph[k]
			t += dt
    
			ph0_hist.append(ph[0])
			ph1_hist.append(ph[1])
			psi_hist.append(ph[0]-ph[1]) 
			t_hist.append(t)

		Omega0=(ph0_hist[M]-ph0_hist[int(M/2)])/(T/2)
		Omega1=(ph1_hist[M]-ph1_hist[int(M/2)])/(T/2)
		domega=omega[0]-omega[1]
		dOmega=Omega0 - Omega1

		dOmega_hist[i,j]=dOmega
		domega_hist[i,j]=domega

	ax=fig.add_subplot(1,P,1+i)
	ax.set_xlabel("Δω")
	ax.set_ylabel("ΔΩ")
	ax.set_xlim(-5,5)
	ax.set_ylim(-5,5)
	ax.set_title("$K=$"+str(K))
	ax.scatter(domega_hist[i,:],dOmega_hist[i,:])

	K=K+0.5
	
#結果のプロット
plt.tight_layout()
plt.show()
