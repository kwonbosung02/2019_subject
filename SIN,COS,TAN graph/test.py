import matplotlib.pyplot as plt
 
 
fig, ax = plt.subplots()
 
ax.set(xlim=[-2, 2], ylim=[-2, 2])
ax.set_aspect('equal', adjustable='box')
 
xdata = [0]
ydata = [0]
line, = ax.plot(xdata, ydata)
 
 
def add_point(event):
    if event.inaxes != ax:
        return
 
    if event.button == 1:
        x = event.xdata
        y = event.ydata
        xdata.append(x)
        ydata.append(y)
        line.set_data(xdata, ydata)
        plt.draw()
 
    if event.button == 3:
        xdata.append(0)
        ydata.append(0)
        line.set_data(xdata, ydata)
        plt.draw()
        plt.disconnect(cid)
 

cid = plt.connect('button_press_event', add_point)

plt.show()