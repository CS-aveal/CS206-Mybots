from solution import SOLUTION
import constants
from tempfile import TemporaryFile
import numpy as np
import os
import copy

class PARALLEL_HILL_CLIMBER:

    def __init__(self):
        # self.parent = SOLUTION()

        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")

        self.nextAvailableID = 0

        self.row = 0
        self.col = 0

        self.parents = {}
        for x in range(0, constants.populationSize):
            self.parents[x] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID = self.nextAvailableID + 1




    def Evolve(self):
        directOrGUI = "DIRECT"
        #self.parent.Evaluate(directOrGUI)
        #
        # for currentGeneration in  range(constants.numberOfGenerations):
        #     self.Evolve_For_One_Generation()

        # for x in range(0,constants.populationSize):
        #     self.parents[x].Start_Simulation(directOrGUI)
        #
        # for x in range(0, constants.populationSize):
        #     self.parents[x].Wait_For_Simulation_To_End(directOrGUI)

        self.Evaluate(self.parents)

        # for x in range(0,constants.populationSize):
        #     self.Evolve_For_One_Generation()
        #UNEEDED CODE

        for currentGeneration in  range(constants.numberOfGenerations):
            self.Evolve_For_One_Generation()
            self.row = self.row + 1
            constants.rownum = self.row





    def Evolve_For_One_Generation(self):

        self.Spawn()
        #
        self.Mutate()
        #
        # directOrGUI = "DIRECT"
        #
        self.Evaluate(self.children)

        #
        self.Print()
        #
        self.Select()




    def Spawn(self):
        # self.child =  copy.deepcopy(self.parent)
        #
        # self.child.Set_ID(self.nextAvailableID)
        # self.nextAvailableID = self.nextAvailableID + 1

        self.children = {}

        for x in range(len(self.parents)):
            self.getID = copy.deepcopy(self.parents[x])
            ID = self.nextAvailableID
            self.getID.Set_ID(ID)
            self.nextAvailableID = self.nextAvailableID + 1
            self.children[x] = SOLUTION(ID)





    def Mutate(self):
        for x in range(len(self.children)):
            self.children[x].Mutate()




    def Select(self):
        for x in range(len(self.parents)):
            if self.children[x].fitness < self.parents[x].fitness:
                self.parents[x] = self.children[x]
                if (constants.rownum % constants.numberOfGenerations == 0):
                    # it is in the first row
                    constants.row1.insert(self.parents[x].col, self.parents[x].fitness)
                elif (constants.rownum % constants.numberOfGenerations == 1):
                    # its the second row
                    constants.row2.insert(self.parents[x].col, self.parents[x].fitness)
                elif (constants.rownum % constants.numberOfGenerations == 2):
                    # it is in the third row
                    constants.row3.insert(self.parents[x].col, self.parents[x].fitness)
                elif (constants.rownum % constants.numberOfGenerations == 3):
                    # its the second row
                    constants.row4.insert(self.parents[x].col, self.parents[x].fitness)
                elif (constants.rownum % constants.numberOfGenerations == 4):
                    # its the second row
                    constants.row5.insert(self.parents[x].col, self.parents[x].fitness)
                elif (constants.rownum % constants.numberOfGenerations == 5):
                    # its the second row
                    constants.row6.insert(self.parents[x].col, self.parents[x].fitness)
                elif (constants.rownum % constants.numberOfGenerations == 6):
                    # its the second row
                    constants.row7.insert(self.parents[x].col, self.parents[x].fitness)
                elif (constants.rownum % constants.numberOfGenerations == 7):
                    # its the second row
                    constants.row8.insert(self.parents[x].col, self.parents[x].fitness)
                elif (constants.rownum % constants.numberOfGenerations == 8):
                    # its the second row
                    constants.row9.insert(self.parents[x].col, self.parents[x].fitness)
                elif (constants.rownum % constants.numberOfGenerations == 9):
                    constants.row10.insert(self.parents[x].col, self.parents[x].fitness)
            # its the second row
            else:
                if (constants.rownum % constants.numberOfGenerations == 0):
                    # it is in the first row
                    constants.row1.insert(self.parents[x].col, self.children[x].fitness)
                elif (constants.rownum % constants.numberOfGenerations == 1):
                    # its the second row
                    constants.row2.insert(self.parents[x].col, self.children[x].fitness)
                elif (constants.rownum % constants.numberOfGenerations == 2):
                    # it is in the third row
                    constants.row3.insert(self.parents[x].col, self.children[x].fitness)
                elif (constants.rownum % constants.numberOfGenerations == 3):
                    # its the second row
                    constants.row4.insert(self.parents[x].col, self.children[x].fitness)
                elif (constants.rownum % constants.numberOfGenerations == 4):
                    # its the second row
                    constants.row5.insert(self.parents[x].col, self.children[x].fitness)
                elif (constants.rownum % constants.numberOfGenerations == 5):
                    # its the second row
                    constants.row6.insert(self.parents[x].col, self.children[x].fitness)
                elif (constants.rownum % constants.numberOfGenerations == 6):
                    # its the second row
                    constants.row7.insert(self.parents[x].col, self.children[x].fitness)
                elif (constants.rownum % constants.numberOfGenerations == 7):
                    # its the second row
                    constants.row8.insert(self.parents[x].col, self.children[x].fitness)
                elif (constants.rownum % constants.numberOfGenerations == 8):
                    # its the second row
                    constants.row9.insert(self.parents[x].col, self.children[x].fitness)
                elif (constants.rownum % constants.numberOfGenerations == 9):
                    # its the second row
                    constants.row10.insert(self.parents[x].col, self.children[x].fitness)

        #this is the actual robot for the generation population iteration


    def Print(self):

        print(" ")
        for x in range(len(self.parents)):
            print(self.parents[x].fitness, self.children[x].fitness)

        print(" ")



    def Show_Best(self):
        # os.system("python3 simulate.py GUI")
        best = 100
        bestIndex = 0
        print("showbest")
        for x in range(len(self.parents)):
            print(self.parents[x].myID)
            if self.parents[x].fitness < best:
                bestIndex = x
                best = self.parents[x].fitness
        self.parents[bestIndex].Start_Simulation("GUI")
        print(best)
        constants.matrix.append(constants.row1)
        constants.matrix.append(constants.row2)
        constants.matrix.append(constants.row3)
        constants.matrix.append(constants.row4)
        constants.matrix.append(constants.row5)
        constants.matrix.append(constants.row6)
        constants.matrix.append(constants.row7)
        constants.matrix.append(constants.row8)
        constants.matrix.append(constants.row9)
        constants.matrix.append(constants.row10)
        print(constants.matrix)
        a = np.matrix([constants.row1, constants.row2, constants.row3, constants.row4, constants.row5, constants.row6, constants.row7, constants.row8, constants.row9, constants.row10])
        mystring = ''
        #x = np.arange(a)
        for x in constants.matrix:
            mystring += '' + str(x)
        # f = open("matrix.txt", "w")
        # np.save(f,constants.matrix)
        # f.close()
        outfile = TemporaryFile()
        with open('testB.npy', 'wb') as f:
            np.save(f,constants.matrix)


    def Evaluate(self, solutions):
        directOrGUI = "DIRECT"
        for x in range(0,constants.populationSize):
            solutions[x].Start_Simulation(directOrGUI)

        for x in range(0, constants.populationSize):
            solutions[x].Wait_For_Simulation_To_End(directOrGUI)