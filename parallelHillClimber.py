from solution import SOLUTION
import constants
import os
import copy

class PARALLEL_HILL_CLIMBER:

    def __init__(self):
        # self.parent = SOLUTION()

        os.system("rm brain*.nndf")
        os.system("rm fitness*.txt")

        self.nextAvailableID = 0


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

        for currentGeneration in  range(1):
            self.Evolve_For_One_Generation()





    def Evolve_For_One_Generation(self):

        self.Spawn()
        #
        # self.Mutate()
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
            self.chidren[x].Mutate()




    def Select(self):
        for x in range(len(self.parents)):
            if self.children[x].fitness < self.parents[x].fitness:
                self.parents[x] = self.children[x]

    def Print(self):

        print(" ")
        for x in range(len(self.parents)):
            print(self.parents[x].fitness, self.children[x].fitness)

        print(" ")



    def Show_Best(self):
        # os.system("python3 simulate.py GUI")
        best = 100
        bestIndex = 0
        for x in range(len(self.parents)):
            if self.parents[x].fitness < best:
                bestIndex = x
                best = self.parents[x].fitness
        self.parents[bestIndex].Start_Simulation("GUI")
        print(best)


    def Evaluate(self, solutions):
        directOrGUI = "DIRECT"
        for x in range(0,constants.populationSize):
            solutions[x].Start_Simulation(directOrGUI)

        for x in range(0, constants.populationSize):
            solutions[x].Wait_For_Simulation_To_End(directOrGUI)