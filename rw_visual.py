import matplotlib.pyplot as plt

from random_walk import RandomWalk
while True:

    #make a random walk
    rw = RandomWalk()
    rw.fill_walk()

    #plot the points in the walk
    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, s =15)
    ax.set_aspect('equal')
    plt.show()

    keep_running = input("make another walk? (y/n): ")
    if keep_running == 'n':
        break