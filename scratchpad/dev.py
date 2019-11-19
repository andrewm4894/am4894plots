
# taken from here: https://stackoverflow.com/a/17903145/1919374

import matplotlib.pylab as plt
import matplotlib.animation as animation
import numpy as np


n_data = 100
n_cols = 2
im_list = []

data = np.random.rand(n_data, 10, 10)

fig, axes = plt.subplots(n_cols)

repeat_length = (np.shape(image)[0]+1)/4
for n in range(n_cols):
    axes[n].set_xlim([0, repeat_length])
    axes[n].autoscale_view()
    axes[n].set_ylim([np.amin(data[:, 5, 5]), np.amax(data[:, 5, 5])])

im1, = axes[0].plot([], [], color=(0, 0, 1))
im2, = axes[1].plot([], [], color=(0, 0, 1))


def func(n):
    im1.set_xdata(np.arange(n))
    im1.set_ydata(image[0:n, 5, 5])
    im2.set_xdata(np.arange(n))
    im2.set_ydata(image[0:n, 5, 5])
    if n > repeat_length:
        axes[0].set_xlim(n-repeat_length, n)
        axes[1].set_xlim(n - repeat_length, n)
    else:
        axes[0].set_xlim(0, repeat_length)
        axes[1].set_xlim(0, repeat_length)
    return im1, im2

ani = animation.FuncAnimation(fig, func, frames=image.shape[0], interval=30, blit=False)

ani.save('tmp/animation.mp4')

plt.show()

