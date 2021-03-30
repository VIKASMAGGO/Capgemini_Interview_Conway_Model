import numpy as np
import random
import time
import os
from tkinter.ttk import * 
from tkinter import *  

#Cellular Automation 
#The matrix is made up of an mxn cells and each cell has an initial state - live - represented by 1 and dea - represented 
# by 0 , each cell interacts with its 8 neighbours , i.e horizontally , vertically and diagnonally traversing using rules mentioned
# below. 

# From Wikipedia : At each step in time following transition may occur 
#1 Any live cell with fewer than two live neighbours dies, as if by underpopulation.
#2 Any live cell with two or three live neighbours lives on to the next generation.
#3 Any live cell with more than three live neighbours dies, as if by overpopulation.
#4 Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

#These rules, which compare the behavior of the automaton to real life, can be condensed into the following:

#1 Any live cell with two or three live neighbours survives.
#2 Any dead cell with three live neighbours becomes a live cell.
#3 All other live cells die in the next generation. Similarly, all other dead cells stay dead.

class Matrix:
    def __init__(self,width,height) : 

        #Initialise the temporary array 
        self.width=width
        self.height=height
        self.createMatrix = np.zeros((self.width,self.height),dtype=int)

    def generate_array(self):
        for j in range(self.width):
            for i in range(self.height):
                self.createMatrix[j][i] = random.randint(0,1)


    #Helper Function - Check up , down and diagonal 
    def helper(self):

        tmp = [[None]*self.height for _ in range(self.width) ] 
        for j in range(self.width):
            for i in range(self.height):
                tmp[j][i] = self.find_neighbour(j,i)
 
        for j in range(self.width):
            for i in range(self.height):
                self.createMatrix[j][i] = tmp[j][i]

        print(self.createMatrix) 

    def find_neighbour(self, rows, cols):
        count = 0
        # co-ordinates we need to check - 8 directions 
        #Check if it is live then increase the counter by 1 
        for x in range(-1, 2):
            for y in range(-1, 2):
                #Find the close neighbours , vertical , horizontal and diagonal if gets 1 then count + 1 
                  # compute 8-neghbor sum 
                if 0 <= rows + y < self.width and 0 <= cols + x < self.height and  self.createMatrix[rows+y][cols+x] == 1 : 
                    count = count+1

            if self.createMatrix[rows][cols]  ==1 : 
                if count < 2 : 
                    return 0 
                elif 2<=count<=3 : 
                    return 1 
                else : 
                    return 0 
            else: 
                if count ==3 : 
                    return 1 
                else : 
                    return 0 
            
