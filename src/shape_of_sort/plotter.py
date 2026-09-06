import matplotlib
import matplotlib.pyplot as plt
from random import shuffle
import matplotlib.animation as animation
import numpy as np

from shape_of_sort.algs import  heapsort,radix_sort_lsd, quicksort_hoare, quicksort_lomuto,bubble
from shape_of_sort.algs import merge
from shape_of_sort.algs import prepare_data
from shape_of_sort.algs import selection

n_cells = 512
start_data = prepare_data(n_cells, shuffled=True, reverse=False)
trace, compares = merge(start_data[:],base=13)

theta = np.linspace(0,2*np.pi,num=n_cells)
matplotlib.use('macosx')

def dist(cells: list[int]) -> list[int]:
    n = len(cells)-1
    return [1-abs((x-i)/n) for (i,x) in enumerate(cells)]

fig, axs = plt.subplots(1,2, subplot_kw={'projection': 'polar'})
axs[0].yaxis.set_visible(False)
axs[0].xaxis.set_visible(False)
axs[1].yaxis.set_visible(False)
axs[1].xaxis.set_visible(False)
line0, = axs[0].plot(theta, dist(trace[0]),'.-', markersize=3)
line1, = axs[1].plot(trace[0], dist(trace[0]),'.', markersize=3)

def animate(i):
    line0.set_ydata(dist(i))  # update the data.
    line1.set_ydata(dist(i))  # update the data.
    line1.set_xdata(i)
    return [line0, line1]


ani = animation.FuncAnimation(
    fig, animate,frames=trace, interval=33,  blit=False, repeat=True)
# To save the animation using Pillow as a gif
# ani.save("movie.mp4",fps=30)
plt.show()
