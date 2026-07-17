import numpy as np
import matplotlib.pyplot as plt
SKY_BLUE=(153/255,187/255,221/255)
SIZE=800
COUNT=120
def hrt(t):
    x=16*(np.sin(t)**3)
    y=13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t)
    s=17
    c=SIZE/2
    return c+x*s,c-y*s
fig,ax=plt.subplots(figsize=(8,8),dpi=120)
ax.set_xlim(0,SIZE)
ax.set_ylim(SIZE,0)
ax.set_axis_off()
t = np.linspace(0, 2*np.pi, 120, endpoint=False)
for i in range(COUNT):
    j=(i+COUNT//2)%COUNT
    x1,y1=hrt(t[i])
    x2,y2=hrt(t[j])
    ax.plot([x1,x2],[y1,y2],c=SKY_BLUE,lw=0.4)
plt.show()
