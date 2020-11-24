import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.broken_barh([(0, 50), (60, 20), (80, 10)], (0, 2),
               facecolors=('tab:orange', 'tab:green', 'tab:red'))
ax.set_xlim(0, 200)
ax.set_xlabel('seconds since start')
ax.set_yticks([5, 10])
ax.set_yticklabels([])

plt.show()