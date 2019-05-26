import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

xmin=-3
xmax=3
x=np.arange(xmin,xmax,0.1)

fig=plt.figure()

plt.xlim(xmin,xmax)
plt.grid()

pages=50

img=[0,0]
images=[]

for i in range(pages):

	y=np.sin(x+2*np.pi*(i/pages))
	img[0]=plt.plot(x,y,c='b')
	img[1]=plt.plot(0,np.sin(2*np.pi*(i/pages)),c='r',marker='o',markersize=12)
	images.append(img[0]+img[1])

ani_art=animation.ArtistAnimation(fig,images,interval=100)
plt.show()
ani_art.save("sindot.gif",writer='KaiTsumoto')
