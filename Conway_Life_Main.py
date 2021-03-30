##--------------------------------------------------##
## Developer : Vikas Maggo                          ##
## -------------------------------------------------##

# From Wikipedia : At each step in time following transition may occur 
#1 Any live cell with fewer than two live neighbours dies, as if by underpopulation.
#2 Any live cell with two or three live neighbours lives on to the next generation.
#3 Any live cell with more than three live neighbours dies, as if by overpopulation.
#4 Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

#These rules, which compare the behavior of the automaton to real life, can be condensed into the following:

#1 Any live cell with two or three live neighbours survives.
#2 Any dead cell with three live neighbours becomes a live cell.
#3 All other live cells die in the next generation. Similarly, all other dead cells stay dead.

from Conway_Methods import *     
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

if __name__ =="__main__" : 
    width, height = 7,7
    Grid = Matrix(width,height)

    while True :
        os.system("cls")
        Grid.generate_array()
        # set up animation
        Grid.helper()
        # fig, ax = plt.subplots()
        # mat = ax.matshow(grid)
        # ani = animation.FuncAnimation(fig, grid, interval=1,save_count=5)
        # plt.show()
        time.sleep(5)
