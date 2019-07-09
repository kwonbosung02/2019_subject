import matplotlib.pyplot as plt

plt.figure(figsize=(16, 4))
plt.margins(0.1, 0.1)
for x in range(0, 8):
    for y in range(0, 4):
        plt.scatter(x, y, c='b')
        plt.text(x+0.1, y, "point({}, {})".format(x, y), fontsize=10)

plt.show()