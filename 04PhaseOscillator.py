import matplotlib
matplotlib.use('TKAgg')

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anime

N=2
K=0.0

omega_list=[(i/5)+5 for i in range(51)]

dt=0.01     
T=50           
M = int(T/dt)   
T0=T/2            
M0 = int(T0/dt)   

t=0
ph=[ 1.0, 1.5 ]

fig=plt.figure()

ims=[]

#variation of K for animation
for i in range(16):

	#variation of delta omega
	for omega0 in omega_list:

		omega=[ omega0, 10.0 ]
		t=0
		dph=[0,0]
		ph0_hist=[ ph[0] ]   
		ph1_hist=[ ph[1] ]  
		psi_hist=[ ph[0]-ph[1] ]
		domega_hist=[ ]
		dOmega_hist=[ ]
		t_hist=[t]
		
		#euler method
		for m in range (M): 
	    		
			dph[0]=(omega[0]+K*np.sin(ph[1]-ph[0]))*dt
			dph[1]=(omega[1]+K*np.sin(ph[0]-ph[1]))*dt
		
			for i in range (N):
				ph[i]=ph[i]+dph[i]
			t += dt
    
			ph0_hist.append(ph[0])
			ph1_hist.append(ph[1])
			psi_hist.append(ph[0]-ph[1]) 
			t_hist.append(t)

		Omega0=(ph0_hist[M]-ph0_hist[int(M/2)])/(T/2)
		Omega1=(ph1_hist[M]-ph1_hist[int(M/2)])/(T/2)
		domega=omega[0]-omega[1]
		dOmega=Omega0 - Omega1
	
		dOmega_hist.append(dOmega)
		domega_hist.append(domega)
	
	plt.xlabel('Δω')
	plt.ylabel('ΔΩ')
	plt.xlim(-5,5)
	plt.ylim(-5,5)
	im=plt.plot(domega,dOmega)
	ims.append(im)	

	K=K+0.1
	
ani = anime.FuncAnimation(fig, ims, interval=100)
#結果のプロット
plt.show()
