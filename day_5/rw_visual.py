import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk(50000)
rw.fill_walk()

plt.style.use('classic')
fig, ax = plt.subplots(figsize=(15, 9))
point_numbers = range(rw.num_points)
ax.scatter(rw.x_value, rw.y_value, c=point_numbers,
           cmap=plt.cm.Blues, s=1, edgecolors='none')

ax.scatter(0, 0, c='green', edgecolors='none', s=10)
ax.scatter(rw.x_value[-1], rw.y_value[-1], edgecolors='none', c='red', s=10)

ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
plt.show()
