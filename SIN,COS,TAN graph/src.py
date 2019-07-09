import numpy as np
import matplotlib.pyplot as plt
ix= ''
iy = ''
def onclick(event):
    
    global ix, iy
    try:
        ix, iy = event.xdata, event.ydata
        ix = round(ix,2)
        iy = round(iy,2)
        #print ('x = %.2f, y = %.2f'%(ix, iy))
        print('='*30)
        print('sin'+str(ix)+" : "+ str(round(np.sin(ix),2)))
        print('cos'+str(ix)+" : "+ str(round(np.cos(ix),2)))
        print('tan'+str(ix)+" : "+ str(round(np.tan(ix),2)))
  
        global coords
        coords = [ix, iy]
        
        return coords
    except:
        pass


X = np.linspace(-np.pi, np.pi, 256,endpoint=True) # 시작, 끝, 256개
C,S,T = np.cos(X), np.sin(X), np.tan(X)

fig = plt.figure(figsize=(10,6), dpi=80)
ax = fig.add_subplot()

plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="cosine")
plt.plot(X, S, color="red",  linewidth=2.5, linestyle="-", label="sine")
plt.plot(X, T, color="orange", linewidth=2.5, linestyle="-", label="tangent")



plt.xlim(X.min()*1.1, X.max()*1.1)
plt.ylim(C.min()*1.1, C.max()*1.1)

plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
plt.yticks([-1, 0, +1], [r'$-1$', r'$0$', r'$+1$'])


ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

plt.legend(loc='lower right', frameon=True)

t = 2*np.pi/3
t2 = 2*np.pi/12

plt.plot([t,t],[0,np.cos(t)], color ='blue', linewidth=1.5, linestyle="--")
plt.scatter([t,],[np.cos(t),], 50, color ='blue')

plt.plot([t,t],[0,np.sin(t)], color ='red', linewidth=1.5, linestyle="--")
plt.scatter([t,],[np.sin(t),], 50, color ='red')

plt.plot([t2,t2],[0,np.tan(t2)], color ='orange', linewidth=1.5, linestyle="--")
plt.scatter([t2,],[np.tan(t2),], 50, color ='orange')

plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
             xy=(t, np.sin(t)), xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
             xy=(t, np.cos(t)), xycoords='data',
             xytext=(-90, -50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.annotate(r'$\tan(\frac{\pi}{6})=\frac{\sqrt{3}}{3}$',
             xy=(t2, np.tan(t2)), xycoords='data',
             xytext=(-140, -50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

cid = fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()