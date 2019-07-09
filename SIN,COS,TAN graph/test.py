import matplotlib.pyplot as plt
 
 
fig, ax = plt.subplots()
 
ax.set(xlim=[-2, 2], ylim=[-2, 2])
ax.set_aspect('equal', adjustable='box')
 
xdata = [0]
ydata = [0]
line, = ax.plot(xdata, ydata)
x =10
y =10 
 
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
plt.scatter(5, 5, c='b')
plt.text(5+0.1, 5, "point({}, {})".format(5, 5), fontsize=10)

cid = plt.connect('button_press_event', add_point)
plt.figure(figsize=(16, 4))



plt.scatter(x, y, c='b')
plt.text(x+0.1, y, "hjdshfjdsgfhjgdshgfhjsd", fontsize=10)
plt.show()